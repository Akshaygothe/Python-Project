import os
import PyPDF2
import pyttsx3
import fitz 
import sys 
from pynput import keyboard
import keyboard
import csv
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dir_path = 'F:/Books/'
books = ['A brief history of human kind', 'Instructions', 'Python.Natural.Language.Processing']
#path = r'C:/Users/Admini/newproj/A-Very-Short-Story.pdf'

def bookReader(path, book_name):
    get_out = 0
    doc = fitz.open(path)
    pdf_size = doc.pageCount
    print("number of pages:",doc.pageCount)

    # Accessing data from csv file for book Mark.
    with open('book_list.csv','rt')as f:
        data = csv.reader(f)
        bookMark_dict = {}
        for row in data:
            bookMark_dict[row[0]] = row[1]
            print(row)
        print(bookMark_dict)
    # staring page is taken from csv file of book mark.
    if bookMark_dict.get(book_name) == None:
        page_no = int(input("Enter the page from you want to start:"))
    else:
        page_no = int(bookMark_dict[book_name])
    print(f"Last time You left on page {page_no + 1}.")
    exited_page = 0
    for i in range(page_no, pdf_size):
        print("You are on page: ", i + 1)
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

            if keyboard.is_pressed('s'):
                speak("You paused reading. After one minute i start reading again.")
                time.sleep(1000)

            speak(sent)
        if get_out == 1:
            break
    
    bookMark_dict[book_name] = str(exited_page)

    col_names = ['Book', 'Bookmark']
    if 'book_list.csv' not in os.listdir(r'C:/Users/Admini/newproj'):
        with open('book_list.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(col_names)
            for book in books:
                csv_writer.writerow([book, bookMark_dict[book]])
    else:
        with open('book_list.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(col_names)
            for book in books:
                csv_writer.writerow([book, bookMark_dict[book]])
    return exited_page

if __name__ == '__main__':
    print("Welcome to Book Reader")
    print("Avalibal Book List:")
    for count, book in enumerate(books):
        print(count, book)
    
    book_number = int(input("Which Book You want To Listen: "))
    exited_page = bookReader(os.path.join(dir_path + books[book_number] + '.pdf'), books[book_number])
    print(f'You stop on page Number: {exited_page + 1}')
    print("visit Next Time.")


    









