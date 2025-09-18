import text_to_speech
import datetime
import webbrowser
import Weather  # Your custom module (must contain a weather() function)
import os
import random
import pyjokes

def Action(data):
 
    if not data:
        return "I didn't hear anything."

    user_input = data.lower().strip()

    # Greet user
    if "what is your name" in user_input:
        response = "My name is AI Agent"
        
    elif"what is my name"in user_input:
        response = "Prajwal M"

    elif "hello" in user_input or "hi" in user_input or "hye" in user_input:
        response = "Hey sir, how can I help you?"

    elif "good morning" in user_input:
        response = "Good morning sir"

    # Time-related
    elif "time now" in user_input or "what is the time now" in user_input:
        now = datetime.datetime.now()
        response = f"The time is {now.strftime('%I:%M %p')}"

    # Shutdown or exit
    elif "shutdown" in user_input or "exit" in user_input or "bye" in user_input:
        response = "Ok sir, shutting down"

    # Web commands
    elif "play music" in user_input or "gaana" in user_input:
        webbrowser.open("https://gaana.com/")
        response = "Gaana is ready for you"

    elif "youtube" in user_input:
        webbrowser.open("https://youtube.com/")
        response = "YouTube is ready for you"

    elif "open google" in user_input:
        webbrowser.open("https://google.com/")
        response = "Google is ready for you"
        
    
    elif "wikipedia" in user_input:
        webbrowser.open("https://www.wikipedia.org/")
        text_to_speech.text_to_speech("Opening Wikipedia")
        response= "Opening Wikipedia"

    elif "calculator" in user_input:
        try:
            os.system("calc")
            text_to_speech.text_to_speech("Open calculator")
            response= "Opening calculator"
        except:
            response= "Sorry, I couldn't open the calculator"

    elif "whatsapp" in user_input:
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech.text_to_speech("Open WhatsApp Web")
        response= "Opening WhatsApp Web"

    elif "joke" in user_input:
        joke = pyjokes.get_joke()
        text_to_speech.text_to_speech(joke)
        response= joke

    elif "inspirational quote" in user_input or "motivate me" in user_input:
        quotes = [
            "Believe in yourself and all that you are.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "Don’t watch the clock; do what it does. Keep going.",
            "Great things never come from comfort zones.",
            "Push yourself, because no one else is going to do it for you."
        ]
        quote = random.choice(quotes)
        text_to_speech.text_to_speech(quote)
        response= quote

    # Weather
    elif "weather" in user_input:
        try:
            response = Weather.weather()  # Make sure this returns a string
        except Exception as e:
            response = "Sorry, I couldn't fetch the weather right now."

    # Fallback
    else:
        response = "I am not able to understand what you want."

    # Speak the response
    text_to_speech.text_to_speech(response)
    return response
