import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDQ1uwMF0E8xVU0Iu-kENoQwE5Ihtr5TxE",
    "databaseURL":"https://cpanda-firebase-test-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "authDomain": "cpanda-firebase-test.firebaseapp.com",
    "projectId": "cpanda-firebase-test",
    "storageBucket": "cpanda-firebase-test.appspot.com",
    "messagingSenderId": "325967061721",
    "appId": "1:325967061721:web:d513aaf05f1e99c7ee14c8",
    "measurementId": "G-FBGX5DH0CB"
  }

firebase=pyrebase.initialize_app(firebaseConfig)

firebase_db=firebase.database()
firebase_db.child("-MbQ4GWVTLHlI8318WLe").remove()
