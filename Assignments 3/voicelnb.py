from gtts import gTTS
from playsound import  playsound

a=input("Enter the string to covert:- ")
language='en'
final=gTTS(text=a,lang=language,slow=False)
final.save("out.mp3")
playsound("out.mp3")