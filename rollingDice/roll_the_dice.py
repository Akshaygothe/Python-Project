import tkinter
from PIL import Image, ImageTk
import random

#top-level width which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll The Dice')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="") # The ‘BlankLine’ label is to skip a line
BlankLine.pack() # use pack() to arrange our widgets in row and column form.

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello From Akshay!",
                                fg = "white",
                                bg = "dark blue",
                                font = "Helvetica 16 bold italic")
HeadingLabel.pack()

# images
dice = ['face-1.png', 'face-2.jpg', 'face-3.png', 'face-4.jpg', 'face-5.jpg', 'face-6.jpg']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keep window open
if __name__ == '__main__':
    root.mainloop()
