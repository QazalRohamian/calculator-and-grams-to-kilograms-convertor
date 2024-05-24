from tkinter import *


#calculator

win = Tk()

win.title("calculator")
win.geometry('650x500')
operator = ""
text_input = StringVar()

ent1 = Entry(win, font=36, bg="#dfe6e9", textvariable= text_input)
ent1.grid(row=0 , column=0, columnspan=4, padx=15, pady=15, ipadx=40, ipady=20)

def click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clean():
    global operator
    operator = ""
    text_input.set("")    

def equalbtn():
    global operator
    equal = str(eval(operator))
    text_input.set(equal)
    operator = ""

num1 = Button(win, text="1", font=33, bg="#ffeaa7", command=lambda:click(1))
num1.grid(row=1 ,column=0, ipadx=14, ipady=14)
num2 = Button(win, text="2", font=33, bg="#ffeaa7", command=lambda:click(2))
num2.grid(row=1 ,column=1, ipadx=14, ipady=14)
num3 = Button(win, text="3", font=33, bg="#ffeaa7",command=lambda:click(3) )
num3.grid(row=1 ,column=2, ipadx=14, ipady=14)
plus_btn = Button(win, text="+", font=33, bg="#ffeaa7", command=lambda:click("+"))
plus_btn.grid(row=1 ,column=3, ipadx=14, ipady=14)
num4 = Button(win, text="4", font=33, bg="#ffeaa7", command=lambda:click(4))
num4.grid(row=2 ,column=0, ipadx=14, ipady=14, padx=10, pady=10)
num5 = Button(win, text="5", font=33, bg="#ffeaa7", command=lambda:click(5))
num5.grid(row=2 ,column=1, ipadx=14, ipady=14, padx=10, pady=10)
num6 = Button(win, text="6", font=33, bg="#ffeaa7", command=lambda:click(6))
num6.grid(row=2 ,column=2, ipadx=14, ipady=14,padx=10, pady=10)
minus_btn = Button(win, text="-", font=33, bg="#ffeaa7", command=lambda:click("-"))
minus_btn.grid(row=2 ,column=3, ipadx=14, ipady=14, padx=10, pady=10)
num7 = Button(win, text="7", font=33, bg="#ffeaa7",command=lambda:click(7))
num7.grid(row=3 ,column=0, ipadx=14, ipady=14,padx=10, pady=10)
num8 = Button(win, text="8", font=33, bg="#ffeaa7", command=lambda:click(8))
num8.grid(row=3 ,column=1, ipadx=14, ipady=14,padx=10, pady=10)
num9 = Button(win, text="9", font=33, bg="#ffeaa7", command=lambda:click(9))
num9.grid(row=3 ,column=2, ipadx=14, ipady=14,padx=10, pady=10)
zarb_btn = Button(win, text="*", font=33, bg="#ffeaa7", command=lambda:click("*"))
zarb_btn.grid(row=3 ,column=3, ipadx=14, ipady=14,padx=10, pady=10)
clear_btn = Button(win, text="c", font=33, bg="#ff7675", command=clean)
clear_btn.grid(row=4 ,column=0, ipadx=14, ipady=14,padx=10, pady=10)
num0 = Button(win, text="0", font=33, bg="#ffeaa7", command=lambda:click(0))
num0.grid(row=4 ,column=1, ipadx=14, ipady=14,padx=10, pady=10)
equal_btn = Button(win, text="=", font=33, bg="#55efc4" , command=equalbtn)
equal_btn.grid(row=4 ,column=2, ipadx=14, ipady=14,padx=10, pady=10)
divide_btn = Button(win, text="/", font=33, bg="#ffeaa7", command=lambda:click("/"))
divide_btn.grid(row=4 ,column=3, ipadx=14, ipady=14,padx=10, pady=10)




#grams to kilograms

lbl1 = Label(win, text="please enter number in grams", font=15)
lbl1.grid(row=0 , column=5, columnspan=2, padx=5, pady=5)

ent2 = Entry(win,font=36, bg="#dfe6e9")
ent2.grid(row=1 , column=5, columnspan=2, padx=6, pady=8, ipadx=40, ipady=20)

lbl2 = Label(win, text="kilograms", font=10)
lbl2.grid(row=2 , column=5, padx=5)

lbl3 = Label(win, text="grams", font=10)
lbl3.grid(row=2 , column=6, padx=5)

txt1= Text(win, width=10, height=5 , bg="#fdcb6e", font=36)
txt1.grid(row=3 , column=5, padx=5)

txt2= Text(win, width=10, height=5, bg="#fdcb6e", font=36)
txt2.grid(row=3 , column=6, padx=5)

def converse():
    kg = int(ent2.get())/1000
    g = int(ent2.get())
    txt1.delete(1.0, END)
    txt2.delete(1.0, END)
    txt1.insert(INSERT, kg)
    txt2.insert(INSERT, g)


converse_btn = Button(win, text="converse", font=15, bg="#ff7675", command=converse)
converse_btn.grid(row=4, column=5, columnspan=2, ipadx=10, ipady=10)
win.mainloop()