from tkinter import*
import tkinter.messagebox

w1 = Tk()
w1.title("성적 계산 프로그램")
w1.geometry("250x130")

def myf3(a):
     if (a<= 60):
        return "F"
     elif (a <=70):
        return "D"
     elif (a <=80):
        return "C"
     elif (a <=90):
        return "B"
     elif (a <=100):
        return "A"
        
        
def myf1():
    number = E1.get()
    name = E2.get()
    sub1 = E3.get()
    sub2 = E4.get()
    sub3 = E5.get()
    tkinter.messagebox.showinfo("알림","저장되었습니다.")
def myf2():
    w2 = Tk()
    w2.title("성적 정보 출력")
    w2.geometry("400x300")
    number = E1.get()
    name = E2.get()
    sub1 = E3.get()
    sub2 = E4.get()
    sub3 = E5.get()
    a = int(sub1)
    a1 = myf3(a)
   
    b = int(sub2)
    a2 = myf3(b)
    
    c = int(sub3)
    a3 = myf3(c)
    
    ttt = "학번 : "+number+"\n이름 : "+name+"\n파이썬 학점 : "+a1+"\n HTML 학점 : "+a2+"\n전장기초 학점 : "+a3
    l1 = Label(w2,text=ttt)
    l1.grid(row=0)
            

L1 = Label(w1,text=("학번 : "))
E1 = Entry(w1)
L2 = Label(w1,text=("이름 : "))
E2 = Entry(w1)
L3 = Label(w1,text=("파이썬 성적 입력 : "))
E3 = Entry(w1)
L4 = Label(w1,text=("HTML 성적 입력 : "))
E4 = Entry(w1)
L5 = Label(w1,text=("전장기초 성적 입력 : "))
E5 = Entry(w1)
B1 = Button (w1,text=("입력"),command=myf1)
B2 = Button (w1,text=("성적 결과.."),command=myf2)

L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
L3.grid(row=2,column=0)
E3.grid(row=2,column=1)
L4.grid(row=3,column=0)
E4.grid(row=3,column=1)
L5.grid(row=4,column=0)
E5.grid(row=4,column=1)
B1.grid(row=5,column=0)
B2.grid(row=5,column=1)

w1.mainloop()
