result = [chr(97)] * 1000000
oneLetterCount = [0] * 26
twoLettersCount = [[0] * 26] * 26
threeLettersCount = [[[0] * 26] * 26] * 26

#first and second symbol insert
i = 2
letter = 2
result[0] = 'a'
result[1] = 'b'
oneLetterCount[0] = 1
oneLetterCount[1] = 1
twoLettersCount[0][1] = 1
while i < 1000000:
    prevLetter = ord(result[i-1])-97
    prevPrevLetter = ord(result[i-2])-97
    #check one letter count, two letters combination count, three letters combination count
    if oneLetterCount[letter] < 40000 and twoLettersCount[prevLetter][letter] < 2000 and threeLettersCount[prevPrevLetter][prevLetter][letter] < 100:
        result[i] = chr(letter+97)
        i += 1
    #change current letter
    if letter < 25:
        letter += 1
    else:
        letter = 0

strResult = ''.join(result)
print(strResult)