import pyttsx3

# Initialize the engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set a voice (usually index 0 for male, 1 for female, depends on system)
# You can skip this line, but it gives your assistant a specific voice
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    """Converts the given text to speech and plays it."""
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait() # Blocks while all currently queued commands are processed

    import speech_recognition as sr

def listen():
    """Listens for audio input from the user and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # Seconds of non-speaking data before a phrase is considered complete
        try:
            # Adjusts for ambient noise levels
            r.adjust_for_ambient_noise(source, duration=1.5) 
            audio = r.listen(source)
        except Exception as e:
            print("Error: Could not access microphone.")
            return "None"

    try:
        print("Recognizing...")
        # Uses Google's speech recognition API
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        # Happens when speech is inaudible or not recognized
        speak("Sorry, I did not catch that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        # Happens if there's no internet connection or API is down
        speak("I am currently offline. Please check your connection.")
        return "None"
        
    return query.lower()

def main():
    speak("Initializing voice assistant. I am ready to help.")
    
    while True:
        query = listen()
        
        # --- Core VA Logic ---
        if 'hello' in query:
            speak("Hello there! How can I assist you today?")

        elif 'what is your name' in query:
            speak("My name is Pyva, your Python Voice Assistant.")

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
        
        elif 'search for' in query:
            # Simple example: open Google with a search term
            # You would need to install the 'webbrowser' module: pip install webbrowser
            import webbrowser
            search_term = query.replace('search for', '').strip()
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")

# Run the assistant
if __name__ == "__main__":
    main()