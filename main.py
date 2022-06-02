import pywhatkit
import wikipedia
import datetime
import pyttsx3
import pyjokes
import pyaudio
import speech_recognition as sr
listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',115)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
        print('whats good.....')
        talk('whats good!!')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if 'alexa' in command:
            command = command.replace('alexa','')
            talk(command)
  except ConnectionError:
      print('you have a poor internet connection')

  except ConnectionAbortedError:
      print('check your internet connection')
  except ConnectionRefusedError:
      print('am having issues with the network connection')
  except ConnectionResetError:
      print('poor connection. why amm about to cry even')
      pass
  return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk(str('playing') + song)
        pywhatkit.playonyt(song)
    elif'time'in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('current time is'+ time)
    elif'who the heck is' or 'who is' or 'what is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif'date'in command:
        talk('sorry,i have a headace')
    elif' tell me a joke'or 'some joke' in command:
        talk(pyjokes.get_joke())
    elif'are you single'in command:
        talk('i am  married to some girl called wifi')
    elif'who created you' in command:
         talk('the flyest guy i know.the charger')
    elif'you and siri who is better'or'are you better than siri'in command:
        talk('i mean that guy. am so super fly than siri')
    elif'who is Muriisa 'or 'who is John'or 'who is Muriisa John'in command:
        talk('you must be very wise to ask about this fly boy. Muriisa John is also known as,The charge . Haaaahaaaahaaahaaa')
    else:
        talk('please say it again i never got you.')
while True:
    run_alexa()