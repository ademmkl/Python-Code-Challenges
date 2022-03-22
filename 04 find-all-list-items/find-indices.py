
def allIndex(takenList, item):
    givenList = []

    i = 0
    while i < len(takenList):
        if takenList[i] == item:
            givenList.append([i])
        elif isinstance(takenList[i], list):
            for index in allIndex(takenList[i], item):
                givenList.append([i] + index)

        i += 1

    return givenList


listExample = [[[1, "d", "data", 8, "mute"], "mute", 1], 1]
print(allIndex(listExample, 1))

