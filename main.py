import speech_recognition as sr
from selenium import webdriver
class voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
                try:
                    with sr.Microphone() as source:
                      audio = self.recognizer.listen(source)
                      command = self.recognizer.recognize_google(audio).lower()
                      
                      print(command)
                      if "search" in command:
                        driver = webdriver.Chrome()
                        driver.get("https://google.com={command.split('search')[1]}")
                except sr.UnknownValueError:
                    print("Sorry, I did not get that. Please try again.")
                    pass

listen = voice()
