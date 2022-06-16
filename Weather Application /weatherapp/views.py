from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
import requests 

from weatherapp.models import CityName

#
# Get an API key from https://openweathermap.org/api 
#




# Create your views here.

url = "https://api.openweathermap.org/data/2.5/weather?units=metric"


# The inputFunc() funtion receives the input and saves it to the db.

def inputFunc(request):
    ksio = request.POST['userinput1']

    newEntry = CityName(contentInside=(ksio))
    newEntry.save()

    return HttpResponseRedirect('/')


def htmlfile(request):

    indexNo = len(CityName.objects.all())

    TheCity = CityName.objects.all()[indexNo -1].contentInside



    querystring = {"q":TheCity,
                "appid":"INSERT_API_KEY_HERE"
                }

    r11 = requests.request("GET", url, params=querystring)
    r22 = r11.json()

    data = {
    "Temp" : r22["main"]["temp"] ,
    "City" : r22["name"] ,
    "Country" : r22["sys"]["country"],
    "Description" : r22["weather"][0]["main"],
    "Icon" : r22["weather"][0]["icon"],
    "humidity" : r22["main"]["humidity"] 

    }   
    
    return render( request, "home.html", data)



