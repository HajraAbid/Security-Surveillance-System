import cv2 as c
import numpy as np
import face_recognition as fc
import os
from datetime import datetime as dt
import winsound  # For alarm sound (works on Windows)

path = 'basic images'
images = []
classes = []
mylist = os.listdir(path)

for item in mylist:
    currentImage = c.imread(f'{path}\\{item}')
    images.append(currentImage)
    classes.append(os.path.splitext(item)[0])

def findEncodings(image):
    encodeList = []
    for img in image:
        img = c.cvtColor(img, c.COLOR_BGR2RGB)
        encode = fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('AttendanceRec.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = dt.now()
            dtString = now.strftime('%H:%M:%S')  # Corrected time format
            f.writelines(f'\n{name},{dtString}')

# Load the known faces and encodings
encodedList = findEncodings(images)

cap = c.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = c.resize(frame, (800, 600))
    gray = c.cvtColor(img, c.COLOR_BGR2RGB)

    faceLocations = fc.face_locations(gray)
    encodedFrame = fc.face_encodings(gray, faceLocations)

    # Flag for unrecognized faces
    recognized = False

    for faceLoc, encode in zip(faceLocations, encodedFrame):
        matches = fc.compare_faces(encodedList, encode)
        faceDis = fc.face_distance(encodedList, encode)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            recognized = True  # Person recognized
            name = classes[matchIndex].upper()
            print(f"Welcome {name}")

            y1, x2, y2, x1 = faceLoc
            c.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            c.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), c.FILLED)
            c.putText(img, name, (x1 + 6, y2 - 12), c.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

            markAttendance(name)
        else:
            # If the face is not recognized, trigger the alarm
            y1, x2, y2, x1 = faceLoc
            c.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red rectangle for unrecognized face
            c.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), c.FILLED)
            c.putText(img, "Unrecognized Face", (x1 + 6, y2 - 12), c.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

            # Play the alarm sound
            winsound.Beep(1000, 1000)  # Frequency: 1000Hz, Duration: 1000ms (1 second)

    if not recognized:
        print("No recognized face detected")

    c.imshow('Security Surveillance System', img)
    if c.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
c.destroyAllWindows()
