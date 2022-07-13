
import pyttsx3
import speech_recognition as sr
import datetime as d
import time
import winsound
from webbrowser import open
import os
import wikipedia
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

x = d.datetime.now()

def email():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("zeustest275@gmail.com", "********")
    server.sendmail("zeustest275@gmail.com", "kehansenuja@gmail.com", "Project zeus is active")

def auth():
    name = input("Enter Username: ")
    password = input("Enter Password: ")
    if name == "kehan" and password == "LOG":
        beep1()
        print("Welcome")
        speak("welcome sir")
        time.sleep(1)
        print("System Online.....")
        speak("Systems are Online and functional")

    else:
        print("Access Denied")
        speak("Security Protocol Initiated")
        speak("Intruder Alert")
        speak("Intruder Alert")
        beep2()
        beep2()
        exit()


def beep1():
    frequency = 600
    duration = 2000
    winsound.Beep(frequency,duration)

def beep2():
    winsound.Beep(1500, 2000)




def map2():
    place = input('Enter target: ')
    result = wikipedia.summary(place, sentences = 2)
    open("https://earth.google.com/web/search/" + place)
    print(result)


def manifest():
    Soldier = ['Kehan, Jhon, for, Chanaka']
    print("Soldiers On Duty", Soldier)
