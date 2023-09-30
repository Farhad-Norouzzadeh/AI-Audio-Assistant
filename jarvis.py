import pyttsx3 # To convert string to voice
import datetime # To get date
import calendar # For getting the month name
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()


def speak(audio):   ## This method can convert string into voice using pyttsx3 library
    engine.say(audio)
    engine.runAndWait()


def time():  ## Getting time from out voice assistant
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():  ## Getting date from our voic assistant
    year = datetime.datetime.now().year
    month_index = datetime.datetime.now().month
    month_name = calendar.month_name[month_index]
    day = datetime.datetime.now().day
    speak(day)
    speak(month_name)
    speak(year)
# date()

def screenshot():
    img = pyautogui.screenshot()
    img.save("./screenshot.png")

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12 :
        speak("Good morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    elif hour >= 16 and hour <19:
        speak("Good evening")
    elif hour >= 19 and hour <= 24:
        speak("Good night")
    # speak("and Welcome back dear user.")
    # speak("the current time is")
    # time()
    # speak("the current date is")
    # date()
    
    speak("I am at your service. please tell me how can I help you ?")

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    # speak(query)
    return query

# takeCommand()
def tellJoke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abzc@gmail.com', '123')
    server.sendmail("abzc@gmail.com", to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    battery = str(psutil.sensors_battery())
    print("CPU is at " + usage)
    speak("CPU is at " + usage)
    print("Battery is at " + battery)
    speak("Battery is at " + battery)

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        # elif 'send email' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "xyz@gmail.com"
        #         sendEmail(to, content)
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Unable to send the Email")
        elif "chrome" in query :
            speak("What do you want me to search?")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.open_new_tab(search + ".com")
        elif "logout" in query:
            os.system('shutdown -l')
        elif "restart" in query:
            os.system('shutdown /r /t 1')
        elif "shutdown" in query:
            os.system('shutdown /s /t 1')
        elif "play songs" in query:
            songs_dir = ""   # Write your music directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open("data.txt", 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that", remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query or 'jokes' in query:
            tellJoke()

        elif 'offline' in query:
            speak("Going offline, goodbye")
            quit()

