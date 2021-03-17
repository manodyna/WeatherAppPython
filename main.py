#This is the main method only meant to call the finished methods
#No functions are to be created here unless absolutely necessary
#All assets(images, icons etc) go in the model package
#All controllers and service classes are in the contollers package
#All UI files go in the views package
#No classes are to be created outside these packages in the project root
#Camel case has been used throughout the project unless in json objects
#Most method and variable names are self explanatory

from controllers import WeatherService

# creating objects
# weather = WeatherService.getWeatherArray()
from views.MainView import MainView

coord = WeatherService.getCoord()
main = WeatherService.getWeatherMain()
description = WeatherService.getWeatherDescription()
temp = WeatherService.getTemp()
feelsLike = WeatherService.getFeelslike()
minTemp = WeatherService.getTempMin()
maxTemp = WeatherService.getTempMax()
humidity = WeatherService.getHumidity()
pressure = WeatherService.getPressure()

#forecast objects
forecast = WeatherService.getForecastArray()
dayTemp = WeatherService.getDayTemp()
nightTemp = WeatherService.getNightTemp()
# dayTempFeelsLike = WeatherService.getDayTempFeelsLike()
# nightTempFeelsLike = WeatherService.getNightTempFeelsLike()
# forecastDescription = WeatherService.getDescription()
print(description)
MainView()