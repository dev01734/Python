import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests 
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# newsapi = "what ever the api we get"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

    #Load mp3 files

def aiprocess(command):

    client = OpenAI(
        api_key = ""
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named Aurora, who gives short responses and skilled in general task like Alexa and Siri."},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        # if "google" in c.lower():
        #         speak("ha ala")
        webbrowser.open("https://google.com") 

    elif "open youtube" in c.lower():
        # if "youtube" in c.lower():
        #         speak("ha ala")
        webbrowser.open("https://youtube.com") 

    elif "open instagram" in c.lower():
        # if "instagram" in c.lower():
        #         speak("ha ala")
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play"):
        # if "play" in c.lower():
        #         speak("ha ala")
        song = c.lower().split()[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    # elif "news" in c.lower():
    #     r = requests.get("link of api")
    #     if r.status_code == 200:
    #         data =r.json()
                #extract the articles
    #         articles = data.get('articles',[])
                #speak its headlines
    #         for article in articles:
    #             speak(article['title'])

    else: 
        # Let OpenAI handle the request
        output = aiprocess(c)
        speak(output)




if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word Aurora
        # Obtain audio from mic
        r = sr.Recognizer()


        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening") 
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Su che")
                # Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                    processCommand(command)

        except Exception as e:
            print("Error;(0)".format(e))