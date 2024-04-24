import os
import pyaudio
import wave
from pynput import keyboard
import pyfiglet
import time
path=os.path.dirname(__file__)
font=pyfiglet.Figlet(font='standard')
heading =font.renderText('Voice Recorder')
Yellow ='\033[33m'
Red='\033[91m'
Reset='\033[0m'
print(heading)
close=False
def keypress(key):
    global close
    if key is not None:
        close= True
        return False

def open():
    global path
    sound=pyaudio.PyAudio()
    track=sound.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames=[]
    print("\n=========================  Recording  ==========================\n")
    print(Yellow + "Press any key to stop recording....." + Reset) 
    with keyboard.Listener(on_press=keypress) as listener:
        while close is False:
            in_voice=track.read(1024)
            frames.append(in_voice)
    print("\n" + Red + "Recording stopped" + Reset + "\n")
    
    timestamp=time.strftime("%Y%m%d_%H%M%S")
    filename=f"Recording_{timestamp}.wav"

    directory=os.path.dirname(path)
    print(f"Your recorded audio has been saved in: {Yellow}{path}\{filename}{Reset}\n\n")

    track.stop_stream()
    track.close()
    sound.terminate()

    doc=wave.open(filename,"wb")
    doc.setnchannels(1)
    doc.setsampwidth(sound.get_sample_size(pyaudio.paInt16))
    doc.setframerate(44100)
    doc.writeframes(b''.join(frames))
    doc.close()

print(Yellow+"Press enter to start recording....."+Reset)
input()
open()
