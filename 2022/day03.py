from pathlib import Path

def main():
    path = Path(__file__).parent / "day03-input.txt"
    data = open(path).read().split('\n')

    matchSum = 0
    for x in data:
        firstHalf = x[slice(0, len(x)//2)]
        secondHalf = x[slice(len(x)//2, len(x))]

        matches = list(set(firstHalf)&set(secondHalf))

        for c in matches:
            matchSum += getCharNumber(c)

    print(f"Sum of matches is {matchSum}")

    matchBatch = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            matches = list(set(val)&set(data[i+1])&set(data[i+2]))

            for c in matches:
                matchBatch += getCharNumber(c)
    
    print(f"Sum of batches is {matchBatch}")

def getCharNumber(input):
    val = ord(input)

    if val > 96:
        val = val - 96
    else:
        val = val - 64 + 26
    
    return val

if __name__ == "__main__":
    main()