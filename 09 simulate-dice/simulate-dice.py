import random
#import winsound as ws

"""
def simulateDice1():
    global sides

    try:
        sides = int(input("Give an integer for sides of the dice\n"))
    except ValueError:
        print("Given number has to be an integer!")

    if sides > 0:
        pass
    else:
        raise("Please give an integer which is bigger than 0.")


    listOfNums = []

    while True:
        try:
            num = random.randint(1, sides)
            ws.PlaySound("dice.wav", ws.SND_FILENAME)
            print("Your lucky number is: {0}".format(num))

            listOfNums.append(num)
            posb = (listOfNums.count(num)/len(listOfNums))*100
            print("It's possibilty was %{0}".format(posb))

            condition = input("Do you wanna play again?('Y for yes and N for no')\n")

            if condition == "Y":
                continue
            elif condition == "N":
                break
        except Exception as e:
            print("There is something wrong.\n{0}".format(e))
"""


from collections import Counter


def simulateDice2(*dice, numTrials=1000000):
    counts = Counter()

    for i in range(0, numTrials):
        counts[sum([random.randint(1, sides) for sides in dice])] += 1

    for num in range(len(dice), sum(dice)+1):
        print("{}: %{:0.3f}".format(num, counts[num]/numTrials*100))


simulateDice2(6, 6)