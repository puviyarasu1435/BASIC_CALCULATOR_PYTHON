from tkinter import *
import tkinter as tk
top = tk.Tk()

top.title("calculator")
def work(num):
    global operator
    operator=operator+str(num)
    text.set(operator)
def cls():
    global operator
    operator=""
    text.set("")
def answer():
    global operator
    ans=str(eval(operator)) 
    text.set(ans)
    operator=""
operator=""
text=StringVar()
enter=tk.Entry(top,bd=5,textvariable=text,width=40,justify="right").grid(columnspan=4)

B = tk.Button(top, text="7",padx=20,pady=10,command=lambda:work(7))
B.grid(row=1,column=0)
B = tk.Button(top, text="8",padx=20,pady=10,command=lambda:work(8))
B.grid(row=1,column=1)
B = tk.Button(top, text="9",padx=20,pady=10,command=lambda:work(9))
B.grid(row=1,column=2)
B = tk.Button(top, text="+",padx=20,pady=10,command=lambda:work("+"))
B.grid(row=1,column=3)

B = tk.Button(top, text="4",padx=20,pady=10,command=lambda:work(4))
B.grid(row=2,column=0)
B = tk.Button(top, text="5",padx=20,pady=10,command=lambda:work(5))
B.grid(row=2,column=1)
B = tk.Button(top, text="6",padx=20,pady=10,command=lambda:work(6))
B.grid(row=2,column=2)
B = tk.Button(top, text="-",padx=20,pady=10,command=lambda:work("-"))
B.grid(row=2,column=3)

B = tk.Button(top, text="3",padx=20,pady=10,command=lambda:work(3))
B.grid(row=3,column=0)
B = tk.Button(top, text="2",padx=20,pady=10,command=lambda:work(2))
B.grid(row=3,column=1)
B = tk.Button(top, text="1",padx=20,pady=10,command=lambda:work(1))
B.grid(row=3,column=2)
B = tk.Button(top, text="*",padx=20,pady=10,command=lambda:work("*"))
B.grid(row=3,column=3)


B = tk.Button(top, text="0",padx=20,pady=10,command=lambda:work(0))
B.grid(row=4,column=0)
B = tk.Button(top, text="c",padx=20,pady=10,command=cls)
B.grid(row=4,column=1)
B = tk.Button(top, text="=",padx=20,pady=10,command=answer)
B.grid(row=4,column=2)
B = tk.Button(top, text="/",padx=20,pady=10,command=lambda:work("/"))
B.grid(row=4,column=3)


top.mainloop()