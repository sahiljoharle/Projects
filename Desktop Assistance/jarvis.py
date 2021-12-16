import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

print("initializing Jarvis")

MASTER = "sahil"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text): #it will pronounce the string that has passed to it 
    engine.say(text)
    engine.runAndWait()

def wishme():# THis function will wish you as per the given time 
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
        speak("good morning" + MASTER)
    
    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)
    else:
        speak("good evening" + MASTER)
    
def takecommand(): #Take user audio and convert it into string 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en=in')
        
        print(f"user said : {query}\n")
    except Exception as e :
        print("say that again please")
        query= None
    return query.lower()


 #program starts    

def sendemail(to, content):# to send email but i havent given email ans pass
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail.com','password')
    server.sendmail("anyone@.com", to,content)
    server.close()

def main(): # it has everything and if elif statement 
        speak("initializing Jarvis")
        wishme()
        speak(" How may i help you? ")
        query = takecommand()


        if 'wikipedia' in query:
            speak('searching wikipidia...')
            query = query.replace("wkipwdia","")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            #webbrowser.open("youtube.com")
            url="youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query:
            songs_dir= "C:\\Users\\sahil\\Downloads\\songs audio"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir ,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")


        '''
        elif 'open anything' in query :
            codepath=' path of program u want to run '
            os.startfile(codepath)

        elif 'email to harry' in query:
            try:
                speak("what should i send")
                content =takecommand()
                to = "harry@gmail.com"
                sendemail(to,content)
                speak("email has been send succesfully)
            except Exception as e:
                print(e)

        '''

main()