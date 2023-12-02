colorLimit = {"green": 13, "red": 12, "blue": 14}

def isValidRound(round: str) -> bool:
    colorsInfo = round.split(", ")
    for colorInfo in colorsInfo:
        info = colorInfo.split()
        count = int(info[0])
        color = info[1]
        if count > colorLimit[color]:
            return False
    return True

def isGameValid(line: str) -> bool:
    gameNumber = int((line.split(' ')[1])[:-1])
    roundsInfo = ' '.join(line.split(' ')[2::]).rstrip()
    rounds = roundsInfo.split("; ")
    for roundNumber, round in enumerate(rounds, start=1):
        if not isValidRound(round):
            print(f"invalid round #{roundNumber} in Game #{gameNumber}")
            return False
    return True

validGameIds = []
with open("input.txt", "r") as f:
    for gameNumber, line in enumerate(f.readlines(), start=1):
        if isGameValid(line):
            validGameIds.append(gameNumber)
print(sum(validGameIds))
