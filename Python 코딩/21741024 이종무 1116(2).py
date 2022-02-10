from tkinter import*
import tkinter.messagebox

main = Tk()
main.title("게임선택 프로그램")
main.geometry("400x400")
def eed():
    sub1 = Tk()
    sub1.title("Need For Speed")
    sub1.geometry("300x250")
def ro():
    sub2 = Tk()
    sub2.title("Project Car")
    sub2.geometry("300x250")
def he():
    sub3 = Tk()
    sub3.title("The Cerw")
    sub3.geometry("300x250")

B1 = Button(main,text="Need For Speed",command=eed)
B2 = Button(main,text="Project Car",command=ro)
B3 = Button(main,text="The Cerw",command=he)

B1.pack()
B2.pack()
B3.pack()

main.mainloop()
