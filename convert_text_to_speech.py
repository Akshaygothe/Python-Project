from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

# Function to convert text to speech
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('sound.mp3')
    playsound('sound.mp3')
    os.remove('sound.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Initializing window
if __name__ == '__main__':
    root = Tk()
    root.geometry("350x350")
    root.configure(bg='ghost white')
    root.title("Text-To-Speech")

    Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg = 'white smoke').pack()

    Msg = StringVar()
    Label(root, text = "Enter Text", font = "arial 15 bold", bg = 'white smoke').pack()

    entry_field = Entry(root, textvariable = Msg, width='50')
    entry_field.place(x = 20, y = 100)

    Button(root, text = "PLAY", font = 'arial 15 bold', command = Text_to_speech, width = '4').place(x=25, y=140)
    Button(root, font='arial 15 bold', text='EXIT', width='4', command=Exit, bg='OrangeRed1').place(x=100, y=140)
    Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=175, y=140)

    root.mainloop()