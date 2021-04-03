# Python-Project
This are some of my project using python language. I try to learn python using this simple projects.

# Project 1: Guess The Number
In this project, 
1. User can guess the number.
2. Computer can guess the number.

First, we have to select range in between of numbers. Then we can try few attempts to guess the number using instruction provided by opponent.

# Project 2: Rock Paper Sciessors
In this project,
User is playing Rock Paper Sciessors with computer. At a time they are making their choice of either Rock, Paper, or Sciessors. As, Rock beats sciessor, Sciessor beats Paper and Paper beats Rock. Using this observations result is declared. 

# Project 3: Hangman
In this project,
User have to identify the English word randomly selected by computer. User have 6 attepmts to identify that word. Also, some latters of that word are shown. So, that it will be help for user. If user able to identify that word in 6 attpemts then good. Otherwise, he will loose the game.

Random words are selected by computer is in Words.py file.

# Project 4: TicTacToe
In this project,
I try to create game TicTacToe. User can play with computer, where computer is not geinus. User has much probabity of winning.  

# Project 5: Genius Tic Tac Toe
In this project,
Computer is makeing good moves than random choices. So, its some sort of hard for user player to win. For makeing good moves computer is useing minmax function. Before makeing an moves it is analysing the game using recursive function.

# Project 6: Binary Search
In this project,
I created a list of 10000 numbers using random function. This list is passed to linear search and binary search to search a target number. and time comparison is done using time function. Binary search is best using log n time complexity. Instead of linear search of time complexity of n.
 
# Project 7: Mine Sweepers
This is a command line based game. In which user have to choose a location from ground of size (10 by 10). In some location, there are few bombs planted which are dengerous for game life. So, dig cousicsly. You may loose the game.

# Project 8: Sudoku Solver
In this project,
We have to pass the sudoku puzzle from command line. And then program of sudoku solver solve that puzzle using recursive calling function and backtracing method.
After solving that puzzle it display the solved version of puzzle. If it is unslovable, or wrong puzzle then it returns False in respect to it is unsolvable.

# Project 9: Dice Rolling Simulator
This is a simple python GUI project.
It mainly uses a tkinter to create GUI. Using it we can roll the dice for playing Snake and Ladders, Ludo and Checkers games.

# Project 10: Calculator
This ia s simple python GUI project. 
It uses a tkinter to create GUI. Using this calculator we can perform basic mathemitacal operations such as multiplication(*), Division(/), Subration(-), Addition(+), Reminder
(%). The result is shown at place of querry. 

# Project 11: Convert Text To Speech
Text to speech is a process to convert any text into voice. Text to speech project takes words on digital devices and convert them into audio with a button click or finger touch. Text to speech python project is very helpful for people who are struggling with reading.

To implement this project, we will use the basic concepts of Python, Tkinter, gTTS, and playsound libraries.

1. Tkinter is a standard GUI Python library that is one of the fastest and easiest ways to build GUI applications using Tkinter.
2. gTTS (Google Text-to-Speech) is a Python library, which is a very easy library that converts the text into audio.
3. The playsound module is used to play audio files. With this module, we can play a sound file with a single line of code.

In this project, we add a message which we want to convert into voice and click on play button to play the voice of that text message.

1. Importing the modules
2. Create the display window
3. Define functions

# Project 12: Book Reader
Sometimes reading books is a boring work. And for some readers english is not alwayes easy to read. So, to avoid this i tryed to make an simple module. Using it, computer can read books for us. For that i used pyttsx3 module. Using it we can access inbuild voice of windows system.
There is another module fitz to access the data of pdf. Using fitz i extract textual data from pdf books. That textual data is transfer to speech module. Which will read that textual data for us. At the end we have the book reader for us. 
