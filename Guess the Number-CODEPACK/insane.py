#from tkinter import *
import random
import tkinter as tk
import os
def check():
    global ans
    #print(ans)
    if int(entry.get())==ans:
        chkbtn.destroy()
        wintext=tk.Label(root,text='Congrats! You win!',bg='midnightblue',fg='white')
        canvas.create_window(125,100,window=wintext)
        wintext.after(800,wintext.destroy)
        newbtn=tk.Button(text='   Generate New   ',command=launchnew,bg='lightgreen',fg='black')
        canvas.create_window(125,125,window=newbtn)
        diffbtn=tk.Button(text='Choose Difficulty',command=diffselect,bg='white',fg='black')
        canvas.create_window(125,155,window=diffbtn)
        
    elif int(entry.get())!=ans:
        other=tk.Label(root,text='Try Again, or enter a valid number',bg='midnightblue',fg='white')
        canvas.create_window(125,100,window=other)
        other.after(800,other.destroy)

    else:
        wrong=tk.Label(root,text='Incorrect Format! Type a number.')
        canvas.create_window(125,100,window=wrong)
        other.after(800,other.destroy)

def launchnew():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/normal.py')
    root.destroy()

def diffselect():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/diffselect.py')
    root.destroy()
ans=int(random.randint(1,60))
root=tk.Tk()
canvas=tk.Canvas(root,width=250,height=200,relief='raised',bg='midnightblue')
canvas.pack()

text=tk.Label(root,text='Type a number from 1-60!',bg='midnightblue',fg='white')
text.config(font=('helvetica',14,'bold'))
canvas.create_window(125,35,window=text)

entry=tk.Entry(root)
canvas.create_window(125,70, window=entry)

#def launchnew

chkbtn=tk.Button(text='Check',command=check,bg='lavender',fg='black')
canvas.create_window(125,140,window=chkbtn)

root.title('I N S A N E')
root.mainloop()


