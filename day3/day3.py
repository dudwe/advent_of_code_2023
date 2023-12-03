



def isPart(y,x,p,grid):

    isSymbol = lambda c : not c.isdigit()  and c != '.'
    dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
    for i in range(x,p):
        #Check up down left right
        for d in dirs:
            coord_y,coord_x = y + d[0], i + d[1]

            if  0<=coord_y<len(grid) and 0<=coord_x<len(grid[0]):
                if isSymbol(grid[coord_y][coord_x]):
                    return True
    
    return False


def part_1():
    '''
    We need to check that a number is adjacent to a symbol
    We need to think of the input as a 2d grid

    Idea:
    Write the input file to a 2d grid
    x = 0


    
    for y in range(len(grid)):
        x = 0
        while x <len(grid[0]):
            if grid[y][x].isDigit():
                Compute the digit
                update x to = x + len(number)
                check if any part of the number is adjancent to a symbol
                    if so than update total
    
    '''


    with open('input.txt') as f:
        grid = [[c for c in line.strip()] for line in f]
        total = 0
        for y in range(len(grid)):
            x = 0
            while x < len(grid[0]):
                if grid[y][x].isdigit():
                    p = x
                    while p<len(grid[0]) and grid[y][p].isdigit():
                        p+=1
                    
                    if isPart(y,x,p,grid):
                        print(f'Part Number:{grid[y][x:p]}')
                        total+=int(''.join(grid[y][x:p]))
                    else:
                        print(f'Not Part :{grid[y][x:p]}')
                    x = p
                else:
                    x+=1
        print(f'Total:{total}')


def getNumbers(c_y,c_x,grid):
    l = c_x
    r = c_x


    while l-1 >= 0 and grid[c_y][l-1].isdigit():
        l-=1

    while r < len(grid[0]) and grid[c_y][r].isdigit():
        r+=1
    
    return grid[c_y][l:r]


def findAdjNumbers(c_y,c_x,grid):
    numbers = []
    #Left and Right are safe to check
    dirs = [[0,1],[0,-1]]

    for d in dirs:
        coord_y,coord_x = c_y + d[0],c_x + d[1]
        if 0<=coord_x <len(grid[0]) and grid[coord_y][coord_x].isdigit():
            number = getNumbers(coord_y,coord_x,grid)
            numbers.append(int(''.join(number)))

        
    '''
    Need to avodi double counting digits above and down:

    12134
    ..*..

    12.34
    ..*..

    We can resovle by checking both types of cases

    '''

    #Handle Up 
    if 0 <=c_y-1<len(grid) and grid[c_y-1][c_x].isdigit():
        #All filed above
        number = getNumbers(c_y-1,c_x,grid)
        numbers.append(int(''.join(number)))
    else:
        #Try diags
        diags = [[-1,-1],[-1,1]]
        for d in diags:
            coord_y,coord_x = c_y + d[0] , c_x + d[1]
            if  0<=coord_y<len(grid) and 0<=coord_x<len(grid[0]) and grid[coord_y][coord_x].isdigit():
                number = getNumbers(coord_y,coord_x,grid)
                numbers.append(int(''.join(number)))



    #Handle Down
    if 0 <=c_y+1<len(grid) and grid[c_y+1][c_x].isdigit():
        #All filed above
        number = getNumbers(c_y+1,c_x,grid)
        numbers.append(int(''.join(number)))
    else:
        #Try diags
        diags = [[1,-1],[1,1]]
        for d in diags:
            coord_y,coord_x = c_y + d[0] , c_x + d[1]
            if  0<=coord_y<len(grid) and 0<=coord_x<len(grid[0]) and grid[coord_y][coord_x].isdigit():
                number = getNumbers(coord_y,coord_x,grid)
                numbers.append(int(''.join(number)))

    return None if len(numbers)!=2 else numbers


def part_2():
    '''
    We need to find numbers adjacent to gears
    A adjgear has exactly 2 nearby numbers

    Idea:
    Loop through the grid
    At each gear, find adjancent numbers
    Checkeach direction
        If we have a digits, find the number using two pointers
        If we have  2 found digits then compute and add to total
    '''
    with open('input.txt') as f:
        grid = [[c for c in line.strip()] for line in f]
        total = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "*":
                    #print("Find adjacent numbers")
                    numbers = findAdjNumbers(y,x,grid)
                    if numbers:
                        print(f'Valid gear {numbers}')
                        total += numbers[0] *numbers[1]
        print(f'Total {total}')
part_2()