from tkinter import *

def con_type(te_val):
    if str(te_val).endswith('.0'):
        return int(te_val)
    elif '.' in str(te_val):
        return float(te_val)
    else:
        return int(te_val)

def ValOver():
    global formatted_value, temp_value
    temp_value_str = str(temp_value)
    if ('.' in temp_value_str and len(temp_value_str) >= 10) or ('.' not in temp_value_str and len(temp_value_str) >= 9):
        formatted_value = f"{temp_value:.3e}"
        display.config(text=str(formatted_value))
    else:
        formatted_value = f"{temp_value:,}"
        display.config(text=str(formatted_value))

def DisplayAdj(new_val):
    global temp_value, formatted_value, stored_value, new_num_check, mem_value

    if new_num_check == True:
        temp_value = 0
        new_num_check = False

    temp_value_str = str(temp_value)

    if new_val == "c":
        temp_value = 0
        stored_value = 0
        formatted_value = f"{temp_value:,}"
        display.config(text=str(formatted_value))
        return
    elif new_val == "pm":
        if float(temp_value) >= 0:
            temp_value = -abs(con_type(temp_value))
            formatted_value = f"{temp_value:,}"
            display.config(text=str(formatted_value))
            return
        else:
            temp_value = abs(con_type(temp_value))
            formatted_value = f"{temp_value:,}"
            display.config(text=str(formatted_value))
            return
    elif new_val == "MS":
            mem_value = temp_value
            return
    elif new_val == "MR":
            temp_value = mem_value
            mem_value = 0
            ValOver()
            return

    if '.' in temp_value_str:
        decimal_part = temp_value_str.split('.')[1]
        decimal_count = len(decimal_part)
    else:
        decimal_count = 0

    if ('.' in temp_value_str and len(temp_value_str) >= 10) or ('.' not in temp_value_str and len(temp_value_str) >= 9):
        return
    else:
        if temp_value == 0 and new_val != ".":
            temp_value = new_val
        elif new_val == ".":
            if decimal_count == 0:
                temp_value = str(temp_value) + "."
        else:
            temp_value = str(temp_value) + str(new_val)

    try:
        if "." in str(temp_value):
            formatted_value = "{:,.{prec}f}".format(float(temp_value), prec=len(temp_value.split('.')[1]))
        else:
            formatted_value = "{:,}".format(int(temp_value))
    except ValueError:
        formatted_value = temp_value

    display.config(text=str(formatted_value))

def MathReq(type):
    global temp_value, stored_value, math_request, new_num_check
    stored_value = temp_value
    new_num_check = True
    if type == "+":
        math_request = 1
    if type == "-":
        math_request = 2
    if type == "*":
        math_request = 3
    if type == r"/":
        math_request = 4
        return

def Result():
    global temp_value, stored_value, formatted_value, math_request
    stored_value = con_type(stored_value)
    temp_value = con_type(temp_value)

    try:
        if math_request == 1:
            temp_value = stored_value + temp_value
        elif math_request == 2:
            temp_value = stored_value - temp_value
        elif math_request == 3:
            temp_value = stored_value * temp_value
        elif math_request == 4:
            temp_value = stored_value / temp_value
            temp_value = con_type(temp_value)
    except ZeroDivisionError:
        display.config(text="Can't div 0")
        return

    ValOver()

main_window = Tk()
mem_value = 0
stored_value = 0
temp_value = 0
math_request = 0
new_num_check = False
formatted_value = f"{temp_value:,}"

try:
    photo = PhotoImage(file="PenCookie.png")
    main_window.iconphoto(True, photo)
except Exception as e:
    print(f"Error loading image: {e}")

main_window.geometry("440x575")
main_window.resizable(False, False)
main_window.title("Pending Calculator")

display = Label(main_window,text=str(formatted_value),font=("Times New Roman",60,"bold"),anchor=E,
                width=9,height=1,relief=GROOVE,bd=4)
button_1 = Button(main_window, text="1", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE,bd=8, command=lambda: DisplayAdj(1))
button_2 = Button(main_window, text="2", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(2))
button_3 = Button(main_window, text="3", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(3))
button_4 = Button(main_window, text="4", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(4))
button_5 = Button(main_window, text="5", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(5))
button_6 = Button(main_window, text="6", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(6))
button_7 = Button(main_window, text="7", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(7))
button_8 = Button(main_window, text="8", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(8))
button_9 = Button(main_window, text="9", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(9))
button_0 = Button(main_window, text="0", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj(0))
button_div = Button(main_window, text=r"/", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: MathReq(r"/"))
button_mul = Button(main_window, text="x", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: MathReq("*"))
button_min = Button(main_window, text="-", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: MathReq("-"))
button_plu = Button(main_window, text="+", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: MathReq("+"))
button_equ = Button(main_window, text="=", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, bg="#ADD8E6", command=lambda: Result())
button_MS = Button(main_window, text="MS", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj("MS"))
button_MR = Button(main_window, text="MR", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj("MR"))
button_clear = Button(main_window, text="C", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj("c"))
button_PluMin = Button(main_window, text="+/-", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj("pm"))
button_deci = Button(main_window, text=".", font=(
    "Times New Roman", 30), width=4, height=1, relief=GROOVE, bd=8, command=lambda: DisplayAdj("."))


display.place(x=0, y=0,width=440,height=100)
button_MS.place(x=0,y=100)
button_MR.place(x=110,y=100)
button_clear.place(x=220,y=100)
button_1.place(x=0, y=195)
button_2.place(x=110, y=195)
button_3.place(x=220, y=195)
button_4.place(x=0, y=290)
button_5.place(x=110, y=290)
button_6.place(x=220, y=290)
button_7.place(x=0, y=385)
button_8.place(x=110, y=385)
button_9.place(x=220, y=385)
button_0.place(x=110, y=480)
button_div.place(x=330,y=100)
button_mul.place(x=330,y=195)
button_min.place(x=330,y=290)
button_plu.place(x=330,y=385)
button_PluMin.place(x=0,y=480)
button_deci.place(x=220,y=480)
button_equ.place(x=330,y=480)

main_window.mainloop()