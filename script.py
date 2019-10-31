import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import keyboard
a = ""
# Fetch the service account key JSON file contents
cred = credentials.Certificate('sunny-spots-757b9-firebase-adminsdk-f8pcs-147f19c951.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sunny-spots-757b9.firebaseio.com/'
})
ref = db.reference('/')
ref.set({
        'boxes': 
            {
                'AI DEUS PEGOU MIZERA': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
        })
a = input()
ref = db.reference('boxes')
box_ref = ref.child('box001')
box_ref.update({
    'color': 'blue'
})
a = input()
ref = db.reference('boxes')
ref.push({
    'color': 'purple',
    'width': 7,
    'height': 8,
    'length': 6
})
a = input()