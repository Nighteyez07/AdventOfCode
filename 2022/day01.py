
def main():
    elfList = []
    with open('C:/Users/Duncan/Repos/AdventOfCode/2022/day01-input.txt','r') as f:
        calorieList = []
        for line in f:
            if len(line.strip()) == 0:
                elfList.append(calorieList)
                calorieList = []
            else:
                calorieList.append(int(line.strip()))
        elfList.append(calorieList) #captures end segment

    totalCalorieList = []
    elfIndex = 1
    for elf in elfList:
        totalCalorieList.append([elfIndex, sum(elf)])
        elfIndex += 1
    
    maxValue = [0,0]
    for elfTotal in totalCalorieList:
        if elfTotal[1] > maxValue[1]:
            maxValue = elfTotal

    topThreeList = sorted(totalCalorieList, key=lambda x: x[1], reverse=True)[:3]
    topThreeSum = 0
    for item in topThreeList:
        topThreeSum += item[1]

    print(f"Most calories held by one elf {maxValue[1]}")
    print(f"Sum of calories held by top three elves {topThreeSum}")
if __name__ == "__main__":
    main()