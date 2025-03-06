import speech_recognition as sr

recognizer = sr.Recognizer()

# Change device_index based on Step 2 output
mic = sr.Microphone(device_index=1)  

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Say something...")
    audio = recognizer.listen(source)

print("Recognizing...")
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError:
    print("Speech recognition service is unavailable.")

