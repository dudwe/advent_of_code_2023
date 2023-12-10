def parse_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
        seqs = []
        for line in lines:
            line = line.split()
            line = list(map(int, line))
            #print(line)
            seqs.append(line)
    return seqs

def get_history(seq):
    '''
    We can do this inplace giving us  O(1) memory
    

    
    0 3 6 9 12 15
    3 3 3 3 3  15
    0 0 0 0 3  15
    stop
            

    1 3 6 10 15 21
    2 3 4 5  6
    1 1 1 1
    0 0 0
    Stop 

    '''
    #print(seq)
    end = len(seq)-1
    allZero = False
    while not allZero:
        allZero = True
        for idx in range(0,end):
            seq[idx] = seq[idx+1] - seq[idx]
            if seq[idx] != 0:
                allZero = False
        #print(seq)
        end -=1
    #print(seq)
    return sum(seq)

def get_history_brute(seq):
    total = seq[-1]
    while not all(x==0 for x in seq):
        #print(seq)
        tmp = []
        for x in range(0,len(seq)-1):
            tmp.append(seq[x+1] - seq[x])
        total += tmp[-1]
        seq = tmp
    #print(seq)
    return total



def part_1(file):
    sequences = parse_input(file)
    sums = []
    for seq in sequences:
        history = get_history(seq)
        sums.append(history)
    return sum(sums)

print(part_1("small.txt"))
print(part_1("input.txt"))


def part_2(file):
    sequences = parse_input(file)
    sequences = [seq[::-1] for seq in sequences]
    #print(sequences)
    sums = []
    for seq in sequences:
        history = get_history(seq)
        sums.append(history)
    return sum(sums)
print(part_2("input.txt"))
print(part_2("small.txt"))