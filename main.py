import os, pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()
#engine.say('Текст')
#engine.runAndWait()

def talk(words):
    print(words)
    #os.system(f'say {words}')
    engine.say(words)
    engine.runAndWait()

#talk("import os, pyttsx3 import speech_recognition as sr engine=pyttsx3.init() #engine.say('Текст') #engine.runAndWait() def talk(words):    print(words)    #os.system(f'say {words}')    engine.say(words)    engine.runAndWait()")

def command(words):
    r=sr.Recognizer()

command('44')