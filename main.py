import datetime
import cv2
import pickle
import numpy as np
import face_recognition
# import gspread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("k.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://crack-celerity-393115-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

file = open('EncodeFile.p', 'rb')
elkID = pickle.load(file)
file.close()
elk, ID = elkID
# gc = gspread.service_account(filename="key.json")
# wks = gc.open("Attendance_Data").sheet1
while True:
    success, img = cap.read()
    img_compressed = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_compressed = cv2.cvtColor(img_compressed, cv2.COLOR_BGR2RGB)
    cv2.imshow("MH4", img)
    cv2.waitKey(1)
    face = face_recognition.face_locations(img_compressed)
    encodeface = face_recognition.face_encodings(img_compressed, face)
    for encodeFace, faceLoc in zip(encodeface, face):
        matches = face_recognition.compare_faces(elk, encodeFace)
        facedistance = face_recognition.face_distance(elk, encodeFace)
        # print(matches)
        print(facedistance)
        matchIndex = np.argmin(facedistance)
        if matches[matchIndex]:
            # cell = wks.find(ID[matchIndex])
            # wks.update_cell(cell.row, cell.col+1, "PRESENT")
            # wks.update_cell(
            #     cell.row, cell.col+2, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            ref.child(f'{ID[matchIndex]}'.upper()).update({
                f'{datetime.date.today().strftime("%d-%m-%Y")}': "Present"
            })