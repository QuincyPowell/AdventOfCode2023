import sys
import math

LEFT = "L"
RIGHT = "R"
desert_map = {}
starting_nodes = []
circuitous_destinations_by_starting_node = {}

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

def is_destination_node(node):
    return desert_map[node][2]

def arrived_destination(node_list):
    arrived = True
    for node in node_list:
        if not is_destination_node(node):
            arrived = False
            break
    return arrived

def find_circuitous_destination_paths(start_node):
    previous_node = start_node
    current_node = start_node
    nodes_traversed = 0
    circuit_dict = {}
    finding_circuit_paths = True
    while finding_circuit_paths:
        for step in desert_route:
            if is_destination_node(current_node):
                circuit_tuple = (previous_node, current_node, nodes_traversed)
                if circuit_tuple in circuit_dict:
                    if circuit_dict[circuit_tuple] >= 2:
                        # Would have added third so we can stop
                        finding_circuit_paths = False
                        break
                    else:
                        circuit_dict[circuit_tuple] += 1
                        previous_node = current_node
                        nodes_traversed = 0
                else:
                    circuit_dict[circuit_tuple] = 1
                    previous_node = current_node
                    nodes_traversed = 0
            if step == LEFT:
                current_node = desert_map[current_node][0]
            else:
                current_node = desert_map[current_node][1]
            nodes_traversed += 1
    return list(circuit_dict.keys())

steps_to_repeated_destination = []
for start in starting_nodes:
    circuitous_paths_list = find_circuitous_destination_paths(start)
    steps_to_repeated_destination.append(circuitous_paths_list[0][2])

#print(circuitous_paths_list)
# So, the input might have been messier but start -> destination and
# all subsequent destination -> destination are  always a self
# loop that is consistently the same number for any given start node.
# So this becomes a lowest common multiple math problem.
# Fortunately Python has a builtin LCM method in the default math library.

print("Found the following paths to destination nodes including repeating paths")
print(steps_to_repeated_destination)
print("The least common multiple among them is the smallest number of steps for the multiple travelers")
print(math.lcm(*steps_to_repeated_destination))
