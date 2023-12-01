matchingStrings = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# def getNumFromLineStart(line: str) -> str:
#     for index, char in enumerate(line):
#         if char.isdigit():
#             return char
#         # if no digit matched, try to match substring until the current character
#         for numInStringRepresentation in matchingStrings.keys():
#             if numInStringRepresentation in line[0:index+1]:
#                 return matchingStrings[numInStringRepresentation]

def getNumFromLine(line: str, reverse: bool=False) -> str:
    if reverse:
        line = line[::-1]
    for index, char in enumerate(line):
        if char.isdigit():
            return char
        # if no digit matched, try to match substring until the current character

        for numInStringRepresentation in matchingStrings.keys():
            # in case of finding from the end
            if reverse and numInStringRepresentation[::-1] in line[0:index+1]:
                return str(matchingStrings[numInStringRepresentation])
            # finding from the start
            if numInStringRepresentation in line[0:index+1]:
                return str(matchingStrings[numInStringRepresentation])



numList = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        firstNum = getNumFromLine(line)
        lastNum = getNumFromLine(line, True)
        numList.append(int(firstNum+lastNum))


print(sum(numList))
