import csv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('treatment-97281-firebase-adminsdk-ba112-c7823d2208.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://treatment-97281-default-rtdb.firebaseio.com"
})

ref = db.reference('/batch')

with open('ICT Alumni Database - 2015-16.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ref.push().set({
            'Name': row['Name'],
            'Hall': row['Hall'],
            'Roll': row["Roll"],
            'Reg': row["Reg"],
            'Phone': "",
            'Email': "",
            'Linkedin': "",
            'Session': "2015-16"
        })

print(row)
