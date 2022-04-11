from tkinter import*
from time import*


w1 = Tk()
w1.title("차량 보기")
w1.geometry("700x500")

frameList=["0.gif","1.gif","2.gif","3.gif","4.gif"]
photoList=[None]*5
num=0


def clickPrev():
    global num
    num=num+1
    if num > 4:
        num=0
    photo=PhotoImage(file=""+frameList[num])
    pL.configure(image=photo)
    pL.image=photo
    
def clickNext():
    global num
    num=num-1
    if num<4:
        num=4
    photo=PhotoImage(file=""+frameList[num])
    pL.configure(image=photo)
    pL.image=photo
#w1.bind("<prior>",pageUp)
#w1.bind("<Next>",pageDown)

bP = Button(w1,text="<<이전",command=clickPrev)
bN = Button(w1,text="다음>>",command=clickNext)

photo=PhotoImage(file=frameList[0])

pL=Label(w1,image=photo)

bP.place(x=250,y=10)
bN.place(x=400,y=10)
pL.place(x=15,y=50)
w1.mainloop()
