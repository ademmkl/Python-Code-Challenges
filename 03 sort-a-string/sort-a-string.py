"""
def sortSring(str):
    strListed = str.split(" ")
    strListed.sort()

    strSorted = " ".join(strListed)

    return  strSorted
"""

def sortSring(string):
    return " ".join(sorted(string.split(" "), key=str.casefold))

print(sortSring("Hello World I am Adem"))