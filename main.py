import time
import sounddevice as sd
from scipy.io.wavfile import write

freq = 44100
duration = input("Kaç saniye kayıt istersiniz?\n")

try:
    duration = int(duration)
    print("3 saniye sonra kayıt başlicak hazır olun!!")
    time.sleep(0.9)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("Konuşmaya başlayın!")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    sd.wait()

    write("record.mp3", freq, recording)
except:
    print("Hata, sayı girdiğinizden emin olun")
