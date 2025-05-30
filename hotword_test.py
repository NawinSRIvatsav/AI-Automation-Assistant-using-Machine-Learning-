"""import pvporcupine
import pyaudio
import struct

def test_hotword():
    print("[INFO] Initializing hotword detection...")

    ACCESS_KEY = "w5Le/uh5RqXD9iSVbpcvr6Va4lW1V9ZSqkj4Nysu1Ow7U9rESJPtaQ=="  # ✅ Replace with actual access key

    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(
            access_key=ACCESS_KEY,
            keywords=["jarvis", "alexa"]
        )

        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("[INFO] Listening for hotwords ('jarvis', 'alexa')... Press Ctrl+C to stop.")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)

            if result >= 0:
                print(f"[HOTWORD DETECTED] Keyword index: {result}")

    except KeyboardInterrupt:
        print("\n[EXIT] Stopping detection...")

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if pa:
            pa.terminate()

if __name__ == "__main__":
    test_hotword()
"""

import os

def find_whatsapp_path():
    search_paths = [
        os.path.join(os.environ['LOCALAPPDATA'], 'WhatsApp', 'WhatsApp.exe'),
        os.path.join(os.environ['PROGRAMFILES'], 'WindowsApps'),
        os.path.join(os.environ['PROGRAMFILES'], 'WhatsApp', 'WhatsApp.exe'),
        os.path.join(os.environ['PROGRAMFILES(X86)'], 'WhatsApp', 'WhatsApp.exe') if 'PROGRAMFILES(X86)' in os.environ else ""
    ]

    for path in search_paths:
        if os.path.exists(path):
            return path

    return None
