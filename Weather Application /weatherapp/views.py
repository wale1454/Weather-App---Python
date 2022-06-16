from django.shortcuts import render

from django.http import HttpResponseRedirect
import requests 

from weatherapp.models import CityName
from weatherapp.forms import NewForm

# Get an API key from https://openweathermap.org/api 
# 

url = "https://api.openweathermap.org/data/2.5/weather?units=metric"

# This weatherFunc() function takes in the city name via the search bar, checks if
#  it's valid, and then send a get request to the API. 
# The API response is then rendered to the HTML template.



def weatherFunc(request):
    formDisplay = NewForm()
    if request.method == 'POST':
        insideForm = NewForm(request.POST)

        if insideForm.is_valid():

            cityInput = insideForm.cleaned_data['contentInside']
            # print(cityInput)

            querystring = {"q":cityInput,
                "appid":"INSERT_API_KEY_HERE"
                }

            r11 = requests.request("GET", url, params=querystring)
            r22 = r11.json()

            # Check for correct input using the status code of the response
            if r22["cod"] == 200:
                insideForm.save()
                print("correct input")
                
                # Collate data to be sent to the HTML template
                data = {
                    "formDisplay": formDisplay,
                    "Temp" : r22["main"]["temp"] ,
                    "City" : r22["name"] ,
                    "Country" : r22["sys"]["country"],
                    "Description" : r22["weather"][0]["main"],
                    "Icon" : r22["weather"][0]["icon"],
                    "humidity" : r22["main"]["humidity"] 
                    }   
            else:
                print("Wrong input! Type in a city name")
                data = { "formDisplay": formDisplay }

    else:
        data = { "formDisplay": formDisplay }

    return render( request, "home.html", data)
