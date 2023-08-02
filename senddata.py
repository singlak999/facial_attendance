import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("k.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://crack-celerity-393115-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")
data = {
    "21BCE8114":
        {
            "Name": "Krishna"
        }
}
for key,values in data.items():
    ref.child(key).set(values)