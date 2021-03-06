from tkinter import *
import parser
from math import factorial

root = Tk()
#root.geometry('400x400')
root.title('Calculator')

# adding the input field
display = Entry(root)
display.grid(row=1, columnspan=4, sticky=N+E+W+S)

# code to add buttons to the calculator
Button(root, text="<x", command = lambda:undo()).grid(row=2, column=3, sticky=N+S+E+W)

Button(root, text="(", command = lambda:get_operation("(")).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text=")", command = lambda:get_operation(")")).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text="/", command = lambda:get_operation("/")).grid(row=3, column=2, sticky=N+S+E+W)
Button(root, text="AC", command = lambda:clear_all()).grid(row=3, column=3, sticky=N+S+E+W)

Button(root, text="7", command = lambda:get_variables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text="8", command = lambda:get_variables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text="9", command = lambda:get_variables(9)).grid(row=4, column=2, sticky=N+S+E+W)
Button(root, text="x", command = lambda:get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)

Button(root, text="4", command = lambda:get_variables(4)).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text="5", command = lambda:get_variables(5)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text="6", command = lambda:get_variables(6)).grid(row=5, column=2, sticky=N+S+E+W)
Button(root, text="-", command = lambda:get_operation("-")).grid(row=5, column=3, sticky=N+S+E+W)

Button(root, text="1", command = lambda:get_variables(1)).grid(row=6, column=0, sticky=N+S+E+W)
Button(root, text="2", command = lambda:get_variables(2)).grid(row=6, column=1, sticky=N+S+E+W)
Button(root, text="3", command = lambda:get_variables(3)).grid(row=6, column=2, sticky=N+S+E+W)
Button(root, text="+", command = lambda:get_operation("+")).grid(row=6, column=3, sticky=N+S+E+W)

Button(root, text="0", command = lambda:get_variables(0)).grid(row=7, column=0, sticky=N+S+E+W)
Button(root, text=".", command = lambda:get_variables(".")).grid(row=7, column=1, sticky=N+S+E+W)
Button(root, text="%", command = lambda:get_operation("%")).grid(row=7, column=2, sticky=N+S+E+W)
Button(root, text="=", command = lambda:claculate()).grid(row=7, column=3,sticky=N+S+E+W)

# i keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length
def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

def claculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")
if __name__ == '__main__':
    root.mainloop()