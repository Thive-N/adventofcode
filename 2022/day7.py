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
    if tokens[1] == "ls" or tokens[0] == "dir":
        continue

    # all if statements above should move on to the next loop

    # if its cd
    # add the name to path
    # set node to the new node
    elif tokens[1] == "cd":
        name = tokens[2]
        node[name] = {}
        path.append(name)
        node = node[name]

    # add the filesize as a dict
    else:
        node[tokens[1]] = int(tokens[0])


def traverse(node):
    su = 0
    s = 0
    for val in node.values():
        if isinstance(val, int):
            s += val
            su += val
        else:
            su += traverse(val)

    if s <= 100000:
        global lt100k
        lt100k += s
    return s


def traversee(node):
    s = 0
    for val in node.values():
        if isinstance(val, int):
            s += val
        else:
            traverse(val)
    return s


def traverse2(node):
    s = 0
    for val in node.values():
        if isinstance(val, int):
            s += val
        else:
            s += traverse(val)

    if s >= free:
        global smallest
        smallest = min(smallest, s)
    return s


print(json.dumps(tree, indent=4))
lt100k = 0
smallest = 99999999999999999
free = traversee(tree)-40000000
traverse(tree)
traverse2(tree)
print(lt100k)
print(smallest)
