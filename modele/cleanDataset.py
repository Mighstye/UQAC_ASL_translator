from tensorflow import keras
import json
import numpy as np
import os
from tqdm import tqdm


if __name__ == '__main__':

    files = os.listdir('datasets')
    fileList = []
    for file in files:
        if file.startswith('DataF'):
            fileList.append(file)
    with tqdm(total=len(fileList)) as pbar:
        pbar.desc = 'Progress'
        for file in fileList:
            with open('datasets/' + file) as featureFile:
                featureFileString = json.load(featureFile)
                features = json.loads(featureFileString)
                featureFileString = ''

            featuresTab = []
            classesTab = []
            lenTab = []
            iteration = 0
            with tqdm(total=len(features)) as pbar2:
                pbar2.desc = 'Feature'
                for sign in range(len(features)):
                    featuresTab.append([])
                    for frame in features[sign]:
                        for type in frame:
                            for hand in type:
                                for keypoints in hand:
                                    featuresTab[sign].append(keypoints[0])
                    while len(featuresTab[sign]) != 15000:
                        if len(featuresTab[sign]) > 15000:
                            featuresTab[sign].pop()
                        elif len(featuresTab[sign]) < 15000:
                            featuresTab[sign].append([0, 0, 0])
                    pbar2.update(1)
            with open('cleanDataset/'+file, 'w') as infile:
                json.dump(json.dumps(featuresTab), infile)
            featureFileString = ''
            features = None
            classesFileString = ''
            classes = None
            os.system('cls')
            pbar.update(1)
