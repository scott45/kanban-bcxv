__author__ = 'Scott Businge'

import pyrebase

  config = {
    apiKey: "AIzaSyAKaB1kkbIAOtcgdAD-b0LiGFPML_j0qgQ",
    authDomain: "scott-kanban.firebaseapp.com",
    databaseURL: "https://scott-kanban.firebaseio.com",
    storageBucket: "scott-kanban.appspot.com",
    messagingSenderId: "324938064474"
          };
  firebase = pyrebase.initialize_app(config);