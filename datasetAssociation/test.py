import json


if __name__ == '__main__':
    with open('multihand_world_landmarks/1176340_1a1.mp4.json') as infile:
           object = json.load(infile)
           realobject = json.loads(object)

    print(realobject)
