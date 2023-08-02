import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("FIREBASE API-KEY")
firebase_admin.initialize_app(cred, {
    'databaseURL': "FIREBASE DATABASE URL"
})

ref = db.reference("Students")
data = {
    "REGESTRATION NUMBER":
        {
            "Name": "NAME"
        }
}
for key,values in data.items():
    ref.child(key).set(values)
