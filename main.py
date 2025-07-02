import speech_recognition as sr
import webbrowser
# import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
import time
from gtts import gTTS
import os
import pygame
import env
import threading
import pyjokes



recogniser = sr.Recognizer()
stop_speaking = False
# engine = pyttsx3.init()





# def speak(text):
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.setProperty('rate', 140)
#     # time.sleep(0.5)
#     engine.say(text)
#     engine.runAndWait()

# Speaking Finctionality
def speak(text):
    # Use Hindi language with Hinglish-style text
    tts = gTTS(text)
    tts.save("temp.mp3")
    print(text)
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)
    while pygame.mixer.music.get_busy():
        if stop_speaking:
            pygame.mixer.music.stop()
            break
        time.sleep(0.1)
        
    # Unload the audio file frome the terminal
    pygame.mixer.music.unload()
    # Delete the audio file after finished speaking
    os.remove("temp.mp3")

    
# Listen for Interupt functionality
def listen_for_interrupt():
    global stop_speaking
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Interrupt listener active...")
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=3)
            command = r.recognize_google(audio)
            print("Heard:", command)
            if "stop" in command.lower() or "pause" in command.lower():
                stop_speaking = True
        except:
            pass
    
def processCommand(c):
    listener_thread = threading.Thread(target=listen_for_interrupt)
    # Opens Google Search
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    # Opens YouTube
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    # Opens Facebook
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    # Opens Instagram
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        
    # Tell Jokes
    elif "joke" in c.lower():
        joke = pyjokes.get_joke(language="en", category="neutral")
        # Listen for interrupt...
        listener_thread.start()
        speak(joke)
        # Wait for thread to finish...
        listener_thread.join()
        
    # If asked for news, this will only fetch headlines of the news and speak them...
    elif "news" in c.lower():
        # Fetch news from the NEWS_API server...
        r = requests.get(env.URL["NEWS_URL"])
        
        # Check if connected to server...
        if r.status_code == 200:
            #  Fetch news as json
            news = r.json()
            # Extract all the articles from json in articles dictionary
            articles = news.get('articles', [])
            
            # Speaks the data of all titles in the dictionary 
            for article in articles:
                # Listening for interrupt...
                listener_thread.start()
                # Starts speaking...
                speak(article['title'])
                # Wait for thread to finish...
                listener_thread.join()
                
        # If not connected to server...
        else:
            print(f"failed to retrieve Headlines: {r.status_code}")
            
    elif "weather" in c.lower():
        r = requests.get(env.URL["WEATHER_URL"])
        if r.status_code == 200:
            data = r.json()

            location = data['location']['name']
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            wind_kph = data['current']['wind_kph']
            # pm2_5 = data['current']['air_quality']['pm2_5']
            pm10 = data['current']['air_quality']['pm10']
            if pm10 in range(0, 51):
                aqi = f"{pm10} Good"
            elif pm10 in range(51, 101):
                aqi = f"{pm10} Satisfactory"
            elif pm10 in range(101, 251):
                aqi = (2/3)*(pm10 - 100)*100
    
                

            speak(f"Location: {location}")
            speak(f"Temperature is {temp_c}°C")
            speak(f"Condition is {condition}")
            speak(f"Humidity is {humidity}%")
            speak(f"Wind Speed is {wind_kph} km/h")
            speak(f"Air Quality is {aqi}")
            # speak(f"PM10: {pm10} µg/m³")

        else:
            print(f"Failed to fetch weather data: {response.status_code}")
        
    
    # Music playing Functionality 
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ")
        song = parts[1]
        
        # If just said music instead of song name
        if song == "music":
            link = musicLibrary.music["goodbye"]
            webbrowser.open(link)
            
        # To play song in Spotify
        elif song == "spotify":
            link = env.URL["SPOTIFY_URL"]
            webbrowser.open(link)
        
        # Search for song name in the musicLibrary
        elif song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            
        # If song not found in library
        else:
            speak(f"Sorry, I couldn't find {song} in the music library")
        
    else:
        # let AI handle the request
        client = OpenAI(
            api_key=env.API_KEY["OPEN_ROUTER_API"],
            base_url=env.URL["OPEN_ROUTER_BASE_URL"]
        )

        # Get response from AI Model
        response = client.chat.completions.create(
            model=env.MODEL["OPEN_ROUTER_MODEL"],
            messages = [
                {
                    "role" : "system",
                    "content" : """You are a Virtual Assistant named Siri.
                    You are skilled in general tasks like Alexa and Google Cloud. 
                    Make responses short. 
                    You are currently serving in India.
                    Do not give myself unitil asked.
                    Give responses to the point.
                    """
                },
                {
                    "role" : "user",
                    "content" : f"{c}"
                }
            ]
        )
        # Listen for interrupt...
        listener_thread.start()
        # Start speaking...
        speak(response.choices[0].message.content)
        # Wait for thread to finish...
        listener_thread.join()
        
        

if __name__ == "__main__":
    # speak("Initializing Assistant...")
    stop_speaking = False
    
    
    
    while True:
        r = sr.Recognizer() 
        
        
        try:
            # Listen for wake word 
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 4, phrase_time_limit = 2)
            
            word = r.recognize_google(audio)
            if word:
                print("Recognising...")
            if word.lower() == "exit":
                print("Exiting...")
                break
            if word.lower() == "hey siri":
                time.sleep(0.2)
                speak("How may i help you")
                while True:
                    try:
                        # Starts listening for commands
                        with sr.Microphone() as source:
                            print("Active Listening...")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            print(command)
                            if command:
                                print("Recognising...")
                            if command.lower() == "exit":
                                print("Exiting...")
                                break
                            processCommand(command)
                    except Exception as e:
                        print(f"{e}")
                    except sr.RequestError:
                        print("Network Error")
                        continue
                    except sr.UnknownValueError:
                        print("Sorry I didn't understand that.")
                        speak("Sorry I didn't understand that.")
                        continue
                    
        except Exception as e:
            print(f"{e}")
            
        except sr.RequestError:
            print("Network Error")
            continue
