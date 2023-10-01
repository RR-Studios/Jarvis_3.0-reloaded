import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import webbrowser
import time
import requests
import shutil
import playsound
### connection apps to the jarvis main file and importing the app functions.
# from apps.bluetooth_manager import discover_nearby_devices, connect_to_device, disconnect_from_device
from apps.alarms import speak_alarm, set_alarm, start_alarm_scheduler, cancel_alarm, list_alarms
from apps.alexa_pairing import alexa_pairing_process
from apps.amazon_shopping_list import speak_shopping_list, get_amazon_shopping_list
from apps.article_genrator import generate_article
from apps.database_handler import DatabaseHandler
from apps.file_creator import create_file_with_extension
from apps.jokes_module import get_joke
# from apps.language_utils import detect_language, translate_text
from apps.mail_sender import sendEmail
from apps.music_player import playmusiconspotify
from apps.restaurants_finder import find_restaurants_near_me
from apps.route_info import get_live_location, get_directions
from apps.school_timetable import get_timetable, display_timetable, school_timetable
from apps.game_module import play_game
from apps.weather import get_live_location_weather

# from apps.database_handler import __init__, create_table, insert_user_input, get_input_history, close_connection


# Speak function
engine = pyttsx3.init('sapi5')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    # Greet the user


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir, I am Jarvis, your assistant. How can I assist you today?")


# Take user's voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


# Function to handle alarm-related commands
def handle_alarm_commands(query, alarms=None, bluetooth_manager=None):
    if "set alarm" in query:
        parts = query.split("set alarm")
        if len(parts) > 1:
            time_str = parts[1].strip()
            message = "Time to wake up!"
            response = alarms.set_alarm(time_str, message)
            speak(response)
    elif "cancel alarm" in query:
        parts = query.split("cancel alarm")
        if len(parts) > 1:
            time_str = parts[1].strip()
            response = alarms.cancel_alarm(time_str)
            speak(response)
    elif "list alarms" in query:
        response = alarms.list_alarms()
        speak(response)


# Function to read an article from a file and speak it
def read_article(filename):
    try:
        with open(filename, "r") as file:
            article = file.read()
        speak("Here is the generated article:")
        speak(article)
    except Exception as e:
        print(str(e))
        speak("Failed to read the article.")

        ### DATABASE ###
        # Create an instance of the DatabaseHandler class
        db_path = 'E:\\jarvis_database\\jarvis_databse.accd'
        db_handler = DatabaseHandler(db_path)

        # Create the table if it doesn't exist
        db_handler.create_table()

        # Inside your while loop where you get user inputs:
        query = takeCommand().lower()

        # Insert user input into the database
        db_handler.insert_user_input(query)

        # To retrieve input history:
        input_history = db_handler.get_input_history()
        for entry in input_history:
            user_input, timestamp = entry
            print(f"User Input: {user_input}, Timestamp: {timestamp}")

        # Close the database connection when done
        db_handler.close_connection()


# Commands
if __name__ == '__main__':
    # weather api key here
    weather_api_key = '38b02e632d50923594e7d5d0760e3417'
    # google maps api key here
    places_api_key = 'AIzaSyBoRyM1MHxbBVM85q_mLS8tJ5rVaZzUvfQ'

    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Raman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open amazon' in query:
            webbrowser.open('http://amazon.in')

        elif 'open google' in query:
            webbrowser.open('http://google.com')

        elif 'open github' in query:
            webbrowser.open('http://github.com')

        elif 'open space' in query:
            webbrowser.open('https://cybersage-vs-net.jetbrains.space/')

        elif 'open spotify' in query:
            webbrowser.open('https://spotify.com')

        elif 'open facebook' in query:
            webbrowser.open('https://facebook.com')

        elif 'open twitter' in query:
            webbrowser.open('https://twitter.com')

        elif 'email to' in query:
            try:
                speak("What should I say?, Sir")
                content = takeCommand()
                to = "raman5ransubhe@gmail.com"
                sendEmail(to, content)
                speak("The mail was sent successfully Sir")
            except Exception as e:
                print(e)
                speak("Sir, I am unable to send the email. Please try again")

        elif "play music on spotify" in query:
            playmusiconspotify(query)
            speak("Playing music on Spotify")

        elif 'show timetable' in query:
            # Ask for the day you want to see the timetable for
            speak("Which day's timetable would you like to see?")
            day_query = takeCommand().capitalize()  # Capitalize the day name
            school_timetable.display_timetable(day_query)

        elif "get weather" in query:
            weather_info = get_live_location_weather(weather_api_key)
            speak(weather_info)

        elif "find restaurants" in query:
            restaurants = find_restaurants_near_me(places_api_key)
            if isinstance(restaurants, list):
                speak("Here are some restaurants near you:")
                for i, (name, address) in enumerate(restaurants, start=1):
                    speak(f"{i}. {name}, located at {address}")
            else:
                speak(restaurants)

        elif "tell me a joke" in query:
            joke = get_joke()
            speak(joke)
            while True:
                speak("Do you want to hear another joke?")
                response = takeCommand().lower()
                if "yes" in response:
                    joke = get_joke()
                    speak(joke)
                elif "no" in response:
                    break

        elif 'create file' in query:
            create_file_with_extension()

        elif "play a game" in query:
            play_game()

        elif "set alarm" in query or "cancel alarm" in query or "list alarms" in query:
            handle_alarm_commands(query)

        #        if "discover bluetooth devices" in query:
        #            nearby_devices = bluetooth_manager.discover_nearby_devices()
        #           # Process the list of nearby Bluetooth devices

        #       elif "connect to device" in query:
        #            device_address = input("Enter the Bluetooth device address: ")
        #           socket = bluetooth_manager.connect_to_device(device_address)
        #           # Handle the connected socket

        #       elif "disconnect from device" in query:
        #            if 'socket' in locals() and socket:
        #               bluetooth_manager.disconnect_from_device(socket)
        #           else:
        #               speak("Not currently connected to any device.")

        elif "get route info" in query:
            speak("Please provide the destination.")
            destination = takeCommand()
            origin = "Your Current Location"  # You can replace this with your live location
            directions = get_directions(origin, destination, maps_api_key)
            weather_info = get_live_location(weather_api_key)
            speak(f"{directions}. {weather_info}")

        elif "get shopping list" in query:
            shopping_list = get_amazon_shopping_list()
            if shopping_list:
                speak_shopping_list(shopping_list)
            else:
                speak("Your Amazon shopping list is empty.")

        if "pair with alexa" in query:
            if alexa_pairing_process.alexa_pairing_process():
                speak("Alexa pairing successful! You can now use Jarvis with Alexa.")
            else:
                speak("Alexa pairing failed. Please try again.")

        # Detect the language of the user's query
        user_lang = detect_language(query)
        # Translate the query to English for processing if it's not already in English
        if user_lang != 'en':
            query = translate_text(query, 'en')

        if 'exit' in query:
            speak("Shutting down the jarvis")
            break