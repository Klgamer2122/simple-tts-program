import pyttsx3


engine = pyttsx3.init()

# Set the properties for the speech
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, how are you?")

# Prompt the user to enter a text to speak
text = input("Enter text to speak: ")
speak(text)








