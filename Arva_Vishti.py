from posixpath import pathsep
import pyttsx3
import speech_recognition as sr
import datetime as dt
import os
import cv2 #pip install opencv-python
import random
from requests import get 
import wikipedia
import webbrowser
import pywhatkit
import keyboard as k #pip install keyboard
import smtplib
import sys
import time
import requests 
from bs4 import BeautifulSoup #pip install bs4
import winsound #pip install Playsound
from playsound import playsound
from tkinter import * #inbuilt
import psutil #pip install psutil 
import speedtest #pip install speedtest-cli
import pyautogui #pip install pyautogui
import winreg #inbuilt
import shlex #inbuilt
from googletrans import Translator  #pip install googletrans #if any error pip install googletrans==4.0.0-rc1
from pytube import YouTube #pip install pytube3  #if any error python -m pip install --upgrade pytube
import pywikihow #pip install pywikihow
from pywikihow import search_wikihow
from pywikihow import WikiHow
import math
import string
from ctypes import windll
import tkinter
import ctypes
import winshell #pip install winshell
import subprocess

#for GUI
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from VirtualAssistantGUI import Ui_ARVA_VISHTI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)heel
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',175)

class ButtonEntry():
    def __init__(self, root):
        self.entry_var=""

        startLabel =tkinter.Label(root,text="Enter here: ")
        self.startEntry=tkinter.Entry(root)

        startLabel.pack()
        self.startEntry.pack()
        self.startEntry.focus_set()

        plotButton= tkinter.Button(root,text="Press to save ",command=self.msgSend).pack()

    def msgSend(self):
        self.entry_var=self.startEntry.get()
        #print("inside class", self.entry_var)
        global resultForMsg
        resultForMsg = self.entry_var
        return resultForMsg

def try_finding_chrome_path():
    result = None
    if winreg:
        for subkey in ['ChromeHTML\\shell\\open\\command','Applications\\crhome.exe\\shell\\open\\command']:
            try: result = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, subkey)
            except WindowsError: pass
            if result is not None:
                result_split = shlex.split(result, False, True)
                result = result_split[0] if result_split else None
                if os.path.isfile(result):
                    break
                result = None

    else:
        expected = "google-chrome" + (".exe" if os.time=="nt" else "")
        for parent in os.environ.get('PATH','').split(os.pathsep):
            path = os.path.join(parent,expected)
            if os.path.isfile(path):
                result = path
                break
    return result

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def selectGender():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=5, phrase_time_limit=7)

    try:
        print("Recognizing...")
        global gender
        gender = r.recognize_google(audio, language='en-in').lower()
        print(f"User Said: {gender}")
    
    except Exception as e:
        speak("say that again please...")
        selectGender()
    
    print(gender)
    global gen
    gen = 0
    if gender=="0" or gender=="arwa" or gender=="Arwa" or gender=="Arva" or gender=="are vah" or gender=="are wah" or gender=="Are vah" or gender=="Are wah":
        engine.setProperty('voice',voices[0].id)  
        gen=0
        speak("I am Arva, how may I assist you?")
    elif gender=="vishti" or gender=="Vishti" or gender=="misty" or gender=="Misty" or gender=="srishti" or gender=="drishti" or gender=="visti" or gender=="bishti" or gender=="bisti" or gender=="bishty":
        engine.setProperty('voice',voices[1].id)
        gen=1
        speak("I am Vishti, how may I assist you?")
    else:
        speak("Can you please repeat")
        return selectGender()

def checkBattery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    return percentage

def wish():
    hour = int(dt.datetime.now().hour)

    battery = checkBattery()
    if battery>15 and battery<35:
        speak("REMINDER... Battery low, connect the charger")

    elif battery<=15 and battery>2:
        speak("Less than 15 percent battery remaining, connect the charger or the system will shut down")
        
    elif battery<=2:
        speak("Sleep mode on, less than 2 percent battery remaining")
        sys.exit()

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    #speak("I am Arva, please tell me how can I help you?")
    #speak("Do you want to talk to Arva or Vishti?") 
    speak("Would you like to talk to Arva or Vishti?")
    selectGender()

#turn on "Less secure app access" from the settings of gmail
def sendEmail(id,pwd,to,content):
    smtpserver = smtplib.SMTP('smtp.gmail.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(id,pwd)
    smtpserver.sendmail(id,to,content)
    smtpserver.close()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return a**b

def remove(str):
    return str.replace(" ", "")

def translateSentence():
    isAvailable = False
    speak("In which language do you want to translate?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=5, phrase_time_limit=7)

    try:
        print("Recognizing...")
        lang = r.recognize_google(audio, language='en-in').lower()
        print(f"User Said: {lang}")
    
    except Exception as e:
        speak("say that again please...")
        translateSentence()
    speak("What do you want to translate?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=5, phrase_time_limit=7)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"User Said: {text}")
    
    except Exception as e:
        speak("say that again please...")
        translateSentence()
    
    text = text.replace('translate','')
    
    translator = Translator()
    if "french" in lang:
        l = "fr"
        isAvailable = True
    elif "german" in lang:
        l = "de"
        isAvailable = True
    elif "spanish" in lang:
        l = "es"
        isAvailable = True
    elif "hindi" in lang:
        l = "hi"
        isAvailable = True
    elif "chinese" in lang:
        l = "zh-tw"
        isAvailable = True
    elif "portuguese" in lang:
        l = "pt"
        isAvailable = True
    elif "italian" in lang:
        l = "it"
        isAvailable = True
    elif "japanese" in lang:
        l = "ja"
        isAvailable = True
    if isAvailable==True:
        translated = translator.translate(text,src='en',dest=l)
        return speak(f"The translation for {text} is: {translated.text}")
    else:
        return speak("Sorry, This language translation is currently not available!")

def alarm(timeforalarm):
    time = str(dt.datetime.now().strptime(timeforalarm,'%I:%M %p'))
    #print(time)
    time = time[11:-3]
    hour = time[:2]
    hour = int(hour)
    minute = time[3:5]
    minute = int(minute)
    speak(f"Done, alarm is set for {timeforalarm}")

    while True:
        if hour == dt.datetime.now().hour:
            if minute == dt.datetime.now().minute:
                #print("Alarm is Running")
                #speak("GET UP!!!!")
                winsound.PlaySound('abc',winsound.SND_ALIAS)

            elif minute < dt.datetime.now().minute:
                sys.exit()
                break

def startGame():
    boardWidth = 30
    boardHeight = 30
    tilesize = 10

    class Snake():

        def __init__(self):

            self.snakeX = [20, 20, 20]
            self.snakeY = [20, 21, 22]
            self.snakeLength = 3
            self.key = "w"
            self.points = 0

        def move(self): # move and change direction with wasd

            for i in range(self.snakeLength - 1, 0, -1):
                    self.snakeX[i] = self.snakeX[i-1]
                    self.snakeY[i] = self.snakeY[i-1]

            if self.key == "w":
                self.snakeY[0] = self.snakeY[0] - 1

            elif self.key == "s":
                self.snakeY[0] = self.snakeY[0] + 1

            elif self.key == "a":
                self.snakeX[0] = self.snakeX[0] - 1

            elif self.key == "d":
                self.snakeX[0] = self.snakeX[0] + 1

            self.eatApple()

        def eatApple(self):

            if self.snakeX[0] == apple.getAppleX() and self.snakeY[0] == apple.getAppleY():

                self.snakeLength = self.snakeLength + 1

                x = self.snakeX[len(self.snakeX)-1] # Snake grows
                y = self.snakeY[len(self.snakeY) - 1]
                self.snakeX.append(x+1)
                self.snakeY.append(y)

                self.points = self.points + 1
                apple.createNewApple()

        def checkGameOver(self):

            for i in range(1, self.snakeLength, 1):

                if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                    return True # Snake eat itself

            if self.snakeX[0] < 1 or self.snakeX[0] >= boardWidth-1 or self.snakeY[0] < 1 or self.snakeY[0] >= boardHeight-1:
                return True # Snake out of Boundary

            return False

        def getKey(self, event):

            if event.char == "w" or event.char == "d" or event.char == "s" or event.char == "a" or event.char == " ":
                self.key = event.char

        def getSnakeX(self, index):
            return self.snakeX[index]

        def getSnakeY(self, index):
            return self.snakeY[index]

        def getSnakeLength(self):
            return self.snakeLength

        def getPoints(self):
            return self.points


    class Apple:

        def __init__(self):
            self.appleX = random.randint(1, boardWidth - 2)
            self.appleY = random.randint(1, boardHeight - 2)

        def getAppleX(self):
            return self.appleX

        def getAppleY(self):
            return self.appleY

        def createNewApple(self):
            self.appleX = random.randint(1, boardWidth - 2)
            self.appleY = random.randint(1, boardHeight - 2)

    class GameLoop:

        def repaint(self):

            canvas.after(200, self.repaint)
            canvas.delete(ALL)

            if snake.checkGameOver() == False:

                snake.move()
                snake.checkGameOver()

                canvas.create_rectangle(snake.getSnakeX(0) * tilesize, snake.getSnakeY(0) * tilesize,
                                        snake.getSnakeX(0) * tilesize + tilesize,
                                        snake.getSnakeY(0) * tilesize + tilesize, fill="red")  # Head

                for i in range(1, snake.getSnakeLength(), 1):
                    canvas.create_rectangle(snake.getSnakeX(i) * tilesize, snake.getSnakeY(i) * tilesize,
                                            snake.getSnakeX(i) * tilesize + tilesize,
                                            snake.getSnakeY(i) * tilesize + tilesize, fill="blue")  # Body

                canvas.create_rectangle(apple.getAppleX() * tilesize, apple.getAppleY() * tilesize,
                                        apple.getAppleX() * tilesize + tilesize,
                                        apple.getAppleY() * tilesize + tilesize, fill="green")  # Apple

            else:   # GameOver Message
                canvas.delete(ALL)
                canvas.create_text(150, 100, fill="darkblue", font="Times 20 italic bold", text="GameOver!")
                canvas.create_text(150, 150, fill="darkblue", font="Times 20 italic bold", text="Points:" + str(snake.getPoints()))

    snake = Snake()
    apple = Apple()
    root = Tk()

    canvas = Canvas(root, width=300, height=300)
    canvas.configure(background="yellow")
    canvas.pack()

    gameLoop = GameLoop()
    gameLoop.repaint()

    root.title("Snake")
    root.bind('<KeyPress>', snake.getKey)
    root.mainloop()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Arva_Vishti()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 3
            audio = r.listen(source, timeout=5, phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")
        
        except Exception as e:
            print(e)
            speak("say that again please...")
            return self.take_command()
        return query

    def Arva_Vishti(self):

        wish()

        if __name__ == "__main__":

            while True:
                
                self.query = self.take_command().lower()

                if "open notepad" in self.query:
                    try:
                        notepad = 'notepad'
                        os.system(notepad)
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "open command prompt" in self.query:
                    try:
                        os.system("start cmd")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "ip address" in self.query:
                    try:
                        ip = get('https://api.ipify.org').text
                        speak(f"Your IP address is {ip}")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "wikipedia" in self.query:
                    try:
                        speak("Searching Wikipedia...")
                        self.query = self.query.replace("wikipedia","")
                        results = wikipedia.summary(self.query,sentences=5)
                        speak("According to wikipedia,")
                        speak(results)
                        #print(results)
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "open youtube" in self.query:
                    try:
                        #webbrowser.open("www.youtube.com")
                        speak("what shall I play on youtube?")
                        song = self.take_command()
                        speak(f'playing {song} for you')
                        pywhatkit.playonyt(song)
                        sys.exit()
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "open facebook" in self.query:
                    try:
                        path = try_finding_chrome_path()
                        path = path.replace(os.sep,'/')
                        path = f'{path} %s'
                        webbrowser.get(path).open("www.facebook.com")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "open google" in self.query:
                    try:
                        speak("What should I search on google for you?")
                        cm = self.take_command().lower()
                        path = try_finding_chrome_path()
                        path = path.replace(os.sep,'/')
                        path = f'{path} %s'
                        webbrowser.get(path).open(f"https://www.google.com/search?q={cm}")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif 'open stackoverflow' in self.query or 'open stack overflow' in self.query:
                    try:
                        speak("Here you go to Stack Over flow.Happy coding")
                        path = try_finding_chrome_path()
                        path = path.replace(os.sep,'/')
                        path = f'{path} %s'
                        webbrowser.get(path).open("stackoverflow.com")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif 'the time' in self.query:
                    try:
                        strTime = dt.datetime.now().strftime("%H:%M:%S")   
                        speak(f"The time is {strTime}")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif 'change background' in self.query:
                    #path to be given in this format C:\Users\HP\Pictures\Saved Pictures\download.jpg
                    root=tkinter.Tk()
                    root.geometry("400x240")
                    BE=ButtonEntry(root)    
                    root.mainloop()
                    pic = resultForMsg
                    ctypes.windll.user32.SystemParametersInfoW(20,0,pic,0)
                    speak("Background changed successfully")

                elif 'lock window' in self.query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
 
                elif 'shutdown system' in self.query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    os.system("shutdown /s /t 30")
                                     
                elif 'empty recycle bin' in self.query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")
 
                elif "don't listen" in self.query or "stop listening" in self.query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(self.take_command())
                    time.sleep(a)
                    print(a)

                elif "write a note" in self.query:
                    speak("What should i write?")
                    note = self.take_command()
                    file = open('note to self.txt', 'w')
                    speak("Should i include date and time?")
                    response = self.take_command()
                    if 'yes' in response or 'sure' in response or 'yeah' in response:
                        strTime = dt.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)

                elif "send message" in self.query:
                    try:
                        speak("Tell me the number of the receiver")
                        cnt_code = "+91"
                        num = cnt_code + self.take_command()
                        speak(f"Please confirm the number: {num}")
                        userResponse = self.take_command().lower()
                        if "yes" in userResponse or "yeah" in userResponse or "ya" in userResponse:
                            speak("what message has to be sent?")
                            root=tkinter.Tk()
                            root.geometry("400x240")
                            BE=ButtonEntry(root)    
                            root.mainloop()
                            msg = resultForMsg
                            now = dt.datetime.now()
                            h = now.hour
                            m = now.minute + 2
                            pywhatkit.sendwhatmsg(num,msg,h,m,20)
                            #pyautogui.press("enter")
                            #pyautogui.click(1050, 950)
                            # time.sleep(2)
                            k.press_and_release('enter')
                            speak("Message sent successfully.")
                        else:
                            speak("Okay! I'll not send the message")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "send email" in self.query:
                    try:
                        def_email = "aartiagarwal197@gmail.com"
                        def_pwd = "pwd"
                        speak(f"Do you want to send message through {def_email} ?")
                        response = self.take_command().lower()
                        if "yes" in response:
                            speak("Provide me with the receiver's email address:")
                            root=tkinter.Tk()
                            root.geometry("400x240")
                            BE=ButtonEntry(root)    
                            root.mainloop()
                            to = resultForMsg
                            speak(f"What do you want to send to {to} ?")
                            content = self.take_command().lower()
                            sendEmail(def_email,def_pwd,to,content)
                        elif "no" in response:
                            speak("Can you please guide me to login your email...")
                            speak("Provide me with the your email address:")
                            root=tkinter.Tk()
                            root.geometry("400x240")
                            BE=ButtonEntry(root)
                            root.mainloop()
                            sender_id = resultForMsg
                            speak("Provide me with the your password for login:")
                            root=tkinter.Tk()
                            root.geometry("400x240")
                            BE=ButtonEntry(root)    
                            root.mainloop()
                            sender_pwd = resultForMsg
                            speak(f"What do you want to send to {to} ?")
                            content = self.take_command().lower()
                            speak("Provide me with the receiver's email address:")
                            root=tkinter.Tk()
                            root.geometry("400x240")
                            BE=ButtonEntry(root)    
                            root.mainloop()
                            to = resultForMsg
                            speak(f"What do you want to send to {to} ?")
                            content = self.take_command().lower()
                            sendEmail(sender_id,sender_pwd,to,content)
                        else:
                            speak("Okay, i'll not send any email")
                            break
                    except Exception as e:
                        print(e)

                elif "open camera" in self.query:
                    try:
                        cam = cv2.VideoCapture(0)
                        cv2.namedWindow("camera")
                        img_counter = 0
                        while True:
                            ret, frame = cam.read()
                            if not ret:
                                print("failed to grab frame")
                                break
                            cv2.imshow("camera", frame)

                            k = cv2.waitKey(1)
                            if k%256 == 27:
                                # ESC pressed
                                print("Escape hit, closing...")
                                #cam.destroyAllWindows()
                                break
                            elif k%256 == 32:
                                # SPACE pressed
                                img_name = "opencv_frame_{}.png".format(img_counter)
                                cv2.imwrite(img_name, frame)
                                print("{} written!".format(img_name))
                                img_counter += 1
                        cam.release()
                        cam.destroyAllWindows()
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "temperature" in self.query:
                    try:
                        speak("which place' temperature would you like to know?")
                        place = self.take_command().lower()
                        search = "Temperature in " + place
                        url = f'https://www.google.com/search?q={search}'
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div",class_="BNeawe").text
                        speak(f"Current {search} is {temp}")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "activate search mode" in self.query:
                    try:
                        speak("Plase tell me what do you want to search")
                        how = self.take_command()
                        max_results=1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "alarm" in self.query:
                    try:
                        speak('Please tell me the time to set the alarm. Example: 10:10 am')
                        userResponse = self.take_command()
                        userResponse = userResponse.replace('set alarm to ','')
                        userResponse = userResponse.replace('.','')
                        userResponse = userResponse.upper()
                        alarm(userResponse)
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "game" in self.query:
                    try:
                        speak('Okay.. I have the best game for you! The snake game! Would you like me to give you instructions?')
                        userResponse = self.take_command().lower()
                        if userResponse == 'yes':
                            speak('Alright! You need to use w key to go up , a key to go left, d key to go right and s key to come down. Eat the apples you grow, if not you die! All the best')
                            startGame()
                            sys.exit()
                        else :
                            speak("Sorry couldn't understand you!")
                    except Exception as e:
                        speak("OOPS! Something went wrong")
        
                elif "do some calculations" in self.query or "can you calculate" in self.query or "do some calculation" in self.query or "calculator" in self.query:
                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            speak("Hey, i can do basic calculations!")
                            speak("What do you want to calculate?")
                            my_string = self.take_command().lower()
                            print(my_string)
                            def getOperator(opr):
                                return{
                                    "+": add,
                                    "-": sub,
                                    "x": mul,
                                    "divided": divide,
                                    "/": divide,
                                    "power": power
                                }[opr]
                            def EvaluateExpression(op1,opr,op2):
                                op1,op2 = int(op1), int(op2)
                                return getOperator(opr)(op1,op2)
                            speak(f"The answer is: {EvaluateExpression(*(my_string.split()))} ")
                    except Exception as e:
                        print(e)
                        speak("OOPS! Something went wrong")
                
                elif "who made you" in self.query or "who created you" in self.query:
                    speak("I have been created by Aarti and Vishwa.")

                elif "who am i" in self.query:
                    speak("If you talk then definitely your human.")
 
                elif "how did you come into world" in self.query:
                    speak("Thanks to Aarti and Vishwa. Further It's a secret")
 
                elif "who are you" in self.query:
                    speak("I am your virtual assistant created by Aarti and Vishwa")
 
                elif 'reason for you' in self.query:
                    speak("I was created as a project by Aarti and Vishwa")
 
                elif "where is" in self.query:
                    self.query = self.query.replace("where is", "")
                    location = self.query
                    speak(f"User has asked to Locate {location}")
                    path = try_finding_chrome_path()
                    path = path.replace(os.sep,'/')
                    path = f'{path} %s'
                    webbrowser.get(path).open("https://www.google.nl/maps/place/"+ location + "")

                elif "will you be my girlfriend" in self.query or "will you be my boyfriend" in self.query:  
                    speak("I'm not sure about that, maybe you should give me some time to think")
 
                elif "how are you" in self.query:
                    speak("I'm fine, glad you asked me that")
 
                elif "i love you" in self.query:
                    speak("It's hard to understand to understand love")

                elif "battery" in self.query or "how much power left" in self.query:
                    try:
                        battery = checkBattery()
                        speak(f"Our system has {battery} percent battery")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "check internet speed" in self.query or "speed test" in self.query or "internet speed" in self.query:
                    try:
                        st = speedtest.Speedtest()
                        dl = round(st.download() / 1048576)
                        up = round(st.upload() / 1048576)
                        speak(f"The download speed is {dl} mbp s and upload speed is {up} mbp s")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "increase volume" in self.query or "volume up" in self.query or "volume high" in self.query:
                    try:
                        pyautogui.press("volumeup")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "decrease volume" in self.query or "volume down" in self.query or "volume low" in self.query:
                    try:
                        pyautogui.press("volumedown")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "volume off" in self.query or "mute" in self.query:
                    try:
                        pyautogui.press("volumemute")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "translate" in self.query:
                    try:
                        translateSentence()
                        res = "yes"
                        while res == "yes":
                            speak("Do you want to translate something else?")
                            res = self.take_command().lower()
                            if "yes" in res:
                                translateSentence()
                            else:
                                res = "no"
                                break
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "download video" in self.query:
                    try:
                        speak("Provide me the youtube link...")
                        root=tkinter.Tk()
                        root.geometry("400x240")
                        BE=ButtonEntry(root)    
                        root.mainloop()
                        url = resultForMsg
                        speak("Downloading, please wait, this might take a few minutes")
                        YouTube(url).streams.get_highest_resolution().download()
                        speak("Download completed.")
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "search a file" in self.query or "open a file" in self.query:
                    try:
                        isFound = False
                        root=tkinter.Tk()
                        root.geometry("400x240")
                        BE=ButtonEntry(root)    
                        root.mainloop()
                        search = resultForMsg
                        drives = []
                        bitmask = windll.kernel32.GetLogicalDrives()
                        for letter in string.ascii_uppercase:
                            if bitmask & 1:
                                drives.append(letter)
                                print(letter)
                                if letter!="c" and letter!="C":
                                    listing1 = os.walk(letter+":/")
                                    if isFound == False:
                                        print("Searching in "+letter+" drive")
                                        for root, dir, files in listing1:
                                            if search in files:
                                                print(os.path.join(root,search))
                                                os.startfile(os.path.join(root,search))
                                                isFound = True
                                                break
                                        if isFound == False:
                                            print(search + " not found in "+letter+" drive")
                            bitmask >>= 1
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                elif "talk to are vah" in self.query or "talk to misty" in self.query or "change gender" in self.query or "bored talking to you" in self.query:
                    global gen
                    g = gen
                    if g==0:
                        engine.setProperty('voice',voices[1].id)
                        speak("Okay, giving power to my partner. Arva Out Vishti In")
                        gen=1
                    elif g==1:
                        engine.setProperty('voice',voices[0].id)
                        speak("Okay, giving power to my partner. Vishti Out Arva In")
                        gen=0
                
                elif "joke" in self.query:
                    speak("Okay let me try to cheer you up. One funny joke coming right away")
                    test_list = ["Man 1 - Why is prime minister not seen in morning? Man 2 - Because he is pm not a m","When a wife asked his husband to give her some space, the husband locked the wife outside the house","People ask me: Is google a man or woman? My simple answer is: its a woman because it wont let you finish your sentence without making a suggesion.","A man shows up late for work. The boss yells: You should have been here at 8:30! The man replies: Why? what happened at 8:30?","Man 1: Whats up? Man 2: Nothing much, converting oxygen into carbon dioxide. Man 1: How the hell you do that? Man 2: Breathing... dude","Teeth says to tongue: if i just press a little, you'll get cut. Tongue replies: if i misuse a single word, all 32 of you will come out.","Imagine that you're in the forest where there is a tiger in front of you and right about to eat you. What will you do? ....... Stop imagining stupid","Boss: Why are you late? Employee: There was a man who lost his 100 dollar bill. Boss: That's nice, you were helping him to look for it? Employee: No, I wan standing on it.","Mother: Why did you scire less in test? Johnny: Because of absence. Mother: You mean you were absent in class? Johnny: No, but the boy who sits next to me was absent.","Customer: Do you serve crabs? Waiter: Please have a sit sir, we serve everyone.","Teacher: Why are you late? John: Because of the sign. Teaacher: What sign? John: The one that says, school ahead, go slow","Teacher: you know you cant sleep in my class. Boy: i know, but maybe if you were just a little quiter, i could"]
                    random_num = random.choice(test_list)
                    speak (str(random_num))
                    playsound('C://Users//HP//Desktop//Hackathon-final//VirtualAssistant//laugh.mp3')

                elif "no" in self.query:
                    try:
                        speak("Thank you for using me, have a great day ahead...")                
                        sys.exit()
                    except Exception as e:
                        speak("OOPS! Something went wrong")

                speak("Do you have any other work?")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ARVA_VISHTI()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.close)
    
    def startTask(self):
        #self.ui.movie = QtGui.QMovie("path of gif")
        #self.ui.label.setMovie(self.ui.movie)
        #self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        now = QDate.currentDate()
        time = currentTime.toString("hh:mm:ss")
        date = now.toString(Qt.DefaultLocaleShortDate)
        self.ui.textBrowser_2.setText(date)
        self.ui.textBrowser.setText(time)

App = QApplication(sys.argv)
ARVA_VISHTI = Main()
ARVA_VISHTI.show()
exit(App.exec_())
