import speech_recognition as sr
import pyaudio
import pywhatkit
import os

#Recognizer Initialization
listen1 = sr.Recognizer()

#Listening to the Microphone
with sr.Microphone() as myorder:
    print("I am listening ...")
    myvoice = listen1.listen(myorder)
    #Recognizing and Processing the Command
    mycommand = listen1.recognize_google(myvoice)
    mycommand = mycommand.lower()
    print(mycommand)
#Executing Commands
    if ("notepad") in mycommand:
        os.system('notepad')
    if("play") in mycommand:
        mycommand=mycommand.replace("play",'')
        pywhatkit.playonyt(mycommand)
    #Opening a Web Browser:
    if "open web browser" in mycommand:
            os.system('start firefox')
    #Searching on Google
    if "search" in mycommand:
            mycommand = mycommand.replace("search", '')
            pywhatkit.search(mycommand)
    #Getting the current time
    import datetime
    if "time" in mycommand:
        now = datetime.datetime.now().strftime('%I:%M %p')
        print("The current time is:", now)

