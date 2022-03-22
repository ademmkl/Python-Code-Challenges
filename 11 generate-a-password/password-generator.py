# import random
# Do not use random for security stuffs

import secrets
import json


def pwGenerator(num):
    file = open("diceware.json", "rt")
    allDict = json.loads(file.read())
    allWords = list(allDict.values())

    # passwordList = random.sample(difWords, num)
    passwordList = [secrets.choice(allWords) for _ in range(num)]

    password = " ".join(passwordList)

    return password


print(pwGenerator(10))
