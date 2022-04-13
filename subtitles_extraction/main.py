import os
import pysrt
import time
import pickle

if __name__ == '__main__':
    filesName = []
    allSubtitles = [["" , []]]

    # C:\Users\romai\Dataset deeplearning
    # r'\FIXE_ROMAIN\Dataset deeplearning'
    # f = open(r"C:\Users\romai\DatasetDeeplearning\1176340_en.srt", encoding='utf8')
    # print(f.read())

    complete_file_list = os.listdir(r'C:\Users\romai\DatasetDeeplearning')
    filelist = []
    for file in complete_file_list:
        if file.endswith('_1a1.mp4') or file.endswith('_1b1.mp4'):
            if file not in filelist:
                file = file.split("_")
                file = file[0]
                file = file + "_en.srt"
                if file in complete_file_list and file not in filelist:
                    filelist.append(file)
    for file in filelist:
        paragraphes = [[]]
        # subtitleNumber = []
        f = open("C:/Users/romai/DatasetDeeplearning/" + file, encoding='utf-8')
        lines = f.readlines()
        for line in lines:  # Separates paragraphes
            if line == '\n':
                paragraphes.append([])
            else:
                paragraphes[-1].append(line)
        for i in range(3):
            paragraphes.pop(-1) # Remove blank lines at the end


        paragraphesWithoutSentences = []
        paragraphesWithSentences = []
        for element in paragraphes:
            try:
                text = element[2][3:]

                if " " not in text:
                    paragraphesWithoutSentences.append(element)
                else:
                    paragraphesWithSentences.append(element)
            except IndexError:
                pass

        editedParagraphes = []
        for element in paragraphesWithoutSentences:
                editedParagraphe = [None, None]
                editedParagraphe[1] = [str(element[1][0:12])] + [str(element[1][17:29])]
                editedParagraphe[0] = element[2][3:-1]
                editedParagraphes.append(editedParagraphe)
        with open('pkl/'+ file + '.pkl', 'wb') as outfile:
            pickle.dump(editedParagraphes, outfile, pickle.HIGHEST_PROTOCOL)


        sousTitres = editedParagraphes

        for sousTitre in sousTitres:

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