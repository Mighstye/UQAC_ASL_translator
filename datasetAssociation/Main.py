import json
import pickle
from cv2 import cv2
import mediapipe


def keypointsToSt(fps, sousTitres, real_object_multi, real_object_world, dict):   # remplie dictionnaire dont key = sous titre et valeur liste [ keypoints multi, keypoints world ]
    listOfKeypoints = []
    listOfKeypoints_multi = []
    listOfKeypoints_world = []

    for v in range(len(sousTitres)):
        i = (sousTitres[v][1]/1000) * fps
        j = (sousTitres[v][2]/1000) * fps

        for k in range(len(real_object_multi)):
            if k>=i and k<=j:
                listOfKeypoints.append(real_object_multi[k])
        for k in range(len(real_object_world)):
            if k>=i and k<=j:
                listOfKeypoints.append(real_object_world[k])

        listOfKeypoints.append(listOfKeypoints_multi)
        listOfKeypoints.append(listOfKeypoints_world)

        if sousTitres[v][0] in dict.keys():
            dict[sousTitres[v][0]].append(listOfKeypoints)
        else:
            dict[sousTitres[v][0]] = []
            dict[sousTitres[v][0]].append(listOfKeypoints)

def transformationTime(sousTitres):      #retourne la liste des sous titres avec pou chacun d'eux le temps de début et de fin en millisecondes
    timer_sousTitre = []

    for sousTitre in sousTitres:
        liste = []

        heuresDebut = int(sousTitre[1][0][0:2])
        minutesDebut = int(sousTitre[1][0][3:5])
        secondesDebut = int(sousTitre[1][0][6:8])
        millisecondesDebut = int(sousTitre[1][0][9:12])

        heuresFin = int(sousTitre[1][1][0:2])
        minutesFin = int(sousTitre[1][1][3:5])
        secondesFin = int(sousTitre[1][1][6:8])
        millisecondesFin = int(sousTitre[1][1][9:12])

        tempsDebut = (heuresDebut * 3600 + minutesDebut * 60 + secondesDebut) * 1000 + millisecondesDebut
        tempsFin = (heuresFin * 3600 + minutesFin * 60 + secondesFin) * 1000 + millisecondesFin

        liste.append(sousTitre[0])
        liste.append(tempsDebut)
        liste.append(tempsFin)

        timer_sousTitre.append(liste)

    return timer_sousTitre







if __name__ == '__main__':
    video = cv2.VideoCapture('1176340_1a1.mp4')
    fps = int(video.get(cv2.CAP_PROP_FPS))
    dictKeypointSt = {}
    print("fps : "+str(fps))


    with open("Multi_hand_landmarks/1176340_1a1.mp4.json", "r") as file:
        multi_hand_landmarks = json.load(file)

        real_object_multi = json.loads(multi_hand_landmarks)
    #print(multi_hand_landmarks[15][0].landmark[3])

    with open("multihand_world_landmarks/1176340_1a1.mp4(1).json", "r") as file:
        multihand_world_landmarks = json.load(file)
        real_object_world = json.loads(multi_hand_landmarks)

    with open("1176340_en.srt.pkl", "rb") as file:
        sousTitres = pickle.load(file)

    timer_sousTitre = transformationTime(sousTitres)

    print(len(timer_sousTitre))
    keypointsToSt(fps, timer_sousTitre, real_object_multi, real_object_world, dictKeypointSt)

    print(dictKeypointSt['MUSS1*'][1])


















