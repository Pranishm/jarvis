from multiprocessing import Process
import eel

# === Import your assistant backend ===
from main import start  # This should launch any face recognition etc.
from backend.feature import hotword  # Hotword detection
from backend import command  # Eel-exposed commands

# === Initialize Eel ===
eel.init('frontend')  # This must point to the folder with your index.html

# === Start Eel as one process ===
def startJarvis():
    print("Starting Jarvis GUI and backend...")
    eel.start('index.html', size=(800, 600))

# === Start Hotword as separate process ===
def listenHotword():
    print("Listening for hotword...")
    hotword()

if __name__ == "__main__":
    p1 = Process(target=startJarvis)
    p2 = Process(target=listenHotword)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
