from pathlib import Path

def CalculateDifference(col1, col2):
    diffScore = 0
    #loop through each element in the list and calculate the difference between the two columns
    for i in range(len(col1)):
        diff = abs(int(col1[i]) - int(col2[i]))
        diffScore += diff
        
    return diffScore

def CalculateSimilarity(col1, col2):
    simScore = 0
    #loop through col1 and find the count of matching elements in col2
    for i in range(len(col1)):
        count = col2.count(col1[i])
        simScore += int(col1[i]) * count
        
    return simScore

def main():
    path = Path(__file__).parent / "day01-input.txt"
    col1, col2 = [], []
    #parse input data with each column of data into 2 separate lists
    with open(path) as f:
        for line in f:
            data = line.split()
            if len(data) >= 2:
                col1.append(data[0])
                col2.append(data[1])
    
    col1.sort()
    col2.sort()
        
    colDiff = CalculateDifference(col1, col2)
    print(f"Column Difference: {colDiff}")    
    simScore = CalculateSimilarity(col1, col2)
    print(f"Column Similarity: {simScore}")


if __name__ == "__main__":
    main()