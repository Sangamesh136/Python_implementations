from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Colors
login_bg = "#caf0ff"
login_text = "black"
login_bg2 = "#fff"

global bgr
bgr = "#fff"
dashboard_txt = "#1e1e1e" # same for Clouds clear rainy snow

login = Tk()
login.title("Authentication Window")
login.geometry("500x400+500+200")
login.resizable(False, False)
login.config(bg=login_bg)

def logUser():
    user = username.get()
    pwd = password.get()
    if user != "demo" or pwd != "demo":
        messagebox.showwarning("Login Error", "Invalid username or password")
        username.delete(0, tk.END)
        password.delete(0, tk.END)
    else:
        login.destroy()
        root = Tk()
        root.title("WeatherVerse")
        root.geometry("900x500+300+200")
        root.resizable(False, False)
        root.config(bg=bgr)

        def getWeather():
            city = textfield.get()
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f733af53d79626f7924e4e19640924cb"
            json_data = requests.get(api).json()
            if json_data['cod'] != 200:
                messagebox.showerror("Error", "Location does not exist!")
                return

            condition_data = json_data['weather'][0]['main']
            description_data = json_data['weather'][0]['description']
            temp_data = int(json_data['main']['temp'] - 273.15)
            pressure_data = json_data['main']['pressure']
            humidity_data = json_data['main']['humidity']
            wind_speed_data = json_data['wind']["speed"]
            
            if condition_data == "Clouds":
                global bgr
                bgr = "#9BBEC8"
            elif condition_data == "Clear":
                bgr = "#E0F4FF"      
            elif condition_data == "Rain":
                bgr = "#83c9ff"
            elif condition_data == "Snow":
                bgr = "#d1d7df"       
            else:
                bgr = "#fff"

            root.config(bg=bgr)
            name.config(bg=bgr)
            label1.config(bg = bgr)
            label2.config(bg=bgr)
            label3.config(bg=bgr)
            label4.config(bg=bgr)
            cityWdg.config(text=city, bg=bgr)
            temp.config(text=str(temp_data) + "°" + "C", bg=bgr)
            condition.config(text=condition_data + " | Feels Like " + str(temp_data) + "°" + "C", bg=bgr)
            wind.config(text=str(wind_speed_data), bg=bgr)
            humidity.config(text=str(humidity_data) + "%", bg=bgr)
            description.config(text=description_data, bg=bgr)
            pressure.config(text=str(pressure_data), bg=bgr)

        # Search Area

        textfield = Entry(justify="center", width=17, font=("poppins", 25, "bold"), bg="#cdcdcd", border=0, fg=dashboard_txt)
        textfield.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        textfield.focus()

        search = Button(text="Fetch", font=("cursive", 10, "bold"), height=1, width=6, cursor="hand2", padx=5, pady=5,
                        bg="#b0adb8", fg="#170056", command=getWeather)
        search.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Middle Left box

        name = Label(text="Current Weather", font=("cursive", 15, "bold"), fg=dashboard_txt, bg=bgr)
        name.place(x=130, y=200)
        cityWdg = Label(text="---",font=("cursive", 15), fg=dashboard_txt, bg=bgr)
        cityWdg.place(x=130, y=230)

        # Middle right box

        temp = Label(text="---", font=("arial", 70, "bold"), fg=dashboard_txt, bg=bgr)
        temp.place(x=550, y=150)
        condition = Label(text="---", font=("arial", 15, 'bold'),  fg=dashboard_txt, bg=bgr)
        condition.place(x=550, y=250)

        # Bottom most two rows
        # Upper Row
        label1 = Label(text="WIND", font=("Helvetica", 15, 'bold'), fg=dashboard_txt, bg=bgr)
        label1.place(x=120, y=350)
        label2 = Label(text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg=dashboard_txt, bg=bgr)
        label2.place(x=250, y=350)
        label3 = Label(text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg=dashboard_txt, bg=bgr)
        label3.place(x=430, y=350)
        label4 = Label(text="PRESSURE", font=("Helvetica", 15, 'bold'), fg=dashboard_txt, bg=bgr)
        label4.place(x=650, y=350)

        # Bottom row
        wind = Label(text="...", font=("arial", 20, "bold"), fg=dashboard_txt, bg=bgr)
        wind.place(x=120, y=400)
        humidity = Label(text="...", font=("arial", 20, "bold"), fg=dashboard_txt, bg=bgr)
        humidity.place(x=280, y=400)
        description = Label(text="...", font=("arial", 15, "bold"), fg=dashboard_txt, bg=bgr)
        description.place(x=450, y=400)
        pressure = Label(text="...", font=("arial", 20, "bold"), fg=dashboard_txt, bg=bgr)
        pressure.place(x=670, y=400)

        root.mainloop()

title = Label(login, text="Login", font=("poppins", 40, "bold"), bg=login_bg, fg=login_text)
title.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

unameLabel = Label(login, text="Username ", font=("poppins", 20), bg=login_bg, fg=login_text)
unameLabel.place(x=40, rely=0.3)
username = Entry(width=15, font=("poppins", 20), bg=login_bg2)
username.place(x=190, rely=0.3)

passwordLabel = Label(login, text="Password ", font=("poppins", 20), bg=login_bg, fg=login_text)
passwordLabel.place(x=40, rely=0.45)
password = Entry(login, width=15, font=("poppins", 20), bg=login_bg2, show="•")
password.place(x=190, rely=0.45)

loginButton = Button(login, text="Login", padx=2, pady=2, font=("poppins", 15, "bold"), command=logUser)
loginButton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

creds = Label(login, text="Designed by PyPros", pady=10, bg=login_bg, fg=login_text)
creds.pack(side="bottom")

login.mainloop()