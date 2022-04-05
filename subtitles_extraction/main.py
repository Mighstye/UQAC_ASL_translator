import os
import pysrt


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
            filelist.append(file)
    #print(filelist)

    subs = pysrt.open()
"""
    for file in filelist:
        paragraphes = []
        # subtitleNumber = []
        f = open("C:/Users/romai/DatasetDeeplearning/" + file, encoding='utf-8')
        lines = f.readlines()
        print(lines)
        for line in lines: # Separates paragraphes
            if line == '/n':
                paragraphes.append([])
            else:
                paragraphes[-1].append(line)
        for paragraphe in paragraphes:
            # subtitleNumber.append(paragraphe[0])
            paragraphe[1] = [paragraphe[1][0:11]+ paragraphe[1][16:28]]
            # ]
            if not " " in paragraphe[2]: # If not a phrase
                paragraphe[2] = paragraphe[2][3:]
            paragraphes.append(paragraphe)
        print(paragraphes)
        
        
        print(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        subs = pysrt.open(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        print(subs)
        allSubtitles.append(subs)
        fileName = file.split("_")
        fileName = fileName[0].split(".")
        filesName.append(fileName[0])
        allSubtitles.append(subs)
        
        """