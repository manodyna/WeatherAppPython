from tkinter import *
import requests
import json 
import datetime 
from PIL import ImageTk, Image
import datetime
  
# necessary details

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



class MainView():

    root = Tk()
    root.title("Weather App")
    root.geometry("750x1050")
    root['background'] = "white"

    #Exit button
    exit_button = Button(root,text="Exit", command=root.destroy)
    exit_button.place(x=350,y=580)

    #Date
    dt = datetime.datetime.now()
    date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
    date.place(x=500, y=70)
    month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
    month.place(x=595, y=70)

    #Time
    hour = Label(root, text=dt.strftime('%I : %M %p'),
                 bg='white', font=("", 15))
    hour.place(x=500, y=100)


    # Theme for the respective time the application is used
    # if int((dt.strftime('%I'))) >=18 and int((dt.strftime('%I')))<=5 :
    #     img = ImageTk.PhotoImage(Image.open('moon.jpg'))
    #     panel = Label(root, image=img)
    #     panel.place(x=475, y=150)
    # else:
    #     img = ImageTk.PhotoImage(Image.open('sun.png'))
    #     panel = Label(root, image=img)
    #     panel.place(x=475, y=150)
    #
    #
    # #Cities
    city_name = StringVar()
    city_entry = Entry(root, textvariable=city_name, width=50)
    city_entry.insert(0, "Enter the city")
    city_entry.place(x=5, y=70,height=40)
    city = city_name


    #Button
    city_nameButton = Button(root, text="Search",command=city)
    city_nameButton.place(x=267,y=70)



    #Title
    Title = Label(root , text = "Weather Report Generator",width=0,
                         bg='yellow',font=("algerian",25))
    Title.place(x=130, y=10)

    #Coordinates

    from controllers.WeatherService import getPressure, getHumidity, getTempMax, getTempMin, getFeelslike, getTemp, \
        getWeatherDescription, getWeatherMain, getCoord, lat, lon, getDayTemp, getNightTemp

    coord = Label(root, text="Coordinates: ", width=0,
                       bg='white', font=("bold", 15))
    coord.place(x=20, y=140)
    lable_coord = Label(root, text="...", width=0,
                           bg='white', font=("bold", 15))
    lable_coord.place(x=140, y=140)

    longitude= Label(root, text="...", width=0,
                          bg='white', font=("bold", 13))
    longitude.place(x=115, y=170)

    latitude = Label(root, text="...", width=0,
                      bg='white', font=("bold", 13))
    latitude.place(x=25, y=170)

    # Current Temperature

    lable_temp = Label(root, text="...", width=0,
                           bg='white', font=("bold",80))
    lable_temp.place(x=30, y=200)
    # Other temperature details

    humi = Label(root, text="Humidity: ", width=0,
                 bg='white', font=("bold", 15))
    humi.place(x=20, y=465)

    lable_humidity = Label(root, text="...", width=0,
                           bg='white', font=("bold", 15))
    lable_humidity.place(x=110, y=465)


    maxi = Label(root, text="Max.Temperature: ", width=0,
                 bg='white', font=("bold", 15))
    maxi.place(x=20, y=435)

    max_temp = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    max_temp.place(x=190, y=435)


    mini = Label(root, text="Min.Temperature: ", width=0,
                 bg='white', font=("bold", 15))
    mini.place(x=20, y=405)

    min_temp = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    min_temp.place(x=185, y=405)


    day= Label(root, text="Day Temperature: ", width=0,
                 bg='white', font=("bold", 15))
    day.place(x=20, y=495)

    day_temp = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    day_temp.place(x=190, y=495)

    night= Label(root, text="Night Temperature: ", width=0,
                 bg='white', font=("bold", 15))
    night.place(x=20, y=525)

    night_temp = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    night_temp.place(x=195, y=525)

    #DESCRIPTION

    weather_Main = Label(root, text="...",width=0,
                     bg='white', font=("bold", 15))
    weather_Main.place(x=25, y=315)

    weather_Descrip = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    weather_Descrip.place(x=25, y=375)

    pres= Label(root, text="Pressure: ", width=0,
                 bg='white', font=("bold", 15))
    pres.place(x=20, y=555)

    pressure = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    pressure.place(x=115, y=555)

    feels_like = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
    feels_like.place(x=25, y=345)

    lable_coord.configure(text=getCoord())
    weather_Main.configure(text=getWeatherMain())
    weather_Descrip.configure(text=getWeatherDescription())
    lable_temp.configure(text=getTemp())
    feels_like.configure(text=getFeelslike())
    min_temp.configure(text=getTempMin())
    max_temp.configure(text=getTempMax())
    pressure.configure(text= getPressure())
    lable_humidity.configure(text=getHumidity())
    latitude.configure(text=lat)
    longitude.configure(text=lon)
    # day_temp.configure(text=getDayTemp())
    # night_temp.configure(text=getNightTemp())
    #night_temp_feels.configure(text=getNightTempFeelsLike())
    #day_temp_feels.configure(text=getDayTempFeelsLike())
    #description.configure(text=getDescription())

    root.mainloop()

