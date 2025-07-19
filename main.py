import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *
from backend.chatgpt_assistant import ask_gpt, speak
from backend.feature import play_assistant_sound

@eel.expose
def askChatGPT(message):
    print(f"Message received: {message}")
    try:
        reply = ask_gpt(message)
        speak(reply)
        return reply
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error: {str(e)}"

def start():
    print("Starting Jarvis...")
    speak("Welcome to Jarvis")
    eel.init('frontend')
    eel.start('index.html')


# Optional: Exposed function for face auth
@eel.expose
def init():
    eel.hideLoader()
    speak("Ready for Face Authentication")
    flag = AuthenticateFace()
    if flag == 1:
        speak("Face recognized successfully")
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Welcome to Your Assistant")
        eel.hideStart()
        play_assistant_sound()
    else:
        speak("Face not recognized. Please try again")

# Run
if __name__ == '__main__':
    start()
