def countingValleys(steps, path):
    # Write your code here
    seaLevel = 0
    valley = 0
    for step in path:
        if step == 'U':
            seaLevel += 1
            if seaLevel == 0:
                valley += 1
        else:
            seaLevel -= 1
    return valley
