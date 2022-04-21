import json


if __name__ == '__main__':
    with open('datasetFiles/DataFEATURES0.json') as infile:
        jsonString = json.load(infile)
        Features = json.loads(jsonString)

    with open('datasetFiles/DataCLASSES0.json') as infile:
        jsonString = json.load(infile)
        Classes = json.loads(jsonString)

    print(Features[5])
    print(Classes[5])