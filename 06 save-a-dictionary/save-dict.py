import json


def saveDict(dictionary):
    content = json.dumps(dictionary, sort_keys=True, indent=4)

    file = open("save-dict.json", "w")
    file.write(content)
    file.close()


def getDict(jsonFile):
    file = open(jsonFile, "r")
    text = file.read()
    file.close()
    return json.loads(text)


myDict = {"name": "adem", "age": "19", "nationality": "turkish"}
saveDict(myDict)

print(getDict("save-dict.json"))
