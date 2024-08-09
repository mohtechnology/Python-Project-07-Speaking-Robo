import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Greet the user
engine.say("Hello boss Friday is here")
engine.runAndWait()

# Loop to continuously take input from the user and speak it
while True:
    text = input("Enter your Text: ")
    engine.say(text)
    engine.runAndWait()
    if text.lower() == "exit":
        break
