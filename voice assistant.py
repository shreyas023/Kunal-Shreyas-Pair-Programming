import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia
import pyjokes
import math

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

print('Hey! I am Granzo')
talk('Hey! I am Granzo')
print('What can I do for you?')
talk('What can I do for you?')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command.lower()
            print(command)
    except:
        pass
    return command

def run_granzo():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'girlfriend' or 'boyfriend' in command:
        print('Hahaha! Ask this question to yourself!')
        talk('Hahaha! Ask this question to yourself!')

    elif 'how are you' in command:
        print('I am fine. What about you?')
        talk('I am fine. What about you?')
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)

    elif 'what is' in command:
        search = command.replace('what is','')
        result = pywhatkit.search(search)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        print(datetime.date.today())
        talk(datetime.date.today())

    elif 'joke' in command:
        jokes = talk(pyjokes.get_joke())
        print(jokes)

    elif 'Hello' or 'Hi' or 'Hey' in command:
        print('How can I help you?')
        talk('Hey! I am Granzo. How can I help you ?')

    else:
        print('Sorry! I dont understand. Can you repeat that again?')
        talk('Sorry! I dont understand. Can you repeat that again?')

while True:
    run_granzo()