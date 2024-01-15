import pyttsx3
def speak(inpText):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(inpText)
    engine.runAndWait()