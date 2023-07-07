import os, pyttsx3, sys
import speech_recognition as sr


def talk(words):
    print(words)
    #os.system(f'say {words}')
    engine.say(words)
    engine.runAndWait()


def command(words):
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('the microphone will be activated in 1 second')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, 1)
        audio=r.listen(source)
    try:
        task=r.recognize_google(audio, language='ru-RU').lower()
        print(f'You: {task}')
    except sr.UnknownValueError:
        print('dont understand')
        talk("Don't understand")
        task=command(words)
    return task


def make_something(what):
    if ('open' and 'site') in what:
        talk('ok')
        os.startfile('https://ituniver.com')
    elif 'stop' in what:
        talk('Good bye')
        sys.exit()
    elif 'name' in what:
        talk('My name is JARVIS')


engine=pyttsx3.init()
#engine.say('Текст')
#engine.runAndWait()
#talk("import os, pyttsx3 import speech_recognition as sr engine=pyttsx3.init() #engine.say('Текст') #engine.runAndWait() def talk(words):    print(words)    #os.system(f'say {words}')    engine.say(words)    engine.runAndWait()")

while 1:
    make_something(command(None))