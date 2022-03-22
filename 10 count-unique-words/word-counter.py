from collections import Counter
import re

def wordCounter(file):

    def keyMethod(tuple):
        return tuple[1]


    #counts = Counter()

    textFile = open(file, "rt")
    text = textFile.read()
    textRe = re.findall(r"[0-9a-zA-Z]+",text)

    """for i in textRe:
        counts[i.casefold()] += 1"""

    counts = Counter([i.casefold() for i in textRe])


    """listOfCounteds= list(counts.items())
    sortedCounts = (sorted(listOfCounteds, key=keyMethod))[::-1]
    top20 = sortedCounts[:20]

    for key,value in top20:
        print(key, ":", value)"""

    #OR

    for key,value in counts.most_common(20):
        print(key, ":", value)

    textFile.close()


wordCounter("lorem-ipsum.txt")