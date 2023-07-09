import os, pyttsx3, sys, openai, speech_recognition as sr
from dotenv import load_dotenv as ld


def talk(words):
    print(words)
    #os.system(f'say {words}')
    engine.say(words)
    engine.runAndWait()


def command(words):
    global r
    with sr.Microphone(device_index=1) as source:
        print('the microphone will be activated in 1 second')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, 1)
        audio=r.listen(source)
    try:
        task=r.recognize_google(audio, language='ru-RU').lower()
        print(f'You: {task}')
    except sr.UnknownValueError:
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
    else:
        try:
            #print(handle_input(input('>')).choices[0].message.content)
            ai_res=ai_response(what).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk('Error, I will try it again.')
            try:
                # print(handle_input(input('>')).choices[0].message.content)
                ai_res = ai_response(what).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk('The error still exists. Ask a message again in 20 seconds.')
                r.pause_threshold=20
        except:
            talk('Ops, what is going on... AAAAAAAA! its amazing! wow! XDXDXDXDXDXD 1 2 3 4 try again')


def ai_response(task):
    completion=openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': task}])
    return completion


dotenv_path=os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    ld(dotenv_path)
openai.api_key=os.getenv('api_key')

r=sr.Recognizer()
engine=pyttsx3.init()
# engine.say('Текст')
# engine.runAndWait()
# talk("import os, pyttsx3 import speech_recognition as sr engine=pyttsx3.init() #engine.say('Текст') #engine.runAndWait() def talk(words):    print(words)    #os.system(f'say {words}')    engine.say(words)    engine.runAndWait()")

while 1:
    make_something(command(None))
