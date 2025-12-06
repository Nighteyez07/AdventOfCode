import copy
from pathlib import Path

def IsReportSafePart1(report):
    #loop each element in the list
    doesIncrease = True
    if report[0] - report[1] > 0:
        doesIncrease = False

    for i in range(len(report)):
        # check if next element is a difference between 1 and 3
        if i+1 < len(report):
            reportDiff = report[i] - report[i+1]

            if doesIncrease:
                if reportDiff < -3 or reportDiff > -1:
                    return False
            else:
                if reportDiff > 3 or reportDiff < 1:
                    return False

    return True   

def IsReportSafePart2(report, tolerate):
    flagRecord = False
    if tolerate == False:
        print(f"Report Recursion: {report}")
    else:
        print(f"Report Original: {report}")
    
    doesIncrease = True
    if report[0] - report[1] > 0:
        doesIncrease = False

    for i in range(len(report)):
        if i+1 < len(report):
            reportDiff = report[i] - report[i+1]

            if abs(reportDiff) < 4 and abs(reportDiff) > 0:
                if (doesIncrease and reportDiff > 0) or (not doesIncrease and reportDiff < 0):
                    flagRecord = True
            else:
                flagRecord = True
            
            if flagRecord:
                if len(report)-1 == i+1:
                    print(f"Last index failure at {i+1} with {reportDiff} of value {report[i+1]}")
                if tolerate:
                    currPop = copy.deepcopy(report)
                    #print(f"Report Original: {report}")
                    report.pop(i)
                    #print(f"Report Pop: {report}")
                    currPop.pop(i+1)
                    #print(f"Report Pop Next Index: {currPop}")
                    return IsReportSafePart2(report, False) or IsReportSafePart2(currPop, False)
                return False

    print(f"Safe Report: {report}")
    return True  

def ReportsSafe(reports):
    safe, safe2 = [], []

    for report in reports:
        report = report.split()
        report = [int(i) for i in report]
        if IsReportSafePart1(report):
            safe.append(report)
        if IsReportSafePart2(report, True):
            safe2.append(report)
        else:
            print(f"Report Not Safe: {report}")


    return safe, safe2

def check_safety(a):
  diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]    # build list of differences between consecutive pairs
  if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
    return True
  else:
    return False

def main():
    reports = []
    path = Path(__file__).parent / "day02-input.txt"
    for line in open(path):
        reports.append(line.strip())

    safe, safe2 = ReportsSafe(reports)
    print(f"Safe Reports: {len(safe)}")
    print(f"Safe Reports Part 2: {len(safe2)}")

if __name__ == "__main__":
    main()