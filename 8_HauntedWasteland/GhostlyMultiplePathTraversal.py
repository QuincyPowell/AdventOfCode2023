import sys

LEFT = "L"
RIGHT = "R"
desert_map = {}
starting_nodes = []

with open(sys.argv[1], "r", encoding="utf-8") as file:
    desert_route = file.readline().strip()
    file.readline()
    for line in file:
        split1 = line.split(" = ")
        node = split1[0]
        is_a_node = (node[2] == "A")
        is_z_node = (node[2] == "Z")
        (left, right) = split1[1].strip()[1:-1].split(", ")
        if node in desert_map:
            print("Duplicate note detected: " + node)
        else:
            desert_map[node] = (left, right, is_z_node)
        if is_a_node:
            starting_nodes.append(node)

def arrived_destination(node_list):
    arrived = True
    for node in node_list:
        if not desert_map[node][2]:
            arrived = False
            break
    return arrived

def go_left():
    cursor = 0
    end = len(starting_nodes)
    while cursor < end:
        starting_nodes[cursor] = desert_map[starting_nodes[cursor]][0]
        cursor += 1

def go_right():
    cursor = 0
    end = len(starting_nodes)
    while cursor < end:
        starting_nodes[cursor] = desert_map[starting_nodes[cursor]][1]
        cursor += 1

# Navigate!
print(starting_nodes)
nodes_traversed = 0
route_loops = 0
while not arrived_destination(starting_nodes):
    for step in desert_route:
        nodes_traversed += 1
        if step == LEFT:
            go_left()
        else:
            go_right()
    route_loops += 1
    if route_loops % 1000 == 0:
        print("Traversed instructions this many times: " + str(route_loops))

print("Arrived at only z-nodes in " + str(nodes_traversed) + " node traversals.")