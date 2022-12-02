from pathlib import Path

def main():
    path = Path(__file__).parent / "day02-input.txt"

    d = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
    d2 = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}
    data = open(path).read().split('\n')
    print(sum([d[x] for x in data]))
    print(sum([d2[x] for x in data]))

if __name__ == "__main__":
    main()