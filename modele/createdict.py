import os
import json
from tqdm import tqdm

if __name__ == '__main__':

    allFile = os.listdir('datasets/')
    neededFile = []
    for file in allFile:
        if file.startswith('DataC'):
            neededFile.append(file)
    dictionnary = {}
    with tqdm(total=len(neededFile)) as pbar:
        for file in neededFile:
            with open('datasets/'+file) as infile:
                classe = json.loads(json.load(infile))
            for c in classe:
                if c not in dictionnary:
                    dictionnary.update({c: len(dictionnary)})
            pbar.update(1)

    jsonString = json.dumps(dictionnary)
    with open('DICTIONNARY', 'w') as outfile:
        json.dump(jsonString, outfile)

    with tqdm(total=len(neededFile)) as pbar:
        for file in neededFile:
            with open('datasets/'+file, 'r') as infile:
                classe = json.loads(json.load(infile))
            classeID = []
            for c in classe:
                classeID.append(dictionnary.get(c))
            with open('cleanDataset/'+file, 'w') as outfile:
                json.dump(json.dumps(classeID), outfile)
            pbar.update(1)
