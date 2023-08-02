import cv2
import face_recognition
import pickle
import os
# import gspread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("YOUR FIREBASE API-KEY")
firebase_admin.initialize_app(cred, {
    'storageBucket': "YOUR STORAGE BUCKET URL"
})


# gc = gspread.service_account(filename="GSPREAD API-KEY")
# wks = gc.open("YOUR FILE NAME").sheet1

folder = 'images'
pathlist = os.listdir(folder)
imglist = []
ID = []
for path in pathlist:
    imglist.append(cv2.imread(os.path.join(folder, path)))
    ID.append(os.path.splitext(path)[0])
    filename = f'{folder}/{path}'
    bucket = storage.bucket()
    bucket.blob(filename).upload_from_filename(filename)
# j = 1
# for i in range(0, len(ID)):
#     wks.update(f"A{j}", ID[i])
#     wks.update(f"B{j}", "ABSENT")
#     j += 1


def encoding(img):
    lst = []
    for l in img:
        l = cv2.cvtColor(l, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(l)[0]
        lst.append(encode)
    return lst


elk = encoding(imglist)
elkID = [elk, ID]
file = open("EncodeFile.p", 'wb')
pickle.dump(elkID, file)
file.close()
