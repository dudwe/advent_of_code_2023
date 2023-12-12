from collections import defaultdict
def parse_input(file):
    """Return 2d array of our file"""
    with open(file) as f:
        lines = f.read().splitlines()
        graph = [list(line) for line in lines]
        #print(graph)
        return graph

def expand(graph,delta=1):
    #Expand by row
    expansion_row = []

    for idx,row in enumerate(graph):
        if all(x == '.' for x in row):
            #print("Expand row")
            for p in range(delta-1):
                expansion_row.append(row)
        expansion_row.append(row)
    
    
    #Expand by column
    expansion_col = [[] for x in expansion_row]

    for y in  range(len(expansion_row[0])):

        expand = True
        for x in range(len(expansion_row)):
            if expansion_row[x][y] != '.':
                expand= False
            expansion_col[x].append(expansion_row[x][y])
        if expand:
            #print("Expand Col")
            for p in range(delta-1):
                for x in range(len(expansion_row)):
                    expansion_col[x].append(expansion_row[x][y])        


    return expansion_col


def part_1(f,delta=1):
    #First get the universe
    graph = parse_input(f)
    #for g in graph:
    #    print (g)
    #Expand the universe
    exp_graph = expand(graph,delta)
    #for g in exp_graph:
    #    print (g)

    '''
    #Count all distances and sum 
          
    '''

    coords = []

    for x, pair_item in enumerate(exp_graph):
        for y, item in enumerate(pair_item):
            if item == '#':
                coords.append((x,y))

    #print(coords)
    total = 0
    for coord in coords:
        for c in coords:
            if c != coord:
                dist = abs(coord[0] - c[0]) + abs(coord[1]-c[1])
                #print(f"{coord}, {c}, {dist=}")
                total+=dist

    return int(total/2)

    



def expand_coords(graph,coords,delta=10):
    #Row expansion 
    row_delta = 0
    for idx,row in enumerate(graph):
        if all(x == '.' for x in row):
            #print(f"Expand row {idx+row_delta}  ")
            for coord in coords:
                if coord[0] >idx + row_delta:
                    coord[0] +=  delta -1
            row_delta = row_delta + delta -1 
    #print(coords)

    col_delta = 0
    for y in  range(len(graph[0])):

        expand = True
        for x in range(len(graph)):
            if graph[x][y] != '.':
                expand= False
        if expand:
            #print(f"Expand Col {y}  {col_delta=}")
            for coord in coords:
                if coord[1] >y + col_delta:
                    coord[1] +=  delta -1
            col_delta = col_delta + delta -1 

    '''
    orig: [[0, 3], [1, 7], [2, 0], [4, 6], [5, 1], [6, 9], [8, 7], [9, 0], [9, 4]]
    #target [(0, 12), (1, 25), (2, 0), (13, 24), (14, 1), (15, 36), (26, 25), (27, 0), (27, 13)]


            [[0, 12], [1, 25], [2, 0], [13, 24], [14, 1], [15, 36], [26, 25], [27, 0], [27, 13]]
    '''
    #print(coords)

    return coords

def part_2(f,delta=1):
    #First get the universe
    graph = parse_input(f)
    #for g in graph:
    #    print (g)    

    '''
    Rather than generating the graph, we want to find the coords after we have done the expansion 
    Store the coords in a list

    Expansion by Row:
    We add 1 million to all coord_y that are AFTER the expanded Row

    Exapnsion by Column:
    We add 1 million to all coord_x that are AFTER the expanded column
    '''

    coords = [] 

    for x, pair_item in enumerate(graph):
        for y, item in enumerate(pair_item):
            if item == '#':
                coords.append([x,y])
    #print(coords)

    coords = expand_coords(graph,coords,delta)


    #print(coords)
    total = 0
    for coord in coords:
        for c in coords:
            if c != coord:
                dist = abs(coord[0] - c[0]) + abs(coord[1]-c[1])
                #print(f"{coord}, {c}, {dist=}")
                total+=dist
    #print(total/2)
    return int(total/2)


print(part_1("small.txt"))
print(part_1("input.txt"))
print(part_1("small.txt",100))
print(part_2("small.txt",100))
print(part_2("input.txt",1000000))