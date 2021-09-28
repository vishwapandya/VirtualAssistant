from math import fabs
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
import smtplib
import sys
import time
import requests 
from bs4 import BeautifulSoup
import psutil #pip install psutil
import speedtest #pip install speedtest-cli
import pyautogui
import winreg
import shlex
from googletrans import Translator  #pip install googletrans #if any error pip install googletrans==4.0.0-rc1
from pytube import YouTube #pip install pytube3  #if any error python -m pip install --upgrade pytube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)heel
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',175)

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

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    
    except Exception as e:
        speak("say that again please...")
        return take_command()
    return query

def selectGender():
    gender = take_command()
    print(gender)
    if gender==0 or gender=="0" or gender=="zero" or gender=="arva" or gender=="arwa" or gender=="Arwa" or gender=="Arva" or gender=="are vah" or gender=="are wah" or gender=="Are vah" or gender=="Are wah":
        engine.setProperty('voice',voices[0].id)
        speak("I am Arva, how may I assist you?")
    elif gender==1 or gender=="1" or gender=="one" or gender=="vishti" or gender=="Vishti" or gender=="misty" or gender=="Misty" or gender=="srishti" or gender=="drishti":
        engine.setProperty('voice',voices[1].id)
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
    speak("To continue with Arva say 0 and say 1 for vishti...")
    selectGender()

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

def askLogin():
    speak("Provide me with your id:")
    usr_name = take_command().lower()
    speak("Can you provide me with your domain name:")
    dmn_name = take_command().lower()
    id = remove(usr_name) + '@' + dmn_name + '.com'
    return id

def remove(str):
    return str.replace(" ", "")

def translateSentence():
    isAvailable = False
    speak("In which language do you want to translate?")
    lang = take_command().lower()
    speak("What do you want to translate?")
    text = take_command().lower()
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
    if isAvailable==True:
        translated = translator.translate(text,src='en',dest=l)
        return speak(f"The translation for {text} is: {translated.text}")
    else:
        return speak("Sorry, This language translation is currently not available!")

wish()

if __name__ == "__main__":

    while True:
        
        query = take_command().lower()

        if "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia,")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            #webbrowser.open("www.youtube.com")
            speak("what shall I play on youtube?")
            song = take_command()
            speak(f'playing {song} for you')
            pywhatkit.playonyt(song)
            sys.exit()

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("What should I search on google for you?")
            cm = take_command().lower()
            path = try_finding_chrome_path()
            path = path.replace(os.sep,'/')
            path = f'{path} %s'
            webbrowser.get(path).open(f"https://www.google.com/search?q={cm}")

        elif "send message" in query:
            speak("Tell me the number of the receiver")
            cnt_code = "+91"
            num = cnt_code + take_command()
            speak(f"Please confirm the number: {num}")
            userResponse = take_command().lower()
            if userResponse == "yes" or userResponse == "yeah" or userResponse == "ya":
                speak("what message has to be sent?")
                msg = input("Enter message here...")
                now = dt.datetime.now()
                h = now.hour
                m = now.minute + 1
                pywhatkit.sendwhatmsg(num,msg,h,m,2)
                speak("Message sent successfully.")
            else:
                speak("Okay! I'll not send the message")

        elif "send email" in query:
            try:
                def_email = "aartiagarwal197@gmail.com"
                def_pwd = "pranavbhondu"
                speak(f"Do you want to send message through {def_email} ?")
                response = take_command().lower()
                if "yes" in response:
                    speak("Provide me with the receiver's email address:")
                    to = input("Enter the receiver's email address:")
                    speak(f"What do you want to send to {to} ?")
                    content = take_command().lower()
                    sendEmail(def_email,def_pwd,to,content)
                else:
                    speak("Can you please guide me to login your email...")
                    id = askLogin()
                    speak(id + " Is this your email id?")
                    res = 'yes'
                    while res=='yes':
                        res = take_command().lower()
                        if "yes" in res:
                            speak('ok')
                            speak("Guide me with your password for login...")
                            pwd = remove(take_command().lower())
                            speak("Guide me with the receiver's id...")
                            rec_id = remove(take_command().lower())
                            speak("Guide me with the receiver's domain...")
                            rec_dom = remove(take_command().lower())
                            to = rec_id + "@" + rec_dom + ".com" 
                            print(to)
                            speak("Do you want to send email to " + to)
                            userResponse = take_command().lower()
                            #print(userResponse)
                            if userResponse == "yes":
                                speak("What should I send?")
                                content = take_command().lower()
                                # sendEmail(to, content)
                                speak("Email has been sent to " + to)
                                break
                            else: 
                                speak("Okay... So i'll not send any email")
                                break
                        elif "no" in res:
                            speak("OOPS! Sorry, Can you please again guide me to login your email...")
                            id = askLogin()
                            speak(id + " - Is this your email id?")
                            res = take_command().lower()
                        else:
                            speak("Okay, i'll not send any email")
                            break
            except Exception as e:
                print(e)

        elif "open camera" in query:
            # number = random.randint(0,100)
            # #initializing cv2
            # videoCaptureObject = cv2.VideoCapture(0)
            # result = True
            # while(result):
            #     #read the frames while the camera is on- it will return a boolean value 
            #     ret,frame = videoCaptureObject.read()
            #     #cv2.imwrite() method is used to save an image to any storage device
            #     img_name = "img"+str(number)+".png"
            #     cv2.imwrite(img_name, frame)
            #     start_time = time.time
            #     result = False
            # speak("Snapshot taken")
            # # releases the camera
            # videoCaptureObject.release()
            # #closes all the window that might be opened while this process
            # cv2.destroyAllWindows()

            cam = cv2.VideoCapture(0)
            cv2.namedWindow("camera")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)

                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1
            cam.release()
            cam.destroyAllWindows()

        elif "temperature" in query:
            speak("which place' temperature would you like to know?")
            place = take_command().lower()
            search = "Temperature in " + place
            url = f'https://www.google.com/search?q={search}'
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif "no" in query:
            speak("Thank you for using me, have a great day ahead...")                
            sys.exit()
 
        elif "do some calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What do you want to calculate?")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def getOperator(opr):
                    return{
                        "+": add,
                        "-": sub,
                        "x": mul,
                        #"divided": operator.__truediv__,
                    }[opr]
                def EvaluateExpression(op1,opr,op2):
                    op1,op2 = int(op1), int(op2)
                    return getOperator(opr)(op1,op2)
                speak("The answer is: ")
                speak(EvaluateExpression(*(my_string.split())))

        elif "battery" in query or "how much power left" in query:
            battery = checkBattery()
            speak(f"Our system has {battery} percent battery")

        elif "check internet speed" in query or "speed test" in query or "internet speed" in query:
            st = speedtest.Speedtest()
            dl = round(st.download() / 1048576)
            up = round(st.upload() / 1048576)
            speak(f"The download speed is {dl} mbp s and upload speed is {up} mbp s")

        elif "increase volume" in query or "volume up" in query or "volume high" in query:
            pyautogui.press("volumeup")

        elif "decrease volume" in query or "volume down" in query or "volume low" in query:
            pyautogui.press("volumedown")

        elif "volume off" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "translate" in query:
            translateSentence()
            res = "yes"
            while res == "yes":
                speak("Do you want to translate something else?")
                res = take_command().lower()
                if "yes" in res:
                    translateSentence()
                else:
                    res = "no"
                    break

        elif "download video" in query:
            speak("Provide me the youtube link...")
            url = input("Enter link here:")
            speak("Downloading, please wait, this might take a few minutes")
            YouTube(url).streams.get_highest_resolution().download()
            speak("Download completed.")

        elif "search a file" in query or "open a file" in query:
            isFound = False
            listing1 = os.walk("C:/")
            listing2 = os.walk("D:/")
            listing3 = os.walk("E:/")
            listing4 = os.walk("F:/")
            search = input("Enter file name:")

            if isFound == False:
                speak(f"Searching {search} in D: drive")
                for root, dir, files in listing2:
                    if search in files:
                        print(os.path.join(root,search))
                        os.startfile(os.path.join(root,search))
                        isFound = True
                if isFound == False:
                    speak(f"{search} not found in D drive")

            if isFound == False:
                speak(f"Searching {search} in E: drive")
                for root, dir, files in listing3:
                    if search in files:
                        print(os.path.join(root,search))
                        os.startfile(os.path.join(root,search))
                        isFound = True
                if isFound == False:
                    speak(f"{search} not found in E drive")

            if isFound == False:
                speak(f"Searching {search} in F: drive")
                for root, dir, files in listing4:
                    if search in files:
                        print(os.path.join(root,search))
                        os.startfile(os.path.join(root,search))
                        isFound = True
                if isFound == False:
                    speak(f"{search} not found in F drive")

            if isFound == False:
                speak(f"Searching {search} in C: drive")
                for root, dir, files in listing1:
                    if search in files:
                        print(os.path.join(root,search))
                        os.startfile(os.path.join(root,search))
                        isFound = True
                if isFound == False:
                    speak(f"{search} not found in C drive")

        speak("Do you have any other work?")