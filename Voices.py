import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
for i in voices:
    #print(i)
    print(f'Name: {i.name}')
    print(f'ID: {i.id}')
    print(f'Language: {i.languages}')
    print(f'Gender: {i.gender}')
    print(f'Age: {i.age}')
    print('-------------------------------------------------------')
engine.setProperty('voice', 'eng')
for i in voices:
    if i.name=='Microsoft Zira Desktop - English (United States)':
        engine.setProperty('voice', i.id)
rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate', rate-199)
engine.say('123254365445141431414474513510000000000000000000000000000000000001111111111 ')
engine.runAndWait()