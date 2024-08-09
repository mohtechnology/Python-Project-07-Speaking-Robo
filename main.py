import win32com.client

speaker = win32com.client.Dispatch("sapi.spvoice")
speaker.speak("Hello boss Friday is here")
while 1:
    text = input("Enter your Text")
    speaker.speak(text)
    if text == "Exit":
        break
