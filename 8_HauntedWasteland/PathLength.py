import sys

START = "AAA"
DESTINATION = "ZZZ"
LEFT = "L"
RIGHT = "R"
desert_map = {}

with open(sys.argv[1], "r", encoding="utf-8") as file:
    desert_route = file.readline().strip()
    file.readline()
    for line in file:
        split1 = line.split(" = ")
        node = split1[0]
        (left, right) = split1[1].strip()[1:-1].split(", ")
        if node in desert_map:
            print("Duplicate note detected: " + node)
        else:
            desert_map[node] = (left, right)

# Navigate!
nodes_traversed = 0
route_loops = 0
current_node = START
while current_node != DESTINATION:
    for step in desert_route:
        #print(current_node + " go " + step)
        nodes_traversed += 1
        if step == LEFT:
            current_node = desert_map[current_node][0]
        else:
            current_node = desert_map[current_node][1]
    route_loops += 1
    print("Went through the whole route " + str(route_loops) + " times.")

print("Arrived at ZZZ in " + str(nodes_traversed) + " node traversals.")