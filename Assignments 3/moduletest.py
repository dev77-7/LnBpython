import platform
import time
import webbrowser
print("The current OS :-",platform.system())
print("Version:-",platform.release())
time.sleep(3)
webbrowser.open("google.com")
time.sleep(2)
webbrowser.open("facebook.com")
time.sleep(2)
webbrowser.open("twitter.com")
