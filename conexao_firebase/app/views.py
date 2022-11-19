from django.shortcuts import render , HttpResponse

# Create your views here.
def resultado(request):
    return render(request , 'indice.html')

import pyrebase 
  
config = {
  apiKey: "AIzaSyBu4u2uEZU6OzNBk8Qp5v6rrSMmQnsoVj8",
  authDomain: "projeto-ifpi-dc359.firebaseapp.com",
  projectId: "projeto-ifpi-dc359",
  storageBucket: "projeto-ifpi-dc359.appspot.com",
  messagingSenderId: "862447392576",
  appId: "1:862447392576:web:37484c2dbcf195b80ecca5"
};
firebase=pyrebase.initialize_app(config) 
authe = firebase.auth() 
database=firebase.database() 
  
def home(request): 
    day = database.child('Data').child('Day').get().val() 
    id = database.child('Data').child('Id').get().val() 
    projectname = database.child('Data').child('Projectname').get().val() 
    return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })