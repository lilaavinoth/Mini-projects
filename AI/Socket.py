import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate('firebase-json.json')

firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://my-ai-81afb.firebaseio.com/'
})

# Upload
def upl():
            ref = db.reference('/')
            (ref.set({
                'My input':
                    {
                        'input':'updatee from puthopn'
                    }
            }))

#upl()

# Retrieve
def ret():
    ref2 = ''
    while True:
            ref = db.reference('My input/input')
            ref1 = ref.get()
            if ref1 != ref2:
                print(ref1)
            ref2 = ref1


ret()