import tkinter
from tkinter import *
import time
root = Tk()
root.geometry("400x400+500+100")
root.resizable(False,False)
root.title("login")
root.iconbitmap("download.ico")
frame1 = Frame(root)
frame1.place(x=0,y=0,width=400,height=200)
images1 = PhotoImage(file="images1.png")
imagelabel = Label(frame1,image=images1)
imagelabel.place(x=100,y=0,width=200,height=200)
# entry frame
framentry = Frame(root,background="#fff")
framentry.place(x=0,y=200,width=400,height=200)
# ===================add ee username and label and some entry=====================
label1 = Label(framentry,text="username:",fg="#222",font=("Courier",13),bg="#fff")
label1.place(x=20,y=40)
en1 = Entry(framentry)
en1.place(x=120,y=40,width=200,height=25)
label2 = Label(framentry,text="lastname:",fg="#222",font=("Courier",13),bg="#fff")
label2.place(x=20,y=80)
en2 = Entry(framentry)
en2.place(x=120,y=80,width=200,height=25)
label3 = Label(framentry,text="age:",fg="#222",font=("Courier",13),bg="#fff")
label3.place(x=20,y=120)
en3 = Spinbox(framentry,from_=0,to=50)
en3.place(x=120,y=120,width=200,height=25)

def chekingfunction():
   
    from tkinter import messagebox
    import subprocess
    tahas = int(en3.get())
    if tahas <= 18:
        messagebox.showerror("error","you should be greather than 18 age")
    else:
        subprocess.Popen(["python","sec.py"])
        def destroyinapp():
             root.destroy()
    destroyinapp()
buttons = Button(framentry,text="send",fg="white",bg="red",cursor="hand2",command=chekingfunction)
buttons.place(x=100,y=160,height=30,width=200)
root.mainloop()