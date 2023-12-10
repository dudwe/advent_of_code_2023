
from collections import defaultdict

class Node():
    def __init__(self,name,left,right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.name=} {self.left=} {self.right=}"


def parse_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
        steps = lines[0].split()[0]
        graph = defaultdict(Node)
        for line in lines[2:]:
            
            line = line.split("=")
            name = line[0].strip()
            tup = line[1].strip()
            tup = tup.replace("(", "") 
            tup = tup.replace(")", "") 
            tup = tup.replace(" ", "") 
            tup = tup.split(",")
            graph[name] = Node(name,tup[0],tup[1])

        return steps, graph



def traverse(steps,graph):
    total = 0
    cur = "AAA"
    s_ptr = 0
    while cur != "ZZZ":
        if s_ptr == len(steps):
            s_ptr=0
        if steps[s_ptr] == "L":
            cur = graph[cur].left
        else:
            cur = graph[cur].right
        s_ptr+=1
        total+=1


    return total

def part_1():
    '''
    Parse the input, we get
    Steps, Graph
    Then do a traversal until we reach the end 
    '''
    steps,graph  = parse_input("small.txt")
    print(traverse(steps,graph))
    steps,graph  = parse_input("small2.txt")
    print(traverse(steps,graph))
    steps,graph  = parse_input("input.txt")
    print(traverse(steps,graph))

#part_1()


def ghost_walk(steps,graph):
    '''
    for ghost walk we do the same as before but with a queue 
    We add to queue if the curent node does not end in Z
    We stop once all nodes end in Z

    This method will be too slow we need a faster approach
    '''
    queue = []
    for key in graph:
        if key[-1] == "A":
            queue.append(key)

    print(f"init with {queue=}")
    total = -1
    s_ptr = 0

    stop = False
    while not stop:
        if s_ptr == len(steps):
            s_ptr=0        


        nodes = queue[:]
        queue = []
        stop = True
        for node in nodes:
            if node[-1] != "Z":
                stop = False
            if steps[s_ptr] == "L":
                queue.append(graph[node].left)
            else:
                queue.append(graph[node].right)
        print(queue)
        s_ptr+=1
        total+=1


    return total

def get_paths(steps,graph):
    '''
    We can figure out at what point we hit an endpoint for each starting node

    From here use the values to find the lcm
    '''
    queue = []
    for key in graph:
        if key[-1] == "A":
            queue.append(key)
    print(queue)
    multiples = []

    while queue:
        node = queue.pop()
        s_ptr = 0
        dist = 0 
        while node[-1] != "Z":
            if s_ptr == len(steps):
                s_ptr = 0
            if steps[s_ptr] == "L":
                node = graph[node].left
            else:
                node = graph[node].right
            dist += 1
            s_ptr+=1
        multiples.append(dist)
    print(multiples)
    return multiples
    
def get_gcd(a,b):
    while b != 0:
        t = b
        b = a % b 
        a = t
    return a


def get_lcm(walks):
    print(walks)
    #Compute the lcm of the array of numbers 
    a = walks.pop(0)
    while walks:
        b = walks.pop(0)
        gcd = get_gcd(a,b)
        a = int((a*b) / gcd)
    return a

def part_2():
    steps,graph  = parse_input("small3.txt")
    walks = get_paths(steps,graph)
    print(get_lcm(walks))
    steps,graph  = parse_input("input.txt")
    walks = get_paths(steps,graph)
    print(get_lcm(walks))

part_2()