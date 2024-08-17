import pyttsx3
import speech_recognition as sr
import os
import datetime
import webbrowser
import pygame
import random
import pygame.camera
import cv2
import time


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry Arpita"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello arpita I am your Personal AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["google", "https://www.google.com"], ["youtube", "https://www.youtube.com"],
                 ["wikipedia", "https://www.wikipedia.com"], ["twitter", "https://www.twitter.com"],
                 ["facebook", "https://www.facebook.com"], ["instagram", "https://www.instagram.com"],
                 ["whatsapp", "https://www.whatsapp.com"], ["yahoo", "https://www.yahoo.com"],
                 ["reddit", "https://www.reddit.com"], ["amazon", "https://www.amazon.com"],
                 ["myntra", "https://www.myntra.com"], ["netflix", "https://www.netflix.com"],
                 ["linkedin", "https://www.linkedin.com"], ["quora", "https://www.quora.com"],
                 ["pinterest", "https://www.pinterest.com"], ["canva", "https://www.canva.com"],
                 ["spotify", "https://www.spotify.com"],]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"OK Arpita, Opening {site[0]} ")
                webbrowser.open(site[1])
        if "what is the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Arpita the time is {strfTime}")

        elif 'play music' in query:
            pygame.mixer.init()
            folder = 'C:\\Users\\DELL\\Music\\'
            files = [file for file in os.listdir(folder) if file.endswith('.mp3')]
            random_mp3 = random.choice(files)
            file_path = os.path.join(folder, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(2)
        elif 'open camera' in query:
            TIMER = int(5)
            cap = cv2.VideoCapture(0)

            while True:
                ret, img = cap.read()
                cv2.imshow('arpita', img)
                k = cv2.waitKey(5)
                if k == ord('c'):
                    prev = time.time()

                    while TIMER >= 0:
                        ret, img = cap.read()

                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(img, str(TIMER),
                                    (200, 250), font,
                                    7, (0, 255, 255),
                                    4, cv2.LINE_AA)
                        cv2.imshow('picture', img)
                        cv2.waitKey(5)
                        cur = time.time()

                        if cur - prev >= 1:
                            prev = cur
                            TIMER = TIMER - 1

                    else:
                        ret, img = cap.read()

                        cv2.imshow('a', img)

                        cv2.waitKey(5)

                        cv2.imwrite('camera.jpg', img)

                elif k == 27:
                    break

            cap.release()

            cv2.destroyAllWindows()

        elif 'open folder web develop' in query:
          os.startfile(r"C:\\Users\\DELL\\OneDrive\\Desktop\\WebDevelop")










