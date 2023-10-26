import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('treatment-97281-firebase-adminsdk-ba112-c7823d2208.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://treatment-97281-default-rtdb.firebaseio.com"
})

ref = db.reference('/test')
print(ref.get())
#
# users_ref = ref.child('users')
# users_ref.set({
#     'alanisawesome': {
#         'date_of_birth': 'June 23, 1912',
#         'full_name': 'Alan Turing'
#     },
#     'gracehop': {
#         'date_of_birth': 'December 9, 1906',
#         'full_name': 'Grace Hopper'
#     }
# })

# posts_ref = ref.child('posts')
vari = "Chinmoy"
tit = "mondal"

ref.push().set({
    'author': vari,
    'title': tit
})
