import speech_recognition as sr
import pyttsx3
import os

micro = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'ru')

def talk(x):
    engine.say(x)
    engine.runAndWait()
    
    
def listen():
    text = ''
    with micro as sourse:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse, phrase_time_limit = 4)
        try:
            text = (r.recognize_google(audio, language = "ru-Ru")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
    return text

def cmd(text):
    if(text == 'создай папку на рабочем столе'):
        print('Hi')
        os.system("mkdir /home/pproger/Desktop/Copy_Video_detection")    


