
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Boss!")
    else:
        speak("Good evening Boss!")

    speak("I am Jarvis, how may i help you?")

def takeCommand():
    #takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss said: {query}\n")

    except Exception as e:
        # print(e)
        print("Can't understand, please repeat boss")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()