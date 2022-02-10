#유원회사 사원 정보 프로그램

#입력 인터페이스-GUI

from tkinter import*
import tkinter.messagebox

w1 = Tk()
w1.title("유원사 사원 정보 프로그램")
w1.geometry("500x500")

def myf1():
    number = E1.get()
    name = E2.get()
    adress = E3.get()
    tell = E4.get()
    tkinter.messagebox.showinfo("알림","저장되었습니다.")
def myf2 ():
    w2 = Tk()
    w2.title("사원정보 출력")
    w2.geometry("400x300")
    number = E1.get()
    name = E2.get()
    adress = E3.get()
    tell = E4.get()
    ttt = "사원번호 : "+number+"\n이름 : "+name+"\n주소 : "+adress+"\n연락처 : "+tell
    l1 = Label(w2,text=ttt)
    
    l1.grid(row=0)
    
    
L1 = Label(w1,text=("사원번호 : "))
E1 = Entry(w1)
L2 = Label(w1,text=("이름 : "))
E2 = Entry(w1)
L3 = Label(w1,text=("주소 : "))
E3 = Entry(w1)
L4 = Label(w1,text=("연락처 : "))
E4 = Entry(w1)

b1 = Button(w1,text=("사원 정보 등록"),command=myf1)
b2 = Button(w1,text=("등록 정보 미리보기"),command=myf2)
#처리기능 - 입력한 자료를 저장, 저장한 자료를 출력하는 기능

#출력 인터페이스 - GUI
L1.grid(row=0, column=0)
E1.grid(row=0, column=1)
L2.grid(row=1, column=0)
E2.grid(row=1, column=1)
L3.grid(row=2, column=0)
E3.grid(row=2, column=1)
L4.grid(row=3, column=0)
E4.grid(row=3, column=1)
b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
w1.mainloop()
