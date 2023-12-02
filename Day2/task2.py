def calculatePowerOfGameSet(colorDict: dict):
    result = 1
    for num in colorDict.values():
        result *= num
    return result

def leastNumberOfColors(round, colorDict):
    colorsInfo = round.split(", ")
    for colorInfo in colorsInfo:
        info = colorInfo.split()
        count = int(info[0])
        color = info[1]
        if count > colorDict[color]:
            colorDict[color] = count
    return colorDict

def getGameSetPower(line: str) -> int:
    gameNumber = int((line.split(' ')[1])[:-1])
    roundsInfo = ' '.join(line.split(' ')[2::]).rstrip()
    rounds = roundsInfo.split("; ")
    colorDict = {"red": 0, "green": 0, "blue": 0}
    for round in rounds:
        colorDict = leastNumberOfColors(round, colorDict)
    print(f"minimum colors used in game {gameNumber}: ", colorDict)
    return calculatePowerOfGameSet(colorDict)

gameSetPowers = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        gameSetPowers.append(getGameSetPower(line))
print(sum(gameSetPowers))
