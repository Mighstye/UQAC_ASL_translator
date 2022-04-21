import mediapipe as mp
import cv2
import json
import os
from tqdm import tqdm

if __name__ == '__main__':
    complete_file_list = os.listdir(r'\\FIXE_ROMAIN\DatasetDeeplearning')
    filelist = []
    for file in complete_file_list:
        if file.endswith('_1a1.mp4') or file.endswith('_1b1.mp4'):
            filelist.append(file)
    for file in filelist:
        if file.endswith('1a1.mp4'):
            srt = file.replace('_1a1.mp4', '_en.srt')
        elif file.endswith('1b1.mp4'):
            srt = file.replace('_1b1.mp4', '_en.srt')
        else:
            srt = ''
        if srt not in complete_file_list and srt != '':
            filelist.remove(file)
    for file in filelist:
        for file in filelist:
            if file.endswith('1a1.mp4'):
                jsonfile = file.replace('_1a1.mp4', '_1a1.mp4.json')
            elif file.endswith('1b1.mp4'):
                jsonfile = file.replace('_1b1.mp4', '_1b1.mp4.json')
            else:
                jsonfile = ''
            alreadyTreated = os.listdir('json/MULTI_HAND_LANDMARKS')
            if jsonfile in alreadyTreated or jsonfile == '':
                filelist.remove(file)
    with tqdm(total=len(filelist)) as filepbar:
        filepbar.desc = 'Global advancement'
        for file in filelist:
            cap = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', file))
            mp_hands = mp.solutions.hands
            RESULT_multi_hand_landmarks = []
            RESULT_multi_hand_world_landmarks = []
            RESULT_multi_handedness = []
            frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            with tqdm(total=frame_number) as pbar:
                pbar.desc = file
                with mp_hands.Hands(
                        model_complexity=0,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:
                    while cap.isOpened():
                        success, image = cap.read()
                        if not success:
                            # If loading a video, use 'break' instead of 'continue'.
                            break

                        # To improve performance, optionally mark the image as not writeable to
                        # pass by reference.
                        image.flags.writeable = False
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        results = hands.process(image)
                        RESULT_multi_hand_landmarks.append(results.multi_hand_landmarks)
                        RESULT_multi_hand_world_landmarks.append(results.multi_hand_world_landmarks)
                        RESULT_multi_handedness.append(results.multi_handedness)
                        pbar.update(1)
            with tqdm(total=len(RESULT_multi_hand_world_landmarks)) as pbar:
                pbar.desc = 'Creating MULTI_HAND_WORLD_LANDMARKS'
                OUTPUT_MULTI_HAND_WORLD_LANDMARKS = []
                for frame in range(len(RESULT_multi_hand_world_landmarks)):
                    OUTPUT_MULTI_HAND_WORLD_LANDMARKS.append([])
                    if RESULT_multi_hand_world_landmarks[frame]:
                        for hand in range(len(RESULT_multi_hand_world_landmarks[frame])):
                            OUTPUT_MULTI_HAND_WORLD_LANDMARKS[frame].append([])
                            for landmark in range(len(RESULT_multi_hand_world_landmarks[frame][hand].landmark)):
                                OUTPUT_MULTI_HAND_WORLD_LANDMARKS[frame][hand].append([])
                                x = RESULT_multi_hand_world_landmarks[frame][hand].landmark[landmark].x
                                y = RESULT_multi_hand_world_landmarks[frame][hand].landmark[landmark].y
                                z = RESULT_multi_hand_world_landmarks[frame][hand].landmark[landmark].z
                                OUTPUT_MULTI_HAND_WORLD_LANDMARKS[frame][hand][landmark].append((x, y, z))
                    pbar.update(1)
            jsonString = json.dumps(OUTPUT_MULTI_HAND_WORLD_LANDMARKS)
            with open('json/MULTI_HAND_WORLD_LANDMARKS/' + file + '.json', 'w') as outfile:
                json.dump(jsonString, outfile)
            with tqdm(total=len(RESULT_multi_hand_landmarks)) as pbar:
                pbar.desc = 'Creating MULTI_HAND_LANDMARKS'
                OUTPUT_MULTI_HAND_LANDMARKS = []
                for frame in range(len(RESULT_multi_hand_landmarks)):
                    OUTPUT_MULTI_HAND_LANDMARKS.append([])
                    if RESULT_multi_hand_landmarks[frame]:
                        for hand in range(len(RESULT_multi_hand_landmarks[frame])):
                            OUTPUT_MULTI_HAND_LANDMARKS[frame].append([])
                            for landmark in range(len(RESULT_multi_hand_landmarks[frame][hand].landmark)):
                                OUTPUT_MULTI_HAND_LANDMARKS[frame][hand].append([])
                                x = RESULT_multi_hand_landmarks[frame][hand].landmark[landmark].x
                                y = RESULT_multi_hand_landmarks[frame][hand].landmark[landmark].y
                                z = RESULT_multi_hand_landmarks[frame][hand].landmark[landmark].z
                                OUTPUT_MULTI_HAND_LANDMARKS[frame][hand][landmark].append((x, y, z))
                    pbar.update(1)
            jsonString = json.dumps(OUTPUT_MULTI_HAND_LANDMARKS)
            with open('json/MULTI_HAND_LANDMARKS/' + file + '.json', 'w') as outfile:
                json.dump(jsonString, outfile)
            with tqdm(total=len(RESULT_multi_handedness)) as pbar:
                pbar.desc = 'Creating MULTI_HANDEDNESS'
                OUTPUT_MULTI_HANDEDNESS = []
                for frame in range(len(RESULT_multi_handedness)):
                    OUTPUT_MULTI_HANDEDNESS.append([])
                    if RESULT_multi_handedness[frame]:
                        for hand in range(len(RESULT_multi_handedness[frame])):
                            OUTPUT_MULTI_HANDEDNESS[frame].append([])
                            index = RESULT_multi_handedness[frame][hand].classification[0].index
                            score = RESULT_multi_handedness[frame][hand].classification[0].score
                            label = RESULT_multi_handedness[frame][hand].classification[0].label
                            OUTPUT_MULTI_HANDEDNESS[frame][hand].append((index, score, label))
                    pbar.update(1)
            jsonString = json.dumps(OUTPUT_MULTI_HANDEDNESS)
            with open('json/MULTI_HANDEDNESS/' + file + '.json', 'w') as outfile:
                json.dump(jsonString, outfile)
            cap.release()
            os.system('cls')
            filepbar.update(1)
