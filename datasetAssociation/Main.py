import json
import pickle
from cv2 import cv2
import mediapipe
import os
from tqdm import tqdm

if __name__ == '__main__':
    video = cv2.VideoCapture('1176340_1a1.mp4')
    fps = int(video.get(cv2.CAP_PROP_FPS))

    def convertToFrame(timecodeTab):
        return parseToFrame(timecodeTab[0]), parseToFrame(timecodeTab[1])

    def parseToFrame(timecode):
        splitted = timecode.split(':')
        hours_count = int(splitted[0])
        minute_count = (int(hours_count) * 60) + int(splitted[1])
        seconde_count = (int(minute_count) * 60) + float(splitted[2].replace(',', '.'))

        return seconde_count*fps

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

    with tqdm(total=len(independantFileList)) as pbar:
        pbar.desc = 'Advancement'
        for file in independantFileList:
            namefile = file+'.mp4'
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
                    MHWL_A = json.loads(MHL_A_JString)
            except FileNotFoundError:
                MHWL_A_JString = None
                MHWL_A = None
            try:
                with open('multihand_world_landmarks/' + file + '_1b1.mp4.json') as infile:
                    MHWL_B_JString = json.load(infile)
                    MHWL_B = json.loads(MHL_B_JString)
            except FileNotFoundError:
                MHWL_B_JString = None
                MHWL_B = None

            DatasetFeatures = [None, None]
            DatasetClasses = [None]
            for subtitle in subtitles:
                print(subtitle)
