import pyttsx3
import speech_recognition as sr
import eel 
import time 

# Initialize the engine
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use female voice
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    eel.receiverText(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing....')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(3)
    except Exception:
        return ""

    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("What message to send")
                    query = takecommand()
                elif "phone call" in query:
                    flag = ''
                    speak("Calling " + name)
                else:
                    flag = ''
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print("Error:", e)

    eel.ShowHood()
