import pyttsx3

# setting a voice using sapi5 speak API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to speak or give audio output to user
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":

    # taking input from console
    #print("please enter the text")
    #text = input()

    # taking input from a file
    with open('speech.txt', 'r') as f:
        speech = f.read()
    
    speak(speech)