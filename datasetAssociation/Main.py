import json
import pickle
from cv2 import cv2
import mediapipe


def keypointsToSt(fps, sousTitres, real_object, dict):
    listOfKeypoints = []

    for v in range(len(sousTitres)):
        i = (sousTitres[v][1]/1000) * fps
        j = (sousTitres[v][2]/1000) * fps


        for k in range(len(real_object)):
            if k>=i and k<=j:
                listOfKeypoints.append(real_object[k])

        if sousTitres[v][0] in dict.keys():
            dict[sousTitres[v][0]].append(listOfKeypoints)
        else:
            dict[sousTitres[v][0]] = []
            dict[sousTitres[v][0]].append(listOfKeypoints)








if __name__ == '__main__':
    video = cv2.VideoCapture('1176340_1a1.mp4')
    fps = int(video.get(cv2.CAP_PROP_FPS))
    dictKeypointSt = {}
    print("fps : "+str(fps))


    with open("Multi_hand_landmarks/1176340_1a1.mp4.json", "r") as file:
        multi_hand_landmarks = json.load(file)

        real_object = json.loads(multi_hand_landmarks)
    #print(multi_hand_landmarks[15][0].landmark[3])

    with open("1176340_en.srt.pkl", "rb") as file:
        sousTitres = pickle.load(file)

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


    print(len(timer_sousTitre))
    keypointsToSt(fps, timer_sousTitre, real_object, dictKeypointSt)


    print(len(real_object[2]))
    print(len(dictKeypointSt[timer_sousTitre[1][0]]))
















