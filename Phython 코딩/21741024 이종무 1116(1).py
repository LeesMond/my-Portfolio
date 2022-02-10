from tkinter import*
import tkinter.messagebox

w1 = Tk()
w1.title("관리자 로그인")
w1.geometry("250x150")

def login():
    pa = "dlwhdan"
    if pa == E1.get():
        tkinter.messagebox.showinfo("결과","로그인 되었습니다")
        w2 = Tk()
        w2.title("가계부 로그인")
        w2.geometry("400x300")
        def add():
            sub1 = E8.get()
            sub2 = E9.get()
            sub3 = E10.get()
            sub4 = E11.get()
            sub5 = E12.get()

            rrr=  int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5)
            L5 = Label(w2,text=rrr)
            L6 = Label(w2,text="합   계 : ")
            L5.grid(row=7,column=3)
            L6.grid(row=7,column=1)



             
        L2 = Label(w2,text="   가   계   부   ")
        L3 = Label(w2,text="날   짜:")
        E2 = Entry(w2)
        L4 = Label(w2,text="내   용:")
        E3 = Entry(w2)
        E4 = Entry(w2)
        E5 = Entry(w2)
        E6 = Entry(w2)
        E7 = Entry(w2)
        E8 = Entry(w2)
        E9 = Entry(w2)
        E10 = Entry(w2)
        E11 = Entry(w2)
        E12 = Entry(w2)
        B2 = Button(w2, text="합계 출력",command=add)
        
        L2.grid(row=0,column=2)
        L3.grid(row=1,column=1)
        E2.grid(row=1,column=2)
        L4.grid(row=2,column=1)
        E3.grid(row=2,column=2)
        E4.grid(row=3,column=2)
        E5.grid(row=4,column=2)
        E6.grid(row=5,column=2)
        E7.grid(row=6,column=2)
        E8.grid(row=2,column=3)
        E9.grid(row=3,column=3)
        E10.grid(row=4,column=3)
        E11.grid(row=5,column=3)
        E12.grid(row=6,column=3)
        B2.grid(row=8,column=2)

    else:
        tkinter.messagebox.showinfo("결과","다시 로그인 해주세요")


L1 = Label(w1,text="관리자 로그인\n 비밀번호를 입력해주세요")
E1 = Entry(w1)
B1 = Button(w1,text="로그인",command=login)


L1.pack()
E1.pack()
B1.pack()

w1.mainloop()
