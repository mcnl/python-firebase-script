import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import keyboard
import time
import random

# Fetch the service account key JSON file contents
cred = credentials.Certificate('sunny-spots-757b9-firebase-adminsdk-f8pcs-147f19c951.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sunny-spots-757b9.firebaseio.com/'
})
ref = db.reference('/')
ref.set({
	'device-1':{
        'reads':{},
        'readnow':{
        	'inclination':-1,
        	'rotacion':-1,
        	'lums':-1,
        	'gps':[0,0],
        	'power': -1,
        	'charge': -1
        }
	}
})
print("Sending Stuff to Firebase")
while(1):

	device = db.reference('device-1')
	leitura = device.child('reads')
	leitura_agr = device.child('readnow')
	leit = {
		'inclination':random.randint(0, 180) ,
		'rotacion':random.randint(0, 360) ,
		'lums':random.randint(0, 10) ,
		'gps':[random.randint(0, 180) ,random.randint(-90, 90) ],
		'power': random.randint(0, 12) ,
		'charge': random.randint(0, 100) 
	}
	leitura_agr.update(leit)
	leitura.push(leit)
	print("Sended!")
	time.sleep(5.0)
