

def part_1():
    with open('input.txt') as f:
        total = 0
        for line in f:
            print(line)
            l = 0
            r = len(line) - 1
            while  l < len(line):
                if line[l].isdigit():
                    break
                l+=1
            while r >=0:
                if line[r].isdigit():
                    break
                r-=1

            num = int(line[l]+line[r])
            total += num

    print(total)

def part_2():
    map_to_number = {"one":1,"two":2,"three":3,"four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

    digits = {"o":["one"], "t":["two","three"],"f":["four", "five"],"s":["six","seven"],"e":["eight"],"n":["nine"]}
    with open('input.txt') as f:
        total = 0
        
        for line in f:
            #First do a digit search, replace all digits in the string with the actual number
            l = 0
            digit_string = ""
            while l < len(line):
                char = line[l]
                if char in digits:
                    #Grow the letter
                    found = None
                    for number in digits[char]:
                        #print(f'Check {line[l:l+len(number)]} == {number}',l+len(number) <= len(line))
                        if l+len(number) <= len(line) and line[l:l+len(number)] == number:
                            #print("Found a digit",number)
                            found = number
                            digit_string += str(map_to_number[found])
                    l+=1

                else: 
                    if line[l].isdigit():
                        digit_string+=line[l]
                    #Drop the letter
                    l+=1
            print(f'{line} -> {digit_string} Result: {int(digit_string[0] + digit_string[-1])}')
            total += int(digit_string[0] + digit_string[-1])


    print(f'Total:{total}')

#part_1()
part_2()