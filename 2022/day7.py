import json
text = open("./values/2022-7", "r").read()
# text = open("./values/2022-7", "r").readtext()
text = text.split("\n")
# text = [x.split(" ") for x in text]

# current path
path = []

# full directory tree
tree = {}
# current node
# program starts at / so node is tree
node = tree

for line in text:
    # split the lines into tokens
    tokens = line.split(" ")

    # hardcoded solutions
    # if the line is "$ cd /" then we need to go to the root directory
    # set path to empty as we are at /
    # set the node to tree like the start of the program
    if line == "$ cd /":
        path = []
        node = tree
        continue

    # if the line is "$ cd .." go back a directory
    # pop an item from the path array
    # starting from the base of the tree
    # for every folder in the path
    # go through the tree and set it to node

    elif line == "$ cd ..":
        path.pop()
        node = tree
        for name in path:
            node = node[name]
        continue

    # useless commands
    if tokens[1] in ["ls"]:
        continue

    # all if statements above should move on to the next loop

    # if the command is dir
    elif tokens[0] == "dir":
        # get the name
        name = tokens[1]
        # add that name to the node as a new hashset
        node[name] = {}

    # if its cd
    # add the name to path
    # set node to the new node
    elif tokens[1] == "cd":
        name = tokens[2]
        path.append(name)
        node = node[name]

    # add the filesize as a dict
    else:
        node[tokens[1]] = int(tokens[0])

# a variable
total = 0

# print(json.dumps(tree, indent=4))


def fullsize(node):
    s = 0
    for v in node.values():
        if isinstance(v, int):
            s += v
        else:
            s += fullsize(v)
    return s


size = fullsize(tree)

print(size)
