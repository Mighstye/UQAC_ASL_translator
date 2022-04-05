import os
import pysrt
import time

if __name__ == '__main__':
    filesName = []
    allSubtitles = []

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
        listOfParagraphes = []
        # subtitleNumber = []
        f = open("C:/Users/romai/DatasetDeeplearning/" + file, encoding='utf-8')
        lines = f.readlines()
        #print(lines)
        #time.sleep(1)
        for line in lines:  # Separates paragraphes
            #print(line)
            if line == '\n':
                paragraphes.append([])
            else:
                paragraphes[-1].append(line)
            print("########")
            print(paragraphes[-1])
            print("########")
        time.sleep(10)
        #print("Before removing : " + str(paragraphes[-1]))
        for i in range(3):
            paragraphes.pop(-1)



        #print("After removing : " + str(paragraphes[-1]))



        # sortie : paragraphes

        iterations = 0
        editedParagraphe = []
        paragraphe = [None, None, None,]
        for element in paragraphes:
            #print(str(iterations) + "/" + str(len(paragraphes)))
            iterations+=1
            # subtitleNumber.append(paragraphe[0])
            #print(element[1][0:11])
            #print(element[1][17:28])
            print("#################")
            print(element)
            print(str(element[1][0:11]))
            print(str(element[1][17:28]))
            print("#################")
            paragraphe[1] = [str(element[1][0:11]) + str(element[1][17:28])]

            if not " " in element[2][3:]:  # If not a phrase
                paragraphe[2] = element[2][3:]

            #print(element)
            editedParagraphe.append(paragraphe)
            #print(editedParagraphe[-1])
        #print(paragraphes)

"""
        print(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        subs = pysrt.open(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        print(subs)
        allSubtitles.append(subs)
        fileName = file.split("_")
        fileName = fileName[0].split(".")
        filesName.append(fileName[0])
        allSubtitles.append(subs)
"""