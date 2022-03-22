
"""
def isPalindrome(str):
    rStringList=[]
    
    for i in str.lower():
        rStringList.append(i)
        
    stringList = rStringList.copy()
    rStringList.reverse()
    
    return stringList == rStringList
"""

import re


def isPalindrome(str):

    forwards = "".join(re.findall("r[a-z]", str.lower()))
    backwards = forwards[::-1]

    return forwards == backwards

print(isPalindrome("Ada"))
