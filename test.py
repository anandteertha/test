import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import time

warnings.filterwarnings('ignore')


def recordAudio():
    r = sr.Recognizer()  #recognizer object
    #open mic and start recording
    with sr.Microphone() as source:
        #btext = 'Say something'
        print("Say something : ")
        #assistantResponse(btext)
        audio = r.listen(source)

    # Use google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said : '+data)
    except sr.UnknownValueError:
        print('Google couldn\'t undestand the audio')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error '+e)

    return data


def assistantResponse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save('Assistant_response.mp3')
    os.system('start Assistant_response.mp3')
    time.sleep(3)


def wakeWord(text):
    WAKE_WORDS = ['hey ruby', 'ok ruby', 'hello ruby', 'greetings ruby', 'ruby', 'rubi', 'google'] #list of lower words
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #if word isn't found in the text from the loop
    return False


def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is '+weekday+' '+month_names[monthNum-1]+' the ' + ordinalNumbers[dayNum-1] + '.'


def greeting(text):
    Greeting_Inputs = ['hi', 'hey', 'hola', 'greetings', 'hello']
    Greeting_Responses = ['howdy', 'whats good', 'hello', 'hey there']

    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Responses)

    return ''


def getPerson(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i+3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]


while True:
    text = recordAudio()
    text = text.lower()
    response = ''

    if(wakeWord(text) == True):
        response = response + greeting(text)

        if('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if('time' in text):
            now = datetime.datetime.now()
            meri = ''
            if now.hour >= 12:
                meri = 'pm'
                hour = now.hour - 12
            else:
                meri = 'am'
                hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + str(hour) + ':' + minute + ' ' + meri

        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if(response == ''):
            response = 'No answer'
        else:
            assistantResponse(response)
