import os
import eel
import threading  # NEW

from engine.features import *  # has hotword
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")
    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    # Start the assistant UI in browser
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # 🔊 Start hotword detection in background
    hotword_thread = threading.Thread(target=hotword, daemon=True)
    hotword_thread.start()

    # Start EEL
    eel.start('index.html', mode=None, host='localhost', block=True)
