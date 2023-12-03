from collections import defaultdict

def parse_line(line):
    game = line.split(":")
    game_no = int(game[0].split(" ")[1])
    turns = game[-1].split(";")

    grabs = []
    for turn in turns:
        cubes = turn.split(",")
        grab = defaultdict(int)
        for cube in cubes:
            cube = cube.strip().split(" ")
            #print(cube)
            grab[cube[-1]] = int(cube[0])
        grabs.append(grab)

    return game_no,grabs

def validate_game(turns):
    for turn in turns:
        if turn["red"]>12 or turn["green"]>13 or turn["blue"]>14:
            return False
    return True
 
def part_1():
    with open('input.txt') as f:
        total = 0
        for line in f:
            #We need to parse the line
            game_no,turns = parse_line(line)
            if validate_game(turns):
                total +=game_no
            #print(game_no,turns)
    print(total)

def minimum_needed(turns):
    max_r = 0
    max_g = 0
    max_b = 0

    for turn in turns:
        max_r = max(max_r,turn["red"])
        max_g = max(max_g,turn["green"])
        max_b = max(max_b,turn["blue"])

    return max_r * max_g * max_b

def part_2():
    with open('input.txt') as f:
        total = 0
        for line in f:
            #We need to parse the line
            _,turns = parse_line(line)
            total +=minimum_needed(turns)
    print(total)    
part_1()
part_2()