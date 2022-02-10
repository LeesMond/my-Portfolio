from tkinter import*
from tkinter.filedialog import*
from time import*
import calc_functions
import tkinter.messagebox
import table, ball, bat

w1 = Tk()
w1.title("차량 보기")
w1.geometry("1006x550")

la = Label(w1,text="자동차 추천",font=("맑은 고딕",20))

frameList=["SSC1.gif","SSm2.gif","SSp1.gif","SSCC1.gif","SSK91.gif","SSS1.gif","SSU1.gif","SSM11.gif","SSH1.gif"]
photoList=[None]*9
num=0
x_velocity = 10
y_velocity = 0
score_left = 0
score_right = 0
first_serve = True

def joke():
    win = Tk()
    win.title("정보")
    win.geometry("500x300")
    x_velocity = 10
    y_velocity = 0
    score_left = 0
    score_right = 0
    first_serve = True

    pas="Hello World"

    def imf() :

        if(uesr_pw.get()==pas):
            tkinter.messagebox.showinfo("Notice","Hello World")
            win.quit()
            x_velocity = 10
            y_velocity = 0
            score_left = 0
            score_right = 0
            first_serve = True

            window = Tk()
            window.title("MyPong")

            my_table = table.Table(window, net_colour = "white", vertical_net = True)

            my_ball = ball.Ball(table = my_table, x_speed = x_velocity, y_speed = y_velocity, width = 24, height = 24, colour = "white", x_start = 288, y_start = 188)

            bat_L = bat.Bat(table = my_table, width = 15, height = 100, x_posn = 15, y_posn = 150, colour = "white")

            bat_R = bat.Bat(table = my_table, width = 15, height = 100, x_posn = 575, y_posn = 150, colour = "white")

            def game_flow():
                global first_serve
                global score_left
                global score_right

                if (first_serve == True):
                    my_ball.stop_ball()
                    first_serve = False

                bat_L.detect_collision(my_ball)
                bat_R.detect_collision(my_ball)

                if (my_ball.x_posn <=10):
                    my_ball.stop_ball()
                    my_ball.start_position()
                    bat_L.start_position()
                    bat_R.start_position()
                    my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
                    my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
                    score_left = score_left + 1
                    if (score_left >= 10):
                        score_left = "W"
                        score_right = "L"
                    first_serve = True
                    my_table.draw_score(score_left, score_right)

                if (my_ball.x_posn + my_ball.width >= my_table.width - 3):
                    my_ball.stop_ball()
                    my_ball.start_position()
                    bat_L.start_position()
                    bat_R.start_position()
                    my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
                    my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
                    score_right = score_right + 1
                    if (score_right >=10):
                        score_right = "W"
                        score_left = "L"
                    first_serve = True
                    my_table.draw_score(score_left, score_right)
                my_ball.move_next()
                window.after(50, game_flow)

            def restart_game(master):
                global score_left
                global score_right
                my_ball.start_ball(x_speed = x_velocity, y_speed = 0)
                if (score_left == "W" or score_left == "L"):
                    score_left = 0
                    score_right = 0
                my_table.draw_score(score_left, score_right)

            window.bind("a", bat_L.move_up)
            window.bind("z", bat_L.move_down)
            window.bind("'", bat_R.move_up)
            window.bind("/", bat_R.move_down)

            window.bind("<space>", restart_game)

            game_flow()
        
            window.mainloop()
        else:
            tkinter.messagebox.showinfo("Nctice","NAA...I Don't Think so")

    L1 = Label(win,text="2017 자동차 추천",font=("맑은 고딕",20))
    L2 = Label(win,text="MADE BY LEE")
    L3 = Label(win,text="제작 소요 시간: 12시간 조금 넘음")
    L4 = Label(win,text="제작 사용툴:파이썬 3.6.1")
    L5 = Label(win,text="가장 개같던 부분: 윈도우 다시 띄우기")
    uesr_pw = Entry(win)
    b1 = Button(win,text = "PUSH",command=imf)
    L1.pack()
    L2.pack()
    L3.pack()
    L4.pack()
    L5.pack()
    uesr_pw.pack()
    b1.pack()


def clar():
    def click(key):
        if key == "=":
            try:
                result = str(eval(display.get()))
                display.insert(END,"="+result)
            except:
                display.insert(END,"-->오류!")
        elif key == "C":
            display.delete(0,END)
        elif key == constants_list[0]:
            display.insert(END, "3.141592654")
        elif key == constants_list[1]:
            display.insert(END, "300000000")
        elif key == constants_list[2]:
            display.insert(END, "300")
        elif key == constants_list[3]:
            display.insert(END, "149597887.5")
        elif key == functions_list[0]:
            n = display.get()
            display.delete(0,END)
            display.insert(END, calc_functions.factorial(n))
        elif key == functions_list[1]:
            n = display.get()
            display.delete(0,END)
            display.insert(END, calc_functions.to_roman(n))
        elif key == functions_list[2]:
            n = display.get()
            display.delete(0,END)
            display.insert(END, calc_functions.to_binary(n))
        elif key == functions_list[3]:
            n = display.get()
            display.delete(0,END)
            display.insert(END, calc_functions.from_binary(n))
        else:
            display.insert(END,key)
    window =Tk()
    window.title("MyCalculator")

    top_row = Frame(window)
    top_row.grid(row=0, column=0, columnspan=2, sticky=N)

    display = Entry(top_row, width=45, bg="light green")
    display.grid()

    num_pad = Frame(window)
    num_pad.grid(row=1, column=0, sticky=W)

    num_pad_list=[
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0','.','=']

    r=0
    c=0

    for btn_text in num_pad_list:
        def cmd(x=btn_text):
            click(x)
        Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
        c = c+1
        if c>2:
            c=0
            r= r+1


    operator = Frame(window)
    operator.grid(row=1, column=1, sticky=E)

    operator_list = [
    '*','/',
    '+','-',
    '(',')',
    'C']

    r=0
    c=0
    for b in operator_list:
        def cmd(x=b):
            click(x)
        Button(operator, text=b, width=5, command=cmd).grid(row=r, column=c)
        c = c+1
        if c>1:
            c=0
            r= r+1

    constants = Frame(window)
    constants.grid(row=3, column=0, sticky=W)

    constants_list = [
    'π',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)']

    r=0
    c=0

    for btn_text in constants_list:
        def cmd(x=btn_text):
            click(x)
        Button(constants, text=btn_text, width=22, command=cmd).grid(row=r, column=c)
        r = r+1

    functions = Frame(window)
    functions.grid(row=3, column=1, sticky=E)

    functions_list=[
    'facorial (!)',
    '-> roman',
    '-> binary',
    'binary-> 10']

    r=0
    c=0
    for b in functions_list:
        def cmd(x=b):
            click(x)
        Button(functions, text=b, width=13, command=cmd).grid(row=r, column=c)
        r = r+1

def tw():
    mylist = w1.grid_slaves()
    for i in mylist:
        i.destroy()
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
                        num>=2
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
            b1.configure(text="상세보기",command=clear)
        
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
                        num>=3
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
            b1.configure(text="상세보기",command=clear1)
            
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear2)
    labelText = Label(w1,text="차량추천", fg="blue",font=("맑은 고딕",20))

    var = IntVar()
    rd1 = Radiobutton(w1,text="카마로 SS",variable=var, value=1)
    rd2 = Radiobutton(w1,text="말리부",variable=var, value=2)
    rd3 = Radiobutton(w1,text="911 터보 S 카브리올레",variable=var, value=3)
    buttonOK = Button(w1,text="사진보기",command=myf)

    photo1 = PhotoImage(file="SC1.gif")
    photo2 = PhotoImage(file="Sm1.gif")
    photo3 = PhotoImage(file="Sp1.gif")

    labelimage = Label(w1,width=200,height=200,bg="gray",image=None)
    b1 = Button(w1,text="상세보기")


    labelText.pack(padx=5,pady=5)
    rd1.pack(padx=5,pady=5)
    rd2.pack(padx=5,pady=5)
    rd3.pack(padx=5,pady=5)
    buttonOK.pack(padx=5,pady=5)
    labelimage.pack(padx=5,pady=5)
    b1.pack()
def ttw():
    mylist = w1.grid_slaves()
    for i in mylist:
        i.destroy()
    w1.title("30대 차량 추천")
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
                w1.geometry("1455x650")

                la = Label(w1,text="폭스바겐 CC (2018)",font=("맑은 고딕",20))

                frameList=["CC1.gif","CC2.gif","CC3.gif","CC4.gif","CC5.gif","CC6.gif","CC7.gif","CC8.gif"]
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
                        num>=7
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
            
            
            b1.configure(text="상세보기",command=clear)
            
        elif var.get()==2:
            labelimage.configure(image=photo2)
            def clear1():
                mylist = w1.pack_slaves()
                for i in mylist:
                    i.destroy()
                w1.title("차량 보기")
                w1.geometry("1066x530")

                la = Label(w1,text="K9 (2018)",font=("맑은 고딕",20))

                frameList=["K91.gif","K92.gif","K93.gif","K94.gif","K95.gif","K96.gif","K97.gif","K98.gif"]
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear1)
        else:
            labelimage.configure(image=photo3)

            def clear2():
                mylist = w1.pack_slaves()
                for i in mylist:
                    i.destroy()
                w1.title("차량 보기")
                w1.geometry("1066x530")

                la = Label(w1,text="쏘렌토 (2018)",font=("맑은 고딕",20))

                frameList=["S1.gif","S2.gif","S3.gif","S4.gif","S5.gif","S6.gif","S7.gif","S8.gif"]
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear2)
    labelText = Label(w1,text="차량추천", fg="blue",font=("맑은 고딕",20))

    var = IntVar()
    rd1 = Radiobutton(w1,text="CC",variable=var, value=1)
    rd2 = Radiobutton(w1,text="K9",variable=var, value=2)
    rd3 = Radiobutton(w1,text="쏘렌토",variable=var, value=3)
    buttonOK = Button(w1,text="사진보기",command=myf)

    photo1 = PhotoImage(file="SCC1.gif")
    photo2 = PhotoImage(file="SK91.gif")
    photo3 = PhotoImage(file="SS1.gif")

    labelimage = Label(w1,width=200,height=200,bg="gray",image=None)
    b1 = Button(w1,text="상세보기")

    labelText.pack(padx=5,pady=5)
    rd1.pack(padx=5,pady=5)
    rd2.pack(padx=5,pady=5)
    rd3.pack(padx=5,pady=5)
    buttonOK.pack(padx=5,pady=5)
    labelimage.pack(padx=5,pady=5)
    b1.pack()
   
    

def ft():
    mylist = w1.grid_slaves()
    for i in mylist:
        i.destroy()
    w1.title("40대 차량 추천")
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
                w1.geometry("1284x600")

                la = Label(w1,text="후라칸 쿠페 (2018)",font=("맑은 고딕",20))

                frameList=["H1.gif","H2.gif","H3.gif","H4.gif","H5.gif","H6.gif","H7.gif","H8.gif"]
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear)
        elif var.get()==2:
            labelimage.configure(image=photo2)
            def clear1():
                mylist = w1.pack_slaves()
                for i in mylist:
                    i.destroy()
                w1.title("차량 보기")
                w1.geometry("1066x530")

                la = Label(w1,text="모하비 (2018)",font=("맑은 고딕",20))

                frameList=["Mo1.gif","Mo2.gif","Mo3.gif","Mo4.gif","M5.gif","M6.gif","M7.gif","M8.gif"]
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear1)
        else:
            labelimage.configure(image=photo3)
            def clear2():
                mylist = w1.pack_slaves()
                for i in mylist:
                    i.destroy()
                w1.title("차량 보기")
                w1.geometry("1015x600")

                la = Label(w1,text="우루스 (2018)",font=("맑은 고딕",20))

                frameList=["U1.gif","U2.gif","U3.gif","U4.gif","U5.gif","U6.gif","U7.gif","U8.gif"]
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
                        num>=7
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
            b1.configure(text="상세보기",command=clear2)
    labelText = Label(w1,text="차량 추천", fg="blue",font=("맑은 고딕",20))

    var = IntVar()
    rd1 = Radiobutton(w1,text="Lamborghini 후라칸",variable=var, value=1)
    rd2 = Radiobutton(w1,text="모하비",variable=var, value=2)
    rd3 = Radiobutton(w1,text="우르스",variable=var, value=3)
    buttonOK = Button(w1,text="사진보기",command=myf)

    photo1 = PhotoImage(file="SH1.gif")
    photo2 = PhotoImage(file="SMo1.gif")
    photo3 = PhotoImage(file="SU1.gif")

    labelimage = Label(w1,width=200,height=200,bg="gray",image=None)
    b1 = Button(w1,text="상세보기")


    labelText.pack(padx=5,pady=5)
    rd1.pack(padx=5,pady=5)
    rd2.pack(padx=5,pady=5)
    rd3.pack(padx=5,pady=5)
    buttonOK.pack(padx=5,pady=5)
    labelimage.pack(padx=5,pady=5)
    b1.pack()


def clickPrev():
    global num
    num=num+1
    if num > 8:
        num=0
    photo=PhotoImage(file=""+frameList[num])
    pL.configure(image=photo)
    pL.image=photo
    
def clickNext():
    global num
    num=num-1
    if num<8:
        num>=7
    photo=PhotoImage(file=""+frameList[num])
    pL.configure(image=photo)
    pL.image=photo


bP = Button(w1,text="<<이전",command=clickPrev)
bN = Button(w1,text="다음>>",command=clickNext)

photo=PhotoImage(file=frameList[0])

pL=Label(w1,image=photo)
main = Menu(w1)
w1.config(menu=main)
file = Menu(main)
main.add_cascade(label="20대",menu=file)
file.add_command(label="20대",command=tw)
ed = Menu(main)
main.add_cascade(label="30대",menu=ed)
ed.add_command(label="30대",command=ttw)
se = Menu(main)
main.add_cascade(label="40대",menu=se)
se.add_command(label="40대",command=ft)
dd = Menu(main)
main.add_cascade(label="기타",menu=dd)
dd.add_command(label="계산기",command=clar)
dd.add_separator()
dd.add_command(label="크래딧",command=joke)



bP.grid(row=0,column=0)
bN.grid(row=0,column=2)
pL.grid(row=1,column=1)
la.grid(row=0,column=1)
w1.mainloop()




