#This is the weather service class to call the current weather data API and retrive its contents
import json
import requests

#from MainView import *
#package requests might have to installed seperatly in your local project.
#PyCharm will handle it automatically if you use PyCharm.

#bangalore has been passed as the city for testing only, the city selection functionality shoud be added during frontend dev
#current data
#temp refers to temperature
#coodr refers to coordinate
#resuts refers to the weather array
#appid is the api key and is to be kept private

#city = "bangalore"



class WeatherService():

    def __init__(self,location):
        self.location=location

    def getWeatherArray(self):
        __appid__ = "6c4a66dafb7d9f1fd2610e07e9396331"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+self.location+"&appid="+__appid__ + "&units=metric"
        response = requests.post(url)
        response.raise_for_status()

        results = response.json()
        return results

# from views.MainView import MainView
# var = MainView.city



weatherServiceArray = WeatherService("london")
weatherArray = weatherServiceArray.getWeatherArray()

def getCoord():
    results = weatherArray
    coord = results['coord']
    return coord

def getWeatherMain():
    results = weatherArray
    return (results['weather'][0]['main'])

def getWeatherDescription():
    results = weatherArray
    return (results['weather'][0]['description'])

def getTemp():
    results = weatherArray
    return (results['main']['temp'])

def getFeelslike():
    results = weatherArray
    return (results['main']['feels_like'])

def getTempMin():
    results = weatherArray
    return (results['main']['temp_min'])

def getTempMax():
    results = weatherArray
    return (results['main']['temp_max'])

def getPressure():
    results = weatherArray
    return (results['main']['pressure'])

def getHumidity():
    results = weatherArray
    return (results['main']['humidity'])

def getLat():
    results = weatherArray
    return (results['coord']['lat'])

def getLon():
    results = weatherArray
    return (results['coord']['lon'])

lat = str(getLat())
lon = str(getLon())

def getForecastArray():
    __appid = "6c4a66dafb7d9f1fd2610e07e9396331"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=hourly,current,minutely&appid="+__appid+"&units=metric"
    response = requests.post(url)
    response.raise_for_status()

    results = response.json()
    return results()

def getDayTemp():
    results = getForecastArray()
    dayTemp= []
    for i in range (7):
        dayTemp.append(results['daily'][i]['temp']['day'])
    return dayTemp

def getNightTemp():
    results = getForecastArray()
    nightTemp= []
    for i in range (7):
        nightTemp.append(results['daily'][i]['temp']['night'])
    return nightTemp

    # def getNightTempFeelsLike():
    #     results = getForecastArray()
    #     nightTempFeelsLike = []
    #     for i in range (7):
    #         nightTempFeelsLike.append(results['daily'][i]['feels_like']['temp']['night'])
    #     return nightTempFeelsLike
    #
    # def getDayTempFeelsLike():
    #     results = getForecastArray()
    #     dayTempFeelsLike = []
    #     for i in range (7):
    #         dayTempFeelsLike.append(results['daily'][i]['feels_like']['temp']['day'])
    #     return dayTempFeelsLike

    # def getDescription():
    #     results = getForecastArray()
    #     description = []
    #     for i in range (7):
    #         description.append(results['current']['weather'][0]['description'])