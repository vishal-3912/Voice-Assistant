import google.generativeai as genai
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibray

genai.configure(api_key="AIzaSyCd_uMYd3fY_GgDcfUlWYUepiKMy5dytuA")

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def ask_gemini(prompt):
    """Send a prompt to Gemini AI and return the response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  
        response = model.generate_content(prompt)
        return response.text if response else "Sorry, I couldn't generate a response."
    
    except Exception as e:
        return f"Error: {str(e)}"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")    
        
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibray.music[song]
        webbrowser.open(link)
    else:
        # If no other command matches, ask Gemini AI
        response = ask_gemini(c)
        speak(response)


if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        r = sr.Recognizer()

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                #lisien for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error {0}".format(e))
