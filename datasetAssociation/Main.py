import json
import pickle
from cv2 import cv2
import mediapipe
import random
import os
from tqdm import tqdm

if __name__ == '__main__':

    def convertToFrame(timecodeTab, fps):
        return parseToFrame(timecodeTab[0], fps), parseToFrame(timecodeTab[1], fps)

    def parseToFrame(timecode, fps):
        splitted = timecode.split(':')
        hours_count = int(splitted[0])
        minute_count = (int(hours_count) * 60) + int(splitted[1])
        seconde_count = (int(minute_count) * 60) + float(splitted[2].replace(',', '.'))

        return seconde_count*fps

    def getFileInfos(file):
        namefile = file + '.mp4'
        cap = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', namefile))
        # SUBTITLES
        with open('srt/' + file + '_en.srt.pkl', 'rb') as infile:
            subtitles = pickle.load(infile)
        # MULTI HAND LANDMARKS
        try:
            with open('Multi_hand_landmarks/' + file + '_1a1.mp4.json') as infile:
                MHL_A_JString = json.load(infile)
                MHL_A = json.loads(MHL_A_JString)
        except FileNotFoundError:
            MHL_A_JString = None
            MHL_A = None
        try:
            with open('Multi_hand_landmarks/' + file + '_1b1.mp4.json') as infile:
                MHL_B_JString = json.load(infile)
                MHL_B = json.loads(MHL_B_JString)
        except FileNotFoundError:
            MHL_B_JString = None
            MHL_B = None
        # MULTI HAND WORLD LANDMARKS
        try:
            with open('multihand_world_landmarks/' + file + '_1a1.mp4.json') as infile:
                MHWL_A_JString = json.load(infile)
                MHWL_A = json.loads(MHWL_A_JString)
        except FileNotFoundError:
            MHWL_A_JString = None
            MHWL_A = None
        try:
            with open('multihand_world_landmarks/' + file + '_1b1.mp4.json') as infile:
                MHWL_B_JString = json.load(infile)
                MHWL_B = json.loads(MHWL_B_JString)
        except FileNotFoundError:
            MHWL_B_JString = None
            MHWL_B = None

        return MHL_A, MHL_B, MHWL_A, MHWL_B, subtitles

    def extractData(fileMHL_A, fileMHL_B, fileMHWL_A, fileMHWL_B, filesubtitles, fps):
        DatasetFeatures = []
        DatasetClasses = []
        with tqdm(total=len(filesubtitles)) as pbar2:
            for subtitle in filesubtitles:
                sign = []
                timecode_start, timecode_end = convertToFrame(subtitle[1], fps)
                pbar2.desc = 'Traitement'
                for loop in range(int(timecode_start), int(timecode_end)):
                    try:
                        if subtitle[2] == 'A':
                            sign.append((fileMHL_A[loop], fileMHWL_A[loop]))
                            DatasetClasses.append(subtitle[0])
                        elif subtitle[2] == 'B':
                            sign.append((fileMHL_B[loop], fileMHWL_B[loop]))
                            DatasetClasses.append(subtitle[0])
                        else:
                            pass
                    except IndexError:
                        pass
                    except TypeError:
                        pass
                DatasetFeatures.append(sign)
                pbar2.update(1)
        return DatasetFeatures, DatasetClasses



    completeFileList = os.listdir("Multi_hand_landmarks")
    filelist = []
    for file in completeFileList:
        if file.endswith('_1a1.mp4.json') or file.endswith('_1b1.mp4.json'):
            filelist.append(file)
    independantFileList = []
    for file in filelist:
        if file.endswith('_1a1.mp4.json'):
            if file.split("_")[0] + "_1b1.mp4.json" not in independantFileList:
                independantFileList.append(file)
        elif file.endswith('_1b1.mp4.json'):
            if file.split("_")[0] + "_1a1.mp4.json" not in independantFileList:
                independantFileList.append(file)
    for index in range(len(independantFileList)):
        independantFileList[index] = independantFileList[index].split("_")[0]
    for file in independantFileList:
        if file+'_en.srt.pkl' not in os.listdir('srt'):
            independantFileList.remove(file)

    with tqdm(total=len(independantFileList)) as pbar:
        iterator = 0
        pbar.desc = 'Advancement'
        while len(independantFileList) > 2:
            file1 = random.choice(independantFileList)
            independantFileList.remove(file1)
            file2 = random.choice(independantFileList)
            independantFileList.remove(file2)
            file3 = random.choice(independantFileList)
            independantFileList.remove(file3)
            video1 = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', file1 + '.mp4'))
            fps1 = int(video1.get(cv2.CAP_PROP_FPS))
            video2 = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', file2 + '.mp4'))
            fps2 = int(video1.get(cv2.CAP_PROP_FPS))
            video3 = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', file3 + '.mp4'))
            fps3 = int(video1.get(cv2.CAP_PROP_FPS))
            video1.release()
            video2.release()
            video3.release()
            file1MHL_A, file1MHL_B, file1MHWL_A, file1MHWL_B, file1subtitles = getFileInfos(file1)
            file2MHL_A, file2MHL_B, file2MHWL_A, file2MHWL_B, file2subtitles = getFileInfos(file2)
            file3MHL_A, file3MHL_B, file3MHWL_A, file3MHWL_B, file3subtitles = getFileInfos(file3)

            DatasetFeatures1, DatasetClasses1 = extractData(file1MHL_A, file1MHL_B, file1MHWL_A, file1MHWL_B, file1subtitles, fps1)
            DatasetFeatures2, DatasetClasses2 = extractData(file2MHL_A, file2MHL_B, file2MHWL_A, file2MHWL_B, file2subtitles, fps2)
            DatasetFeatures3, DatasetClasses3 = extractData(file3MHL_A, file3MHL_B, file3MHWL_A, file3MHWL_B, file3subtitles, fps3)

            DatasetFeatures = DatasetFeatures1 + DatasetFeatures2 + DatasetFeatures3
            DatasetClasses = DatasetClasses1 + DatasetClasses2 + DatasetClasses3

            Datasets = list(zip(DatasetFeatures, DatasetClasses))
            random.shuffle(Datasets)

            DatasetFeatures, DatasetClasses = zip(*Datasets)

            jsonString = json.dumps(DatasetFeatures)
            with open('datasetFiles/DataFEATURES' + str(iterator) + '.json', 'w') as outfile:
                json.dump(jsonString, outfile)
            jsonString = json.dumps(DatasetClasses)
            with open('datasetFiles/DataCLASSES' + str(iterator) + '.json', 'w') as outfile:
                json.dump(jsonString, outfile)
            iterator += 1
            os.system('cls')
            pbar.update(3)
