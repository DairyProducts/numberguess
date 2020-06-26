from tkinter import *
import os
master=Tk()
w=Label(master,text='Choose your difficulty to start a game!',font=('calibri',11))
w.place(x=125,y=25,anchor=CENTER)
w.pack

def gabe():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/tetris.mp4')

def stop():
    master.destroy()

def easy():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/easy.py')
    master.destroy()

def normal():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/normal.py')
    master.destroy()

def hard():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/hard.py')
    master.destroy()

def insane():
    os.startfile(r'C:/Users/2007d/Desktop/Guess the Number-CODEPACK/insane.py')
    master.destroy()

btneasy=Button(master,text='         Easy        ',bg='palegreen',fg='black',command=easy)
btneasy.pack()
btneasy.place(x=125,y=65,anchor=CENTER)

btnnormal=Button(master,text='      Normal      ',bg='khaki',fg='black',command=normal)
btnnormal.pack()
btnnormal.place(x=125,y=95,anchor=CENTER)

btnhard=Button(master,text='         Hard        ',bg='sandybrown',fg='black',command=hard)
btnhard.pack()
btnhard.place(x=125,y=125,anchor=CENTER)

btninsane=Button(master,text='        Insane       ',bg='salmon',fg='black',command=insane)
btninsane.pack()
btninsane.place(x=125,y=155,anchor=CENTER)

btngabe=Button(master,text="Don't click me!",command=gabe,bg='cornflowerblue',fg='white')
btngabe.pack()
btngabe.place(x=125,y=185,anchor=CENTER)

btnclose=Button(master,text=" Close Window ",command=stop,bg='gray',fg='white')
btnclose.pack()
btnclose.place(x=125,y=215,anchor=CENTER)

master.title('Difficulty')
master.geometry('250x250+5+5')
master.mainloop()
