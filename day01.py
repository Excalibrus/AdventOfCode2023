file1 = open('inputs/day01.txt', 'r')
lines = file1.readlines()

# Part 1
sum = 0
for line in lines:
    firstChar = None
    lastChar = None
    for character in line:
        if character.isdigit():
            if firstChar is None:
                firstChar = character
                lastChar = character
            else:
                lastChar = character
        
    if firstChar is not None and lastChar is not None:
        sum += int(firstChar + lastChar)

print(sum)
    
# Part 2

sum = 0
stringNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines: 
    firstNum = None
    lastNum = None
    # print(line)
    for index in range(len(line)):
        character = line[index]
        if character.isdigit():
            if firstNum is None:
                firstNum = int(character)
                lastNum = int(character)
            else:
                lastNum = int(character)
        elif character.isalpha():
            # print(character)
            if index <= len(line) - 3:
                matchingItems = filter(lambda x: x[0] == character, stringNumbers)
                for item in matchingItems:
                    # print(item)
                    if index + len(item) <= len(line):
                        itemInLine = line[index:index+len(item)]
                        if(itemInLine == item):
                            # print("Found:" + itemInLine)
                            num = stringNumbers.index(itemInLine) + 1
                            if firstNum is None:
                                firstNum = num
                                lastNum = num
                            else:
                                lastNum = num

        
    if firstNum is not None and lastChar is not None:
        # print(firstNum)
        # print(lastNum)
        sum += int(str(firstNum) + str(lastNum))
        # print(sum)

print(sum)
