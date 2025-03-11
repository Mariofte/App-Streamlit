import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCY8Y1DBxnSIEvkS1PQIi2NTRI_zMUdcV8",
    "authDomain": "scoutingapp2025frc.firebaseapp.com",
    "databaseURL": "https://scoutingapp2025frc-default-rtdb.firebaseio.com",
    "projectId": "scoutingapp2025frc",
    "storageBucket": "scoutingapp2025frc.firebasestorage.app",
    "messagingSenderId": "49672242717",
    "appId": "1:49672242717:web:93f0320d40764d0519a8f4"
}

if not firebase_admin._apps:
    cred = credentials.Certificate("Toekn.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()