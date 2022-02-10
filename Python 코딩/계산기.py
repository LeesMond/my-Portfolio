from tkinter import*
import calc_functions

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

window.mainloop()
