import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    filename = f"response_{random.randint(1,100000)}.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("🤷 Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        print("⚠️ Could not connect to the recognition service.")
        return ""

def listen_and_respond():
    print("🚀 Say 'Yo Bot' to start...")
    text = listen()

    if text.startswith("hey Nexus"):
        speak_text("Hey! What do you want me to do?")
        print("👂 Waiting for your command...")
        command = listen()
        if command:
            speak_text(command)
        else:
            speak_text("Sorry, I didn't catch that.")
    else:
        print("🛑 Wake word not detected. Ignoring...")

# Continuous loop
while True:
    listen_and_respond()
