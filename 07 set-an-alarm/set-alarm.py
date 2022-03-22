import time
import winsound as ws


def setAlarm(sound, alarmMessage, hour, minutes, seconds=0):
    alarmList = []

    for i in (hour, minutes, seconds):
        if i < 10:
            alarmList.append("0{}".format(i))
        else:
            alarmList.append("{}".format(i))

    alarm = ":".join(alarmList)
    now = time.strftime("%H:%M:%S")

    while now != alarm:
        now = time.strftime("%H:%M:%S")

    ws.PlaySound("alarm.wav", ws.SND_FILENAME)
    print(alarmMessage)



setAlarm("alarm.wav", "Wake Up!", 13, 48)