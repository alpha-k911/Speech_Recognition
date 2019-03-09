import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something that i can recognize: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("I guess {}".format(text))
    except:
        print("I didn't get")

