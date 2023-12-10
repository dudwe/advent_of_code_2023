
import math
from functools import reduce

def parse_file(file):
    with open(file) as f:
        lines = f.read().splitlines()
        print(lines)
        times = lines[0]
        times = times.split()[1:]
        times = [int(x) for x in times]
        distances = lines[1]
        distances = distances.split()[1:]
        distances = [int(x) for x in distances]

        return times, distances




def count_sols(total_time,max_distance):
    #time = dist/speed
    #speed = dits/time
    '''
    Only ned to find the minimum viable speed and then compute the range from 
    '''
    #for x in range(total_time+1):
    #    print(x,compute_game_distance(total_time,x))


    min_speed = 0
    while compute_game_distance(total_time,min_speed) <= max_distance:
        min_speed +=1

    #print(minimum_held)
    max_speed = total_time
    while compute_game_distance(total_time,max_speed) <= max_distance:
        max_speed -=1

    print(f"{min_speed=},{max_speed=}")



    return max_speed - min_speed+1


def part_1():
    times, distances = parse_file("input.txt")
    print(f"{times=},{distances=}")
    
    res = []
    for idx,tup in enumerate(zip(times,distances)):
        print(f"{idx}:{tup}")
        res.append(count_sols(tup[0],tup[1]))
    print(res)
    res =  reduce(lambda x,y : x * y ,res)
    return res


def parse_file2(file):
    with open(file) as f:
        lines = f.read().splitlines()
        print(lines)
        times = lines[0]
        times = times.split()[1:]
        t = int(''.join(times))
        distances = lines[1]
        distances = distances.split()[1:]
        d = int(''.join(distances))

        return t, d


def find_sol_left(time,distance):
    '''
    We want to find the left pointer such that


    left-1 invalid left is valid left+1 valid
    '''

    l = 0 
    r = time - 1 
    while l <= r :
        m = int(math.floor((l+r)/2))
        m_d = compute_game_distance(time,m)
        #print(l,r,":",m,m_d)
        if m_d > distance:
            #We beat the record
            #Check if d-1 fails
            t_l = m-1
            t_l_d = compute_game_distance(time,t_l)
            if t_l_d <= distance:
                return m
            r = m-1
        else:
            l = m+1
        #print(l,r,":",m,m_d)
        
def find_sol_right(time,distance):
    '''
    We want to find the right pointer such that


    right-1 valid right is valid right+1 invalid
    '''
    l = 0
    r = time
    while l<=r:
        m = int((l+r)/2)
        m_d = compute_game_distance(time,m)
        if m_d > distance:
            if compute_game_distance(time,m+1) <= distance:
                return m
            l = m + 1
        else:
            r = m -1 
    return -42    


def compute_game_distance(total_time,speed):
    return speed  * (total_time - speed )






def part_2():
    '''
    Our numbers are now very big :/
    Best thing we can do is a binary search on left and right to get the result
    This means we go from linear to a logarithmic operation
    We need to beat the record -> so the distance needs to be greater
    '''
    time, distance = parse_file2("input.txt")
    print(time,distance)
    l = (find_sol_left(time,distance))
    print(time,distance)
    r = (find_sol_right(time,distance))

    return r-l+1

print(part_2()) 

#71530 940200   Result 71503
#34454850