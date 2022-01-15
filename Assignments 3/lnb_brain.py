from cgitb import text
import os
from re import T
from gtts import gTTS
from playsound import playsound
def voi():
    for i in range(1,4):
        a=input("Enter the name of the directory:- ")
        parent=r"C:\Users\shubh\Desktop\LnB_assignments\Assignments 3"
        mode=0o666
        path=os.path.join(parent,a)
        isFile=os.path.isfile(path)
        try:
            os.makedirs(path,mode)
            b="Dimame created"
            language='en'
            final=gTTS(text=b,lang=language,slow=True)
            final.save("out.mp3")
            playsound("out.mp3")
        except FileExistsError:
            b="dimame already exists"
            language='en'
            final=gTTS(text=b,lang=language,slow=True)
            final.save("out.mp3")
            playsound("out.mp3")
            voi()

voi()
    