import tkinter as tk
from tkinter import *
import PyPDF2
import pyttsx3
import docx
from tkinter import filedialog
import tkinter


root =Tk()
root.geometry('500x400')
root.title('PDF to Audio')


Label(root, text = "PDF to Audio",font="Arial 20", bg='Red').pack()

m=tk.IntVar()
f=tk.IntVar()

#Browse funtion

def browse():
    global text_content
    text_content= ""
    file = filedialog.askopenfilename(title="Select a fie",filetypes=[("PDF Files","*.pdf"),("Word File","*.docx"),("All files","*.")])

    if file.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(open(file,'rb'))
            for page in pdf_reader.pages:
                text_content +=page.extract_text()
        
        except Exception as e:
            print("Error while reading PDF {e}")

    elif file.endswith('.docs'):
        try:
            doc = docx.Document(file)
            for para in doc.paragraphs:
                text_content+= para.text

        except Exception as e:
            print("Error while reading word file {e}")

        pathlabel.config(text=file)


def save():
    global speaker
    if not text_content:
        Label(root,text="No text content found. Please select a valid file").pack()
        return


#Initialing the text to speach engine

    speaker =pyttsx3.init()
    voices = speaker.getProperty('voices')


    if m.get()== 0:
        speaker.setProperty('voice',voices[0].id) #male voice

    elif f.get() == 1:
        speaker.setProperty('voice',voices[1].id) #female voice


    #convert text into speach and saving audio file

    speaker.say(text_content)
    speaker.runAndWait()
    speaker.save_to_file(text_content,"audio.mp3")
    speaker.runAndWait()

    Label(root,text="Your audio file is saved").pack()


    #creating GUI
pathlabel=Label(root)
pathlabel.pack()

Button(root,text="Browse your file",command=browse).pack()
Button(root,text="Create and save audio file",command=save).pack()

Checkbutton(root,text="Male voice", onvalue=0,offvalue=10,variable=m).pack()
Checkbutton(root,text="Female voice",onvalue=0,offvalue=10,variable=f).pack()

root.mainloop()



                                      
                                    
                                                   
