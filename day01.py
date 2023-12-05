file1 = open('inputs/day01.txt', 'r')
lines = file1.readlines()
 
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
    