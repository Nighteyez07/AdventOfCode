from pathlib import Path

def main():
    path = Path(__file__).parent / "day05-input.txt"
    data = open(path).read().split('\n')

    crates = crateStart(data)
    crates9001 = crateStart(data)

    actions = getActions(data)

    for step in actions:
        doCount = step["counter"]
        for count in range(0, doCount, 1):
            crates[step["end"]].append(crates[[step["start"]][-1]].pop())

        startIdx = len(crates9001[step["start"]]) - step["counter"]
        dataToMove = crates9001[step["start"]][startIdx:(startIdx + step["counter"])]
        del crates9001[step["start"]][-step["counter"]:]
        crates9001[step["end"]].extend(dataToMove)

    message = ""
    for item in crates:
        message += item[-1]

    message9001 = ""
    for item in crates9001:
        message9001 += item[-1]

    print(message)    
    print(message9001)

def getActions(data):
    startLine = 10
    actions = []
    
    for line in data[startLine:]:
        moveData = line.split(" ")
        actions.append({
            "counter": int(moveData[1]),
            "start": int(moveData[3]) -1,
            "end": int(moveData[5]) -1
        })
    
    return actions

def crateStart(data):
    crates = [[] * 1 for i in range(9) ]
    indexes = [2,6,10,14,18,22,26,30,34]
    
    for stack, value in enumerate(indexes):
        for x in range(7, -1, -1):
            stringIndex = value - 1
            if data[x][stringIndex] != " ":
                crates[stack].append(data[x][stringIndex])
    
    return crates

def getCharAtPosition(string, index):
    return string[index]

if __name__ == "__main__":
    main()