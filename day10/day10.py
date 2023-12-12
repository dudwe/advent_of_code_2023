def parse_input(file):
    """Return 2d array of our file"""
    with open(file) as f:
        lines = f.read().splitlines()
        graph = [list(line) for line in lines]
        #print(graph)
        return graph
pipe_dict = {"|":[(1,0),(-1,0)],"-":[(0,-1),(0,1)], "L":[(-1,0),(0,1)], "J":[(-1,0),(0,-1)], "7":[(1,0),(0,-1)],"F":[(1,0),(0,1)], "S": [(0,1),(1,0),(-1,0),(0,-1)]}

def find_start(start,graph) :
    """Find the starting symbol for a S """
    print(f"{start=}")
    M,N = len(graph),len(graph[0])
    for d in pipe_dict:
        valid = True
        for dir in pipe_dict[d]:
            d_y = start[0] + dir[0]
            d_x = start[1]+dir[1] 
            if  0 <= d_y < M  and 0 <= d_x < N:
                if graph[d_y][d_x]  == '.':
                    valid = False
        if valid:
            #Check that the symbol is valid on case by case basis


            if d == "-":
                #Look at prev and after, make sure both are valid 
                if graph[start[0]][start[1]-1] in ["F","-","L"] and graph[start[0]][start[1]+1] in ["-","7","J"]:
                    print(f"VALID {d=}")
                    return d
            if d == "7":
                if graph[start[0] + 1 ][start[1]] in ["|","J","L"] and graph[start[0]][start[1]-1] in ["F","-","L"]:
                    print(f"VALID {d=}")
                    return d
            if d == "F":
                if graph[start[0] + 1 ][start[1]] in ["|","J","L"] and graph[start[0]][start[1]+1] in ["-","7","J"]:
                    print(f"VALID {d=}")
                    return d


def part_1(file):
    '''
    We need to translate the input into a graph data structure
    We then need to BFS from the start -> continue until all nodes are visited
    We use directions to choose which nodes we can go to
    BFS and store distances in a 2d copy
    '''
    graph = parse_input(file)
    distances = [[-1 for x in g] for g in graph]
    #print(distances)

    #Find the start node
    start = None
    for idx_y,row in enumerate(graph):
        for idx_x, val in enumerate(row):
            if val == "S":
                start = (idx_y,idx_x)
                break
    print(f"{start=}")

    #We need to find the type of pipe S is
    # S need to be able to complete the loop
    # So we could try and run a dfs using each possible node

    valid = find_start(start,graph)
    graph[start[0]][start[1]] = valid

    queue = [start]
    distances[start[0]][start[1]] = 0


    M,N = len(graph),len(graph[0])
    while(queue):
        node = queue.pop(0)
        #print(f"Walk {node}")
        val = graph[node[0]][node[1]]
        if val in pipe_dict:
            directions = pipe_dict[val]

            for dir in directions:
                d_y = node[0] + dir[0]
                d_x = node[1]+dir[1]
                if  0 <= d_y < M  and 0 <= d_x < N:
                    if graph[d_y][d_x] != '.' and distances[d_y][d_x] == -1:
                        distances[d_y][d_x] = distances[node[0]][node[1]] + 1
                        queue.append((d_y,d_x))
    #print(max(max(distances)))
    #for g in graph:
    #    print(g)

    print()
    max_d = -1
    for d in distances:
        max_d = max(max_d,max(d))
    
    return max_d



#print(part_1("small.txt"))
#print(part_1("small2.txt"))
print(part_1("input.txt"))