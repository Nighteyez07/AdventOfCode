from pathlib import Path

def main():
    path = Path(__file__).parent / "day04-input.txt"
    data = open(path).read().split('\n')

    matchSum = 0
    overlapSum = 0

    for x in data:
        sections = x.split(',')
        
        firstElf = sections[0].split('-')
        secondElf = sections[1].split('-')
        
        if int(firstElf[0]) <= int(secondElf[0]) and int(firstElf[1]) >= int(secondElf[1]):
            matchSum += 1
        elif int(firstElf[0]) >= int(secondElf[0]) and int(firstElf[1]) <= int(secondElf[1]):
            matchSum += 1

        if (int(firstElf[0]) < int(secondElf[0]) and int(firstElf[1]) < int(secondElf[0])):
            overlapSum += 1
        elif (int(secondElf[0]) < int(firstElf[0]) and int(secondElf[1]) < int(firstElf[0])):
            overlapSum += 1

    print(f"pairs in one range fully contained in the other are {matchSum}")
    print(f"pairs with any overlap {len(data) - overlapSum}")

if __name__ == "__main__":
    main()