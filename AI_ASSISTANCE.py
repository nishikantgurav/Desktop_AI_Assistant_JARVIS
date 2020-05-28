import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine=pyttsx3.init('sapi5')#sapi5 is microsoft speech API
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)#0 is for male voice
# 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis sir.Please tell me how can I help you")


def take_command():
    '''It takes the microphone input from the user
   and returns string output'''
    r=sr.Recognizer()#Recognizer is a class that helps to recognize the audio
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing.......")
        query=r.recognize_google(audio,language='en-in')
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("Say that again please......")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("nishikantgurav19@gmail.com","password")
    server.sendmail('nishikantgurav19@gmail.com',to,content)
    server.close()



if __name__== "__main__":
    wishme()
    while True:
        query=take_command().lower()
        #logic for executing tasks based on query
        if 'wikipedia'in query:
            speak("Searching wikipedia.....")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='D:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint
            (0,3)]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" Sir,The time is {strTime}")

        elif ' open code' in query:
            codePath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to nishikant' in query:
            try:
                speak("What should I say?")
                content=take_command()
                to="nishikantgurav19@gmial.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("sorry , unable to send the mail")

        elif 'quit' in query:
            exit()




