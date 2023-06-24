import os, pyttsx3

engine=pyttsx3.init()
#engine.say('Текст')
#engine.runAndWait()

def talk(words):
    print(words)
    #os.system(f'say {words}')
    engine.say(words)
    engine.runAndWait()

talk('hello')