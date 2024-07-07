from __future__ import print_function


from Jarvis import JarvisAssistant
import re
import os
import random
import pprint





from plyer import notification
from pygame import mixer
import warnings  # for avoiding warnings
import pyttsx3  # for text to speech
import speech_recognition as sr  # for speech recognition

import os  # portable way to use os dependent functionality
from gtts import gTTS  # google text to speech
import playsound  #

import calendar  # support calander related functions
import datetime
import random

import webbrowser  # it allows to perform websearch
import wikipedia

import ctypes
import winshell

import pyjokes
import subprocess

import smtplib

import json
import requests


import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from twilio.rest import Client

import wolframalpha
from time import sleep

import psutil
import speedtest
from geopy.geocoders import Nominatim
import requests












import requests
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_JarvisUI
from Jarvis.features.login_dialog import LoginDialog
from Jarvis.config import config



from pynput.keyboard import Key,Controller
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



import pywhatkit
import webbrowser
from bs4 import BeautifulSoup
from datetime import timedelta


from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
from playsound import playsound
import time


import pygame
import tempfile
import PyPDF2

# Now you can use PyPDF2 functions and classes


obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello maya", "maya", "wake up maya", "you there maya", "time to work maya", "hey maya",
             "ok maya", "are you there","goood morning","good afternoon", "good evening", "goood night","good"]
GREETINGS_RES = ["always there for you mam", "i am ready mam",
                 "your wish my command", "how can i help you mam?", "i am online and ready mam"]

EMAIL_DIC = {
    'myself': 'emailid@gmail.com',
    'my official email': 'email@gmail.com',
    'my second email': 'emailid@gmail.com',
    'my official mail': 'emailid@gmail.com',
    'my second mail': 'emailid@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =======================================================================================================================================================



engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
#engine.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[1].id)

rate = engine.getProperty("rate")  # getting details of current speaking rate
engine.setProperty("rate", 155)



def speak(text):
    engine.say(text)
    engine.runAndWait()


app_id = config.wolframalpha_id


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry mam I couldn't fetch your question's answer. Please try again ")
        return None
    
def startup():
    speak("Initializing maya")
    speak("Starting all system applications")
    #speak("Installing and checking all drivers")
    #speak("Caliberating and examining all the core processors")
    #speak("Checking the internet connection")
    speak("Wait a moment")
    #speak("All drivers are up and running")
    #speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    #speak(f"Currently it is {c_time}")
    speak("I am Maya. Online and ready . Please tell me how may I help you")
# if __name__ == "__main__":


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."


def get_battery_level():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return percent

def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    return download_speed, upload_speed



    
extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()
    



keyboard = Controller()

def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 0.1), None)

# Function to decrease volume
def decrease_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(0.0, current_volume - 0.1), None)






def sendMessage():
    current_time = datetime.datetime.now()
    current_hours = current_time.hour
    current_minutes = current_time.minute
    new_minutes = current_minutes + 1


    if new_minutes >= 60:
        current_hours += 1
        new_minutes -= 60

    speak("Who do you want to message")
    a = int(input('''Person 1 - 1  Person 2 - 2  : '''))
    if a == 1:
        #speak("Whats the message")
        #message = str(input("Enter the message- "))
        speak("Opening Whats app and sending message")
        pywhatkit.sendwhatmsg("+911234567890","Hello , This Is An Automatic Whatsapp Message Generator Project Which Is Sended Automatically Using Python.",current_hours,new_minutes)
        speak("message sent sucessfull") 
    elif a==2:
        pass







def My_Location():
    import webbrowser as web 
    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"Mam , You Are Now In {state , country} .")


def translate_to_hindi(text):
    translator = Translator()
    
    try:
        translation = translator.translate(text, dest='hi')  # 'hi' is the language code for Hindi
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None



def speak_text(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        temp_file.close()
        os.unlink(temp_file.name)
    except Exception as e:
        print(f"Text-to-speech error: {e}")

#PDF reader
def pdf_reader(self):
        speak("enter the name of the book which you want to read")
        n = "material"
        n = n.strip()+".pdf"
        book_n = open(n,'rb')
        pdfReader = PyPDF2.PdfFileReader(book_n)
        pages = pdfReader.numPages
        speak(f"Boss there are total of {pages} in this book")
        speak("plsase enter the page number Which I nedd to read")
        num = int(input("Enter the page number: "))
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        speak(text)



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        wish()

        while True:
            command = obj.mic_input()

            if "date" in command or "month" in command:
                date = today_date()
                print(date)
                speak(date)
            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(time_c)

            elif "read material" in command:
                pdf_reader(self)


                speak(f"Mam the time is {time_c}")
            elif "wish judges" in command or "wish the judges" in command or "judges" in command:
                speak("Good afternoon, sir or mam. I'm Maya, a personal voice assistant designed by Rushitha and team  Today, I'm delighted to introduce myself to you. I can perform many tasks with just a simple voice command, making your life more comfortable and efficient. How can I assist you today?")
            elif "wish my friends" in command or "friends" in command:
                speak("Hey there, everyone! I'm Maya, personal voice assistant. It's awesome to be here with all you amazing students today. I'm here to make your lives easier by doing some of cool stuff with just a simple voice command.")




            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))
                
            elif "who are you" in command or "define yourself" in command:
                speak("Hello, Mam I am an Assistant. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera")
                #talk(speak)
            elif "made you" in command or "created you" in command:
                speak("I was created by Rushitha Gudipudi")
                #talk(speak)
            elif "your name" in command or "name" in command:
                speak("My name is Maya , I am personal voice Assistant")
                #talk(speak) 
            elif "who am i" in command:
                speak("You must probably be a human")
                #talk(speak)  
            elif "why do you exist" in command or "why did you come to this word" in command:
                speak("It is a secret")
                #talk(speak)
            elif "how are you" in command:
                speak("I am awesome, Thank you")
                speak("\nHow are you?")
                #talk(speak)
            elif "fine" in command or "good" in command:
                speak("It's good to know that your fine")
                #talk(speak)



    
                
            elif "open" in command.lower() or "launch" in command.lower():
                if "chrome" in command.lower():
                    speak("Opening Google Chrome mam")
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

                elif "word" in command.lower():
                    speak("Opening Microsoft Word mam")
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in command.lower():
                    speak("Opening Microsoft Excel mam")
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                    )
                
                elif "ppt" in command.lower():
                    speak("Opening Power Point Presentation mam")
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                    )    

                elif "vs code" in command.lower():
                    speak("Opening Visual Studio Code mam")
                    os.startfile(
                        r"C:\Users\RUSHITHA\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

               

                elif "google" in command.lower():
                    speak("Opening Google mam\n")
                    webbrowser.open("https://google.com/")

                elif "stack overflow" in command.lower():
                    speak("Opening StackOverFlow mam")
                    webbrowser.open("https://stackoverflow.com/")
                    
                elif re.search('open', command):
                    domain = command.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    speak(f'Alright mam !! Opening {domain}')
                    print(open_result)

                else:
                    speak("Application not available mam")
                    
            elif "wikipedia" in command or "Wikipedia" in command or "tell me about" in command or "who is" in command:
                command = command.replace("maya", "")
                wiki = wikipedia.summary(command, sentences = 2)               
                speak(wiki)





            elif "youtube" in command.lower():
                ind = command.lower().split().index("youtube")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                #pywhatkit.playonyt(search)
                r = "Opening " + str(search) + " on youtube mam"
                speak(r)
                
            elif "search" in command.lower():
                ind = command.lower().split().index("search")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                r = "Searching " + str(search) + " on google mam"
                speak(r)
                
            elif "google" in command.lower():
                ind = command.lower().split().index("google")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                r= "Searching " + str(search) + " on google mam"
                speak(r)





            elif "change background" in command or "change wallpaper" in command or "background" in command or "wallpaper" in command:
                
                img = r"C:\Users\RUSHITHA\Downloads\JARVIS-master\JARVIS-master\wallpapers"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak("Background changed successfully mam")

            elif "play music" in command or "play song" in command or "hit some music" in command or "music" in command:
                speak("Here you go with music mam")
                music_dir = r"C:\Users\RUSHITHA\Downloads\JARVIS-master\JARVIS-master\music"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

            elif "empty recycle bin" in command or "recycle bin" in command:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak("Recycle Bin Emptied mam")
                
            elif "joke" in command or "jokes" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

                




            elif "battery" in command and "level" in command or "check battery level" in command:
                battery_level = get_battery_level()
                r = "The current battery level is "+ str(battery_level) + "percent."
                speak(r)
                    
            elif "internet speed" in command or "speed test" in command or "internet" in command:
                speak("Checking Internet speed , please wait a moment ")
                download, upload = check_internet_speed()
                r = "Download speed: "+str(download)
                speak(r)
                r = "Upload speed: "+ str(upload)
                speak(r)

            elif "make a note" in command or "write this down" in command or "remember this" in command or "write" in command:
                speak("What would you like me to write down mam?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that mam")

            elif "close the note" in command or "close notepad" in command or "close" in command or "close notes" in command:
                speak("Okay mam, closing notepad")
                os.system("taskkill /f /im notepad.exe")


                

            elif 'my location' in command:
                My_Location()

            elif "where is" in command or "location" in command or "Google maps" in command:
                ind = command.lower().split().index("is")
                location = command.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                r = "This is where " + str(location) + " is."
                speak(r)
                webbrowser.open(url)

            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                speak(weather_res)

            elif "buzzing" in command or "news" in command or "headlines" in command or "read news" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('mam Todays Headlines are..')
                url = (
                    "http://newsapi.org/v2/top-headlines?"
                    "country=in&"
                    "apiKey="
                )
                try:
                    response = requests.get(url)
                except:
                    speak("Please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    speak(str(new["title"]))
                    engine.runAndWait()

                    #print(str(new["description"]), "\n")
                    #speak(str(new["description"]))
                    sleep(2)
                speak('These were the top headlines, Have a nice day Mam!!..')


            





            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    #speak("Whom do you want to email sir ?")
                    #recipient = obj.mic_input()
                    recipient = "myself"
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:
                        print(sender_email)
                        print(sender_password)
                        speak("What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(sender_email, sender_password,
                                      receiver_email, msg)
                        speak("Email has been successfully sent")
                        sleep(2)

                    else:
                        speak(
                            "I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    speak("Sorry mam. Couldn't send your mail. Please try again")






            elif "system status" in command or "cpu storage" in command or "disk storage" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)
                
            elif "calculate" in command or "what is" in command:
                 query = command
                 answer = computational_intelligence(query)
                 speak(answer)

            elif "switch the window" in command or "switch window" in command or "minimize window" in command or "switch tab" in command or "switch the tab" in command or "change window" in command:
                speak("Okay mam, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyUp("alt")
                
            elif "ip address" in command or"ip" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")






            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command or "click screenshot" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright mam, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured mam")

            elif "show me the screenshot" in command or "show screenshot" in command or "show the screenshot" in command:
                try:
                    img_path = r'C:\Users\RUSHITHA\Downloads\JARVIS-master\JARVIS-master\\' + name
                    img = Image.open(img_path)
                    img.show()
                    speak("Here it is mam")
                    sleep(2)

                except IOError:
                    speak("Sorry mam, I am unable to display the screenshot")
                    
            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak("Sorry mam, I coundn't fetch your current location. Please try again")


            elif "send sms message" in command or "send the sms message" in command:
                account_sid = ""
                auth_token = ""
                client = Client(account_sid, auth_token)


                speak("What should i send as message")
                message = client.messages.create(
                    body=obj.mic_input(), from_="+17622206524", to="+911234567890"
                )

                print(message.sid)
                speak("Message sent successfully mam")

                


            elif "hide all files" in command or "hide this folder" in command or"hide files" in command or "hide all the files" in command:
                os.system("attrib +h /s /d")
                speak("Mam, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command or "show files" in command:
                os.system("attrib -h /s /d")
                speak("Mam, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")


            
            elif "don't listen" in command or "stop listening" in command or "do not listen" in command or "go to sleep" in command:
                speak("for how many seconds do you want me to sleep mam")
                a = int(obj.mic_input())
                #talk(a)
                sleep(a)
                r= str(a) + " seconds completed. Now you can ask me anything"
                speak(r)
                
            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright mam, going offline. It was nice working with you")
                sys.exit()

            elif "pause" in command:
                pyautogui.press("k")
                speak("video paused")

            elif "play" in command:
                pyautogui.press("k")
                speak("video played")

            elif "mute" in command:
                pyautogui.press("m")
                speak("video muted")

            elif "increase volume" in command:
               
                speak("Turning volume up,sir")
                increase_volume()

            elif "decrease volume" in command:
                
                speak("Turning volume down, sir")
                decrease_volume()

            elif "set an alarm" in command or "alarm" in command:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                alarm(a)
                speak("Done,mam")


            elif "schedule my day" in command:
                tasks = [] #Empty list
                speak("Do you want to clear old tasks")
                query = obj.mic_input()
                query = query.lower()
                if "yes" in query:
                    file = open("tasks.txt","w")
                    file.write(f"")
                    file.close()
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    i = 0
                    for i in range(no_tasks):
                        speak("Say the task ")
                        speak(i+1)   
                        z = obj.mic_input()
                        tasks.append(z)
                        file = open("tasks.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                elif "no" in query:
                    i = 0
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task :- "))
                        file = open("tasks.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                speak("Scheduled Sucessfully")




            elif "show my schedule" in command or "show schedule" in command or"show the schedule" in command:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                print("Notification Content:", content)
                mixer.init()
                mixer.music.load(r"C:\Users\RUSHITHA\Downloads\JARVIS-master\JARVIS-master\notification.wav")
                mixer.music.play()
                notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 100
                )


            elif "whatsapp" in command:
                sendMessage()


            elif "click my photo" in command or "click photo" in command:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")




            elif "translate" in command:
                speak("Give the English sentence which you wants to translate")
                english_text = obj.mic_input()
                hindi_translation = translate_to_hindi(english_text)
                if hindi_translation:
                    speak("Translation to Hindi is")
                    print(hindi_translation)
                    speak_text(hindi_translation, lang='hi')


startExecution = MainThread()

class Main(QMainWindow):
    cpath =""
    
    def __init__(self, path):
        self.cpath = path
        super().__init__()

        # Create an instance of the LoginDialog
        self.login_dialog = LoginDialog()

        # Connect the login button in LoginDialog to show_main_window method
        self.login_dialog.login_button.clicked.connect(self.show_main_window)

        # Show the login dialog when the Main window is created
        self.login_dialog.show()

    def show_main_window(self):
        result =  self.login_dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            if not hasattr(self, 'ui'):
                self.ui = Ui_JarvisUI(path=self.cpath)
                self.ui.setupUi(self)
                self.ui.pushButton_4.clicked.connect(self.startTask)
                self.ui.pushButton_3.clicked.connect(self.close)
        self.show()



    #NOTE make sure to place a correct path where you are keeping this gifs
    def startTask(self):
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ringJar.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\lines1.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3_flipped.gif")
        self.ui.label_16.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\Sujith.gif")
        self.ui.label_17.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
if __name__ == "__main__":
    current_path = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    jarvis = Main(path=current_path)
    
    exit(app.exec_())





