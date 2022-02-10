#유원대 통합 정보 시스템 GUI

from tkinter import*
import tkinter.messagebox
w1 = Tk()
w1.title("U1 Univercity student managment system")
w1.geometry("400x400")

id1 ="abcd"
pas = "1234"

def myf() :
    if (uesr_id.get()==id1)&(uesr_pw.get()==pas):
        tkinter.messagebox.showinfo("Notice","LOGIN")
    else:
        tkinter.messagebox.showinfo("Nctice","LOGIN fail")

L1 = Label(w1,text = "U1 Univercity student managment system")
L1.grid(row=0,column=0)
L2 = Label(w1, text = "PASSWORD : ")
L2.grid(row=1,column=1)
L3 = Label(w1, text = "ID : ")
L3.grid(row=1,column=0)
uesr_pw = Entry(w1)
uesr_pw.grid(row=2,column=1)
uesr_id = Entry(w1)
uesr_id.grid(row=2,column=0)
b1 = Button(w1,text = "LOGIN",command=myf)
b1.grid(row=3,column=1)


w1.mainloop()
