import sys
import re
import itertools

start_coord = None
maze = []
travelers = []
start_re = re.compile("S")

class MazeTraveler:
    maze_legend = {
        ".": [],
        "|": [(0, 1), (0, -1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)]
        # Should never encounter S as it is the start
        # "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]
    }

    @staticmethod
    def is_valid_start(maze_start, traveler_first_step, given_maze):
        x = maze_start[0] + traveler_first_step[0]
        y = maze_start[1] + traveler_first_step[1]
        traveler_start_coord = (x, y)
        symbol = given_maze[traveler_start_coord[1]][traveler_start_coord[0]]
        if symbol == ".":
            return False
        # check up position start connects to start below it
        if traveler_first_step == (0, -1) and (symbol == "|" or symbol == "7" or symbol == "F"):
            return True
        # check down position start connects to start above it
        if traveler_first_step == (0, 1) and (symbol == "|" or symbol == "J" or symbol == "L"):
            return True
        # check right position start connects to start left of it
        if traveler_first_step == (1, 0) and (symbol == "-" or symbol == "J" or symbol == "7"):
            return True
        # check left position start connects to start right of it
        if traveler_first_step == (-1, 0) and (symbol == "-" or symbol == "L" or symbol == "F"):
            return True
        # all remaining cases are a bad start - not connected to maze_start
        print("Symbol was: " + symbol + " and first step was " + str(traveler_first_step))
        return False

    def __init__(self, start, first_step, maze, name):
        self.history = []
        self.history.append(start)
        #print(self.history)
        self.maze = maze
        x = start[0] + first_step[0]
        y = start[1] + first_step[1]
        self.currently_at = (x, y)
        self.traveler_name = name
        print("Spawned " + self.traveler_name + " at " + str(self.currently_at) + " on maze symbol " + self.maze[y][x])
        if maze[y][x] == ".":
            print("Dead end for " + self.traveler_name)
            self.found_dead_end = True
        else:
            self.found_dead_end = False

    def get_current_maze_symbol(self):
        return self.maze[self.currently_at[1]][self.currently_at[0]]

    def legend_lookup(self, coordinate):
        symbol = self.maze[coordinate[1]][coordinate[0]]
        return self.maze_legend[symbol]

    def find_next_step(self):
        if self.found_dead_end:
            return None
        previously_at = self.history[-1]
        #print(self.traveler_name + " looking forward from " + str(self.currently_at) + " previously at " + str(previously_at))
        options = self.legend_lookup(self.currently_at)
        if not options:
            print("This should not happen")
            print(self.traveler_name + " on a dead end at " + str(self.currently_at))
            return None
        for option in options:
            x = self.currently_at[0] + option[0]
            y = self.currently_at[1] + option[1]
            look = (x, y)
            if look == previously_at:
                #print("looked backward and did not select: " + str(look))
                continue
            else:
                #print("looked forward and did select: " + str(look))
                return look

    def move(self):
        if self.found_dead_end:
            return

        next_step = self.find_next_step()
        if next_step is None:
            print("This should not happen, already on a dead end but found_dead_end condition not set.")
            return
        else:
            self.history.append(self.currently_at)
            self.currently_at = next_step
            print(self.traveler_name + " just moved to " + str(self.currently_at) + " - " + self.get_current_maze_symbol())
            #print(self.history)
            if self.maze[self.currently_at[1]][self.currently_at[0]] == ".":
                print("which was a dead end.")
                self.found_dead_end = True

    def are_you_my_neighbor(self, fellow_traveler):
        #print(self.traveler_name + " at " + str(self.currently_at) + " and " + fellow_traveler.traveler_name + " at " + str(fellow_traveler.currently_at) + " checking if neighbors.")
        if self.found_dead_end or fellow_traveler.found_dead_end:
            return False
        if self.currently_at == fellow_traveler.currently_at:
            print(self.traveler_name + " and " + fellow_traveler.traveler_name + " on same location: " + str(self.currently_at))
            return True
        if self.find_next_step() == fellow_traveler.currently_at:
            print(self.traveler_name + " and " + fellow_traveler.traveler_name + " next to one another: " + str(self.currently_at) + str(fellow_traveler.currently_at))
            return True
        return False


with open(sys.argv[1], 'r', encoding="utf-8") as file:
    line_num = 0
    looking_for_start = True
    for line in file:
        maze.append(line.strip())
        if looking_for_start:
            match = start_re.search(line)
            if match:
                looking_for_start = False
                start_coord = (match.start() , line_num)
        line_num += 1

# adjacency (diagonals never adjacent in this maze)
first_step_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# edge detection
if start_coord[0] == 0:
    first_step_list.remove((-1, 0))
if start_coord[0] == len(maze[1]) - 1:
    first_step_list.remove((1, 0))
if start_coord[1] == 0:
    first_step_list.remove((0, -1))
if start_coord[1] == len(maze) - 1:
    first_step_list.remove((0, 1))
# spawn the travelers, up to four. What a friendly bunch.
i = 0
for first_step in first_step_list:
    if first_step == (0, 1):
        traveler_name = "down_start"
    elif first_step == (0, -1):
        traveler_name = "up_start"
    elif first_step == (1, 0):
        traveler_name = "right_start"
    elif first_step == (-1, 0):
        traveler_name = "left_start"
    else:
        traveler_name = "unexpected"
    if MazeTraveler.is_valid_start(start_coord, first_step, maze):
        travelers.append(MazeTraveler(start_coord, first_step, maze, traveler_name))
    else:
        print(traveler_name + " will not be in this maze.")
    i += 1

def any_current_neighbor():
    cmb_itr = itertools.combinations(travelers, 2)
    for comb in cmb_itr:
        if comb[0].are_you_my_neighbor(comb[1]):
            return True
    return False

while travelers and not any_current_neighbor():
    i = 0
    remaining_traveler_count = len(travelers)
    while i < remaining_traveler_count:
        if travelers[i].found_dead_end:
            print("Traveler at dead end, removing: " + travelers[i].traveler_name)
            travelers.pop(i)
            i += 1
            remaining_traveler_count -= 1
        else:
            travelers[i].move()
            i += 1

for traveler in travelers:
    print(traveler.traveler_name + " traveled " + str(len(traveler.history)))