from tkinter import*
from time import*
from tkinter.filedialog import*
import tkinter.messagebox

w1 = Tk()
w1.title("20대 차량 추천")
w1.geometry("400x450")
num=0

def myf():
    if var.get()==1:
        labelimage.configure(image=photo1)
        def clear():
            mylist = w1.pack_slaves()
            for i in mylist:
                i.destroy()
            w1.title("차량 보기")
            w1.geometry("1006x470")

            la = Label(w1,text="올 뉴 카마로 SS (2018)",font=("맑은 고딕",20))

            frameList=["C1.gif","C2.gif","C3.gif"]
            photoList=[None]*3
            num=0


            def clickPrev():
                global num
                num=num+1
                if num > 2:
                    num=0
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo
    
            def clickNext():
                global num
                num=num-1
                if num<2:
                    num=2
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo


            bP = Button(w1,text="<<이전",command=clickPrev)
            bN = Button(w1,text="다음>>",command=clickNext)

            photo=PhotoImage(file=frameList[0])

            pL=Label(w1,image=photo)


            bP.grid(row=0,column=0)
            bN.grid(row=0,column=2)
            pL.grid(row=1,column=1)
            la.grid(row=2,column=1)
        b1 = Button(w1,text='상세보기',command=clear)
        b1.pack()
        
    elif var.get()==2:
        labelimage.configure(image=photo2)
        def clear1():
            mylist = w1.pack_slaves()
            for i in mylist:
                i.destroy()
            w1.title("차량 보기")
            w1.geometry("1006x400")

            la = Label(w1,text="올 뉴 말리부 (2018)",font=("맑은 고딕",20))

            frameList=["M1.gif","M2.gif","M3.gif","M4.gif"]
            photoList=[None]*4
            num=0


            def clickPrev():
                global num
                num=num+1
                if num > 3:
                    num=0
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo
    
            def clickNext():
                global num
                num=num-1
                if num<3:
                    num=3
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo


            bP = Button(w1,text="<<이전",command=clickPrev)
            bN = Button(w1,text="다음>>",command=clickNext)

            photo=PhotoImage(file=frameList[0])

            pL=Label(w1,image=photo)


            bP.grid(row=0,column=0)
            bN.grid(row=0,column=2)
            pL.grid(row=1,column=1)
            la.grid(row=2,column=1)
        b2 = Button(w1,text="상세보기",command=clear1)
        b2.pack()
            
    else:
        labelimage.configure(image=photo3)
        def clear2():
            mylist = w1.pack_slaves()
            for i in mylist:
                i.destroy()
            w1.title("차량 보기")
            w1.geometry("1107x600")

            la = Label(w1,text="911 터보 S 카브리올레 (2018)",font=("맑은 고딕",20))

            frameList=["p1.gif","p2.gif","p3.gif","p4.gif","p5.gif","p6.gif","p7.gif","p8.gif"]
            photoList=[None]*8
            num=0


            def clickPrev():
                global num
                num=num+1
                if num > 7:
                    num=0
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo
    
            def clickNext():
                global num
                num=num-1
                if num<7:
                    num=8
                photo=PhotoImage(file=""+frameList[num])
                pL.configure(image=photo)
                pL.image=photo


            bP = Button(w1,text="<<이전",command=clickPrev)
            bN = Button(w1,text="다음>>",command=clickNext)

            photo=PhotoImage(file=frameList[0])

            pL=Label(w1,image=photo)


            bP.grid(row=0,column=0)
            bN.grid(row=0,column=2)
            pL.grid(row=1,column=1)
            la.grid(row=2,column=1)
        b3 = Button(w1,text="상세보기",command=clear2)
        b3.pack()
labelText = Label(w1,text="most car", fg="blue",font=("맑은 고딕",20))

var = IntVar()
rd1 = Radiobutton(w1,text="카마로 SS",variable=var, value=1)
rd2 = Radiobutton(w1,text="말리부",variable=var, value=2)
rd3 = Radiobutton(w1,text="911 터보 S 카브리올레",variable=var, value=3)
buttonOK = Button(w1,text="사진보기",command=myf)

photo1 = PhotoImage(file="SC1.gif")
photo2 = PhotoImage(file="Sm1.gif")
photo3 = PhotoImage(file="Sp1.gif")

labelimage = Label(w1,width=200,height=200,bg="pink",image=None)



labelText.pack(padx=5,pady=5)
rd1.pack(padx=5,pady=5)
rd2.pack(padx=5,pady=5)
rd3.pack(padx=5,pady=5)
buttonOK.pack(padx=5,pady=5)
labelimage.pack(padx=5,pady=5)

w1.mainloop()
