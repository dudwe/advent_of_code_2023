from collections import Counter,defaultdict

def parse_line(line):
    
    line = line.split(": ")
    card_no,card = line[0],line[1]
    card_no = int(card_no.split()[-1])
    card = card.split(" | ")
    winning,guesses = card[0],card[1]
    winning = Counter(winning.split())
    guesses = guesses.split()
    print(winning,guesses)
    return card_no, winning, guesses

def compute_score(winning,guesses):
    matches = -1
    for guess in guesses:
        if winning[guess]>0:
            matches+=1
            winning[guess]-=1


    return 0 if matches == -1 else 2 ** matches



def compute_matches(winning,guesses):
    matches = 0
    for guess in guesses:
        if winning[guess]>0:
            matches+=1
            winning[guess]-=1


    return  matches

def part_1():
    '''
    Parse the row and write the winning numbers to a Counter
    Then iterate over the guesses and compute the score
    Return the result
    '''
    total = 0
    with open('input.txt') as f:
        for line in f:
            _,winning, guesses = parse_line(line.strip())
            print(f"{winning=} {guesses=}")
            score = compute_score(winning,guesses)
            print(f"{score=}")
            total +=score
    return total
#print(part_1())


def part_2():
    '''
    Same parsing as before
    In this case we need to track the number of copies we have as we process the data -> we can use a dictionary for this
    So:
    for guess in f:
        Add guess to dict
        compute number of matches for current
        Increment all subsequent n guess by d[g]
    return the sum for d.values()

    '''
    with open('input.txt') as f:
        x = len(f.readlines())
        cards = {i+1:1 for i in range(x)}
        #print(f"{cards=}")

    with open('input.txt') as f:
        for line in f:
            guess_no,winning, guesses = parse_line(line.strip())
            #print(f"{guess_no=} {winning=} {guesses=}")
            score = compute_matches(winning,guesses)
            for x in range(guess_no+1,guess_no+1+score):
                cards[x]+= cards[guess_no]

            #print(f"{cards=}")
    return sum(cards.values())
print(part_2())