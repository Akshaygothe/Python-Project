import os
import PyPDF2
import pyttsx3
import fitz 
import sys 
from pynput import keyboard
import keyboard
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dir_path = 'F:/Books/'
books = ['A brief history of human kind']
#path = r'C:/Users/Admini/newproj/A-Very-Short-Story.pdf'

def bookReader(path, book_name):
    get_out = 0
    doc = fitz.open(path)
    pdf_size = doc.pageCount
    print("number of pages:",doc.pageCount)
    page_no = int(input("Enter the page number from you want to listen: "))
    exited_page = 0
    for i in range(page_no, pdf_size):
        pageText = doc.loadPage(i)
        pageText = pageText.getText("text")
        pageText = pageText.replace('\r', '').replace('\n', '')
        sent_list = pageText.split('.')
        print(sent_list)
        for sent in sent_list:
            sent = sent.strip()
            if keyboard.is_pressed('q'): 
                speak('You Stop reading Book!')
                get_out = 1
                exited_page = i
                break
            if keyboard.is_pressed('n'):
                break
            speak(sent)
        if get_out == 1:
            break
    return exited_page 

if __name__ == '__main__':
    print("Welcome to Book Reader")
    print("Avalibal Book List:")
    for count, book in enumerate(books):
        print(count, book)
    
    book_number = int(input("Which Book You want To Listen: "))
    exited_page = bookReader(os.path.join(dir_path + books[book_number] + '.pdf'), books[book_number])
    print(f'You stop on page Number: {exited_page}')
    print("remember it for next time.")
    print("visit Next Time.")



    









