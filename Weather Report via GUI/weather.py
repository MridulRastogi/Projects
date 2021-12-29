from bs4 import BeautifulSoup
import requests
import tkinter as tk
from PIL import Image, ImageTk

def weather(city):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city = city.replace(" ", "+")
    res  = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    soup          = BeautifulSoup(res.text, 'html.parser')
    
    location      = soup.select('#wob_loc')[0].getText().strip()
    time          = soup.select('#wob_dts')[0].getText().strip()
    weather       = soup.select('#wob_dc') [0].getText().strip()
    temperature   = soup.select('#wob_tm') [0].getText().strip() + '°C'
    precipitation = soup.select('#wob_pp') [0].getText().strip()
    humidity      = soup.select('#wob_hm') [0].getText().strip()
    wind          = soup.select('#wob_ws') [0].getText().strip()
    
    LOCATION.delete('1.0', 'end')
    TIME.delete('1.0', 'end')
    WEATHER.delete('1.0', 'end')
    TEMPERATURE.delete('1.0', 'end')
    PRECIPITATION.delete('1.0', 'end')
    HUMIDITY.delete('1.0', 'end')
    WIND.delete('1.0', 'end')

    LOCATION.insert(tk.END, location)
    TIME.insert(tk.END, time)
    WEATHER.insert(tk.END, weather)
    TEMPERATURE.insert(tk.END, temperature)
    PRECIPITATION.insert(tk.END, precipitation)
    HUMIDITY.insert(tk.END, humidity)
    WIND.insert(tk.END, wind)
    
    print("Location: ",location)
    print("Time: ",time)
    print("Weather: ",weather)
    print("Temperature: ",temperature+"°C")
    print("Precipitation: ",precipitation)    
    print("Humidity: ",humidity)    
    print("Wind: ",wind)
    
def getInput():
    city = LOC.get(1.0, "end-1c")
    city = city + ' Weather'
    weather(city)
    
root = tk.Tk()
root.geometry("400x350")
root.configure(bg="Black")
root.title("Weather Report")

'''
load = Image.open('D:/Python Codes/Python/Softwares/Weather/weather_forecast_2.jfif')
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.place(x=225, y=225, width=290, height=150)
'''

IT = tk.Text( root, font=("Bahnschrift SemiBold",20,'bold'), fg="black", bg="blue")
IT.pack()
IT.place(x=100, y=10, height=40, width=200)
IT.insert(tk.END,'Weather Report')

ELOC = tk.Text( root, font=("Berlin Sans FB",14), bg="white", fg="black")
ELOC.place(x=25, y=60, height=25, width=130)
ELOC.insert(tk.END,"Enter Location:")

LOC = tk.Text(root, font=("Berlin Sans FB",16), bg="white", fg="black")
LOC.place(x=160, y=60, height=25, width=200)

SHOW = tk.Button(root,text="Show Weather Report",font=("Comic Sans MS",12),fg="black",bg="light green", command=getInput)
SHOW.place(x=160,y=90,height=25,width=165)

############################################################################### HERE BEGINS THE INFORMATION BOXES

L = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
L.place(x=60,y=125,height=25,width=75)
L.insert(tk.END, 'Location:')
LOCATION = tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
LOCATION.place(x=140,y=125,height=25,width=240)

T = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
T.place(x=85,y=155,height=25,width=50)
T.insert(tk.END, 'Time:')
TIME = tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
TIME.place(x=140,y=155,height=25,width=180)

WE = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
WE.place(x=50,y=185,height=25,width=85)
WE.insert(tk.END, 'Weather:')
WEATHER = tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
WEATHER.place(x=140,y=185,height=25,width=180)

T = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
T.place(x=23,y=215,height=25,width=112)
T.insert(tk.END, 'Temperature:')
TEMPERATURE = tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
TEMPERATURE.place(x=140,y=215,height=25,width=50)

P = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
P.place(x=27,y=245,height=25,width=108)
P.insert(tk.END, 'Precipitation:')
PRECIPITATION= tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
PRECIPITATION.place(x=140,y=245,height=25,width=50)

H = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
H.place(x=55,y=275,height=25,width=80)
H.insert(tk.END, 'Humidity:')
HUMIDITY= tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
HUMIDITY.place(x=140,y=275,height=25,width=50)

WI = tk.Text(root, font=('Comic Sans MS',12,'bold'), fg='black', bg='white')
WI.place(x=85,y=305,height=25,width=50)
WI.insert(tk.END, 'Wind:')
WIND = tk.Text(root, font=("Comic Sans MS",12), fg='white', bg='black')
WIND.place(x=140,y=305,height=25,width=70)

root.mainloop()