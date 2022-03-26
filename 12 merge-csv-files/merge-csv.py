import csv


def mergeCSV(*inputFiles, outputFile):
    headerList = []
    for file in inputFiles:
        with open(file) as csvFile:
            csvReader = csv.DictReader(csvFile)
            headerList.extend([i for i in csvReader.fieldnames if i not in headerList])

    with open(outputFile, "wt", newline="") as output:
        csvWriter = csv.DictWriter(output, fieldnames=headerList)
        csvWriter.writeheader()
        for file in inputFiles:
            with open(file) as csvFile:
                csvReader = csv.DictReader(csvFile)
                for row in csvReader:
                    csvWriter.writerow(row)


mergeCSV("class1.csv", "class2.csv", outputFile="exported.csv")
