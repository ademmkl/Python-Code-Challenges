import time
import random


def theWaitingGame():

    print("Hi player!")
    time.sleep(2)
    print("Please, start when I say start to you and finish by pushing the enter button when you feel ready.")
    time.sleep(6)

    while True:
        waitingTime = random.randint(1,100)

        print("Your goal is to wait {} seconds.".format(waitingTime))
        time.sleep(3)

        for i in [3, 2, 1]:
            print(i)
            time.sleep(2)

        print("Start!")

        timeStart = time.time()
        input()
        timeFinish = time.time()

        waitingScore = round(timeFinish - timeStart)

        print("Your waiting score is", waitingScore)

        if waitingTime > waitingScore:
            print("You need to be more patient!")
            time.sleep(2)
            print("It was {} seconds more than the time that I want you to wait.".format(waitingTime - waitingScore))
        elif waitingTime < waitingScore:
            print("That was slow.")
            time.sleep(2)
            print("It was {} seconds less than the time that I want you to wait.".format(waitingScore - waitingTime))
        else:
            print("Congratulations! That must be hard!")

        if input("Do you wanna play another game?") == "Yes":
            continue

        break


theWaitingGame()