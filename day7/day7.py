from collections import Counter,defaultdict


hand_types = {1:"High Card",2:"One Pair",3:"Two Pair",4:"Three of a Kind",5:"Full house",6:"Four of a Kind",7:"Five of a kind"}


class Hand():
    """
    Represents a hand

    
        """
    def __init__(self,hand,bid):
        self.hand = hand
        self.internal_hand = self.parse_hand(hand)
        self.bid = bid
        self.type = find_type(Counter(self.internal_hand))
    
    def parse_hand(self,hand):
        d = {'T':10,'J':11,'Q':12,'K':13,'A':14}
        hand = list(hand)
        for idx,val in enumerate(hand):
            if val in d:
                hand[idx]= d[val]
            else:
                hand[idx] = int(val)
        return hand

    def __str__(self):
        res = f"""{self.hand=}\t{self.internal_hand=}\t{self.bid=}\t{self.type=}\t{hand_types[self.type]}"""
        return res

def find_type(hand_d):
    #print(hand_d)
    if len(hand_d) == 1:
        #print("Five of a kind")
        return 7
    if len(hand_d) == 2:
        vals = hand_d.values()
        if 4 in vals:
            #print("Four of a Kind")
            return 6
        else:
            #print( "Full house")
            return 5
    if len(hand_d) == 3:
        vals = hand_d.values()
        if 3 in vals:
            #print("Three of a Kind")
            return 4
        #print( "Two Pair")
        return 3
    if len(hand_d) == 4:
        #print( "One Pair")
        return 2
    #print("High Card")
    return 1



def parse_inpute(file):
    with open(file) as f:
        lines = f.read().splitlines()
        hands  = []
        for line in lines:
            line = line.split()
            hand,bid = line[0],int(line[1])
            hands.append(Hand(hand,bid))
            #print(hands[-1])
        #print(hands)
        hands.sort(key= lambda x: (x.type,x.internal_hand))

        #Calculate the bids
        total_winnings = 0
        for idx,hand in enumerate(hands):
            total_winnings += (idx+1)  * hand.bid
        print(f"{total_winnings=}")
def part_1():
    parse_inpute("small.txt")
    parse_inpute("input.txt")
'''
print(find_type("AAAAA"))
print(find_type("AA8AA"))
print(find_type("23332"))
print(find_type("TTT98"))
print(find_type("23432"))
print(find_type("A23A4"))
print(find_type("23456"))
'''



part_1()





class JokerHand():
    """
    Represents a hand

    
        """
    def __init__(self,hand,bid):
        self.hand = hand
        self.internal_hand = self.parse_hand(hand)
        self.bid = bid
        self.type = find_joker_type(self.hand)
    
    def parse_hand(self,hand):
        d = {'T':10,'J':1,'Q':12,'K':13,'A':14}
        hand = list(hand)
        for idx,val in enumerate(hand):
            if val in d:
                hand[idx]= d[val]
            else:
                hand[idx] = int(val)
        return hand

    def __str__(self):
        res = f"""{self.hand=}\t{self.internal_hand=}\t{self.bid=}\t{self.type=}\t{hand_types[self.type]}"""
        return res

def  find_joker_type(hand):
    hand = list(hand)
    if 'J' not in hand:
        return find_type(Counter(hand))
    
    hand_dict = defaultdict(int)
    jcount = 0
    for card in hand:
        if card == 'J':
            jcount+=1
        else:
            hand_dict[card]+=1
    #print(hand_dict,jcount)
    #Find the max card, increment this by d
    max_card = None
    max_count = 0
    for k,v in hand_dict.items():
        if v>max_count:
            max_count = v
            max_card = k
    hand_dict[max_card]+=jcount
    #print("Jokered:",hand_dict)
    return find_type(hand_dict)


def parse_input2(file):
    #Approach is same as before, but this time we need to handle the joker differently in both case
    #So for internal we store a joker as 2 
    #And for finding the type, we use a similar method to before which is modified to replace joker with whatever gives us the best result
    with open(file) as f:
        lines = f.read().splitlines()
        hands  = []
        for line in lines:
            line = line.split()
            hand,bid = line[0],int(line[1])
            hands.append(JokerHand(hand,bid))
            
        #print(hands)
        hands.sort(key= lambda x: (x.type,x.internal_hand))

        #Calculate the bids
        total_winnings = 0
        for idx,hand in enumerate(hands):
            #print(hand)
            total_winnings += (idx+1)  * hand.bid
        print(f"{total_winnings=}")

def part_2():
    parse_input2("small.txt")
    parse_input2("input.txt")
#print(find_joker_type("QJJQ2"),hand_types[find_joker_type("QJJQ2")])
part_2()