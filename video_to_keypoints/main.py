import mediapipe as mp
import cv2
import pickle
import os
from tqdm import tqdm

if __name__ == '__main__':
    complete_file_list = os.listdir(r'\\FIXE_ROMAIN\Dataset deeplearning')
    filelist = []
    for file in complete_file_list:
        if file.endswith('.mp4') and not file.endswith('_1a1.mp4') and not file.endswith('_1b1.mp4') \
                and not file.endswith('_1c.mp4'):
            file = file.replace('.mp4', '')
            if not (file + '_1a1.mp4' in complete_file_list and file + '_1b1.mp4' in complete_file_list):
                file = file + '.mp4'
                filelist.append(file)
    for file in filelist:
        cap = cv2.VideoCapture(os.path.join(r'\\FIXE_ROMAIN\Dataset deeplearning', file))
        mp_hands = mp.solutions.hands
        OUTPUT_multi_hand_landmarks = []
        OUTPUT_multi_hand_world_landmarks = []
        OUTPUT_multi_handedness = []
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
                    OUTPUT_multi_hand_landmarks.append(results.multi_hand_landmarks)
                    OUTPUT_multi_hand_world_landmarks.append(results.multi_hand_world_landmarks)
                    OUTPUT_multi_handedness.append(results.multi_handedness)
                    pbar.update(1)
        with open('pkl/MULTI_HAND_LANDMARKS/' + file.replace('.mp4', '_') + 'MULTI_HAND_LANDMARKS.pkl',
                  'wb') as outfile:
            pickle.dump(OUTPUT_multi_hand_landmarks, outfile, pickle.HIGHEST_PROTOCOL)
        with open('pkl/MULTI_HAND_WORLD_LANDMARKS/' + file.replace('.mp4', '_') + 'MULTI_HAND_WORLD_LANDMARKS.pkl',
                  'wb') as outfile:
            pickle.dump(OUTPUT_multi_hand_world_landmarks, outfile, pickle.HIGHEST_PROTOCOL)
        with open('pkl/MULTI_HANDEDNESS/' + file.replace('.mp4', '_') + 'MULTI_HANDEDNESS.pkl', 'wb') as outfile:
            pickle.dump(OUTPUT_multi_handedness, outfile, pickle.HIGHEST_PROTOCOL)
        cap.release()
