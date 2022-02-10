from tkinter import*
import tkinter.messagebox
w1 =Tk()
w1.title("U1 University Student Managment System")
w1.geometry("400x400")

id1="abcd"
pas="1234"

def myf():
    if(user_id.get()==id1)&(user_pw.get()==pas):
        tkinter.messagebox.showinfo("Notice","LOGIN")
    else:
        tkinter.messagebox.showinfo("Notice","LOGIN fail")
L1 = Label(w1,text = "U1 University Student Managment System")
L1.grid(row=0, column = 0)
L2 = Label(w1,text = "PASSWORD")
L2.grid(row=1, column = 1)
L3 = Label(w1,text = "ID : ")
L3.grid(row=1, column = 0)
user_pw = Entry(w1)
user_pw.grid(row=2, column=1)
user_id = Entry(w1)
user_id.grid(row=2, column=0)
b1 = Button(w1, text="LOGIN", command = myf)
b1.grid(row=3, column=1)

w1.mainloop()
                
