
# Python calculator

from tkinter import *


# Functions

def click(event):
    global input_value
    action = event.widget.cget("text")
    print(action)
    
    if action == "=":
        pass
    elif action == "+":
        pass
    elif action == "-":
        pass
    elif action == "X":
        pass
    elif action == "/":
        pass
    elif action == "C":
        input_value.set("")
        input_screen.update()
    else:
        input_value.set(input_value.get() + action)
        input_screen.update()



base = Tk()

base.geometry("308x500")
base.maxsize(width=308,height=500)
base.minsize(width=308,height=500)

base.title("Calculator")
base.config(bg="black")

# base.wm_iconbitmap("calculator_icon.ico")

input_value = StringVar()
input_value.set("")

input_screen = Entry(base, textvariable=input_value, font="Digital-7 40 bold",width=10)
input_screen.grid(row=0,column=0,pady=13, padx=1,ipady=2,columnspan=4)

button_frame = Frame(base, bg="lightgrey")
button_frame.grid(row=1, column=0, columnspan=4, pady=2, padx=4)


b7 = Button(button_frame, text="7",font="Digital-7 30 bold",padx=10)
b7.grid(row=1,column=0,padx=1,pady=1)
b7.bind("<Button-1>",click)

b8 = Button(button_frame, text="8",font="Digital-7 30 bold",padx=10)
b8.grid(row=1,column=1,padx=1,pady=1)
b8.bind("<Button-1>",click)

b9 = Button(button_frame, text="9",font="Digital-7 30 bold",padx=10)
b9.grid(row=1,column=2,padx=1,pady=1)
b9.bind("<Button-1>",click)

bdiv = Button(button_frame, text="/",font="Digital-7 30 bold",padx=10)
bdiv.grid(row=1,column=3,pady=1)
bdiv.bind("<Button-1>",click)

b4 = Button(button_frame, text="4",font="Digital-7 30 bold",padx=10)
b4.grid(row=2,column=0,padx=1,pady=1)
b4.bind("<Button-1>",click)

b5 = Button(button_frame, text="5",font="Digital-7 30 bold",padx=10)
b5.grid(row=2,column=1,padx=1,pady=1)
b5.bind("<Button-1>",click)

b6 = Button(button_frame, text="6",font="Digital-7 30 bold",padx=10)
b6.grid(row=2,column=2,padx=1,pady=1)
b6.bind("<Button-1>",click)

bmul = Button(button_frame, text="x",font="Digital-7 30 bold",padx=5)
bmul.grid(row=2,column=3,pady=1)
bmul.bind("<Button-1>",click)

b1 = Button(button_frame, text="1",font="Digital-7 30 bold",padx=10)
b1.grid(row=3,column=0,padx=1,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(button_frame, text="2",font="Digital-7 30 bold",padx=10)
b2.grid(row=3,column=1,padx=1,pady=1)
b2.bind("<Button-1>",click)

b3 = Button(button_frame, text="3",font="Digital-7 30 bold",padx=10)
b3.grid(row=3,column=2,padx=1,pady=1)
b3.bind("<Button-1>",click)

badd = Button(button_frame, text="+",font="Digital-7 30 bold",padx=5)
badd.grid(row=3,column=3,pady=1)
badd.bind("<Button-1>",click)

bper = Button(button_frame, text="%",font="Digital-7 30 bold",padx=4)
bper.grid(row=4,column=0,padx=1,pady=1)
bper.bind("<Button-1>",click)

b0 = Button(button_frame, text="0",font="Digital-7 30 bold",padx=10)
b0.grid(row=4,column=1,padx=1,pady=1)
b0.bind("<Button-1>",click)

bdot = Button(button_frame, text=".",font="Digital-7 30 bold",padx=15)
bdot.grid(row=4,column=2,padx=1,pady=1)
bdot.bind("<Button-1>",click)

beq = Button(button_frame, text="=",font="Digital-7 30 bold",padx=5,bg="lightblue")
beq.grid(row=4,column=3,pady=1)
beq.bind("<Button-1>",click)

base.mainloop()