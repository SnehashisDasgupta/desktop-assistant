
import pyttsx3,webbrowser,datetime,wikipedia, os, random 
import speech_recognition as sr

#pip install pyttsx3
#pip install webbrowser
#pip install datetime
#pip install wikipedia
#pip install os
#pip install speech_recognition

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

    speak("What's the task boss")

def takeCommand():
    #takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query,"\n")

    except Exception as e:
        # print(e)
        print("Can't understand, please repeat boss")
        speak("Can't understand, please repeat boss")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    check = True
    while check:
    # if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Seaching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"Boss, the time is {strTime}")

        elif 'stop jarvis' in query:
            check = False 
