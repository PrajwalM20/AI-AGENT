import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None

# Call the function
if __name__ == "__main__":
    speech_to_text()
