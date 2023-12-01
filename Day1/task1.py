def getNumFromLine(line: str, reverse: bool=False) -> str:
    if reverse:
        line = line[::-1]
    for char in line:
        if char.isdigit():
            return char

numList = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        firstNum = getNumFromLine(line)
        lastNum = getNumFromLine(line, True)
        numList.append(int(firstNum+lastNum))


print(sum(numList))
