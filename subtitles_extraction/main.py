import os
import pysrt


if __name__ == '__main__':
    filesName = []
    allSubtitles = []


# C:\Users\romai\Dataset deeplearning
# r'\FIXE_ROMAIN\Dataset deeplearning'
    complete_file_list = os.listdir("C:\\Users\\romai\\DatasetDeeplearning")
    filelist = []
    for file in complete_file_list:
        if file.endswith('.mp4') and not file.endswith('_1a1.mp4') and not file.endswith('_1b1.mp4') \
                and not file.endswith('_1c.mp4'):
            file = file.replace('.mp4', '')
            if not (file + '_1a1.mp4' in complete_file_list and file + '_1b1.mp4' in complete_file_list):
                file = file + '_en.srt'
                filelist.append(file)
    for file in filelist:
        print(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        subs = pysrt.open(os.path.join("C:\\Users\\romai\\DatasetDeeplearning", file))
        print(subs)
        allSubtitles.append(subs)
        fileName = file.split("_")
        fileName = fileName[0].split(".")
        filesName.append(fileName[0])
        allSubtitles.append(subs)