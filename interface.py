from tkinter import *
from tkinter import font
import math

def change_page(frame):
    frame.tkraise()

def button_input(char):
    ipt = str(entry.get())
    if "Syntax Error" in ipt:
        ipt = ipt.replace("Syntax Error","")
    numbers = [str(i) for i in range(10)] + [".","(",")"]
    if str(char) not in numbers:
        if len(ipt) == 0:
            entry.delete(0, END)
            entry.insert(0, ipt)
        elif ipt[-1] not in numbers:
            ipt = ipt[:-1] + str(char)
            entry.delete(0, END)
            entry.insert(0, ipt)
        elif ipt[-1] in numbers:
            entry.delete(0, END)
            entry.insert(0, ipt + str(char))
    else:
        if str(char) == ".":
            if "." not in ipt:
                entry.delete(0, END)
                entry.insert(0, ipt + str(char))
            else:
                pass
        else:
            entry.delete(0, END)
            entry.insert(0, ipt + str(char))

def input_brackets():
    global brackets_stack
    ipt = str(entry.get())
    if len(ipt) == 0 or ipt == "Syntax Error" or set(ipt) == {"("}:
        entry.delete(0, END)
        entry.insert(0, ipt + "(")
        brackets_stack.append("(")
    elif len(ipt) > 0:
        if len(brackets_stack) > 0:
            entry.delete(0, END)
            entry.insert(0, ipt + ")")
            brackets_stack.pop()
        else:
            entry.delete(0, END)
            entry.insert(0, ipt + "(")
            brackets_stack.append("(")

def clear():
    global brackets_stack
    brackets_stack= []
    entry.delete(0, END)

def last_ans():
    global history
    if len(history) > 0:
        ipt = entry.get()
        ans = str(history[-1])
        entry.delete(0, END)
        entry.insert(0, str(ipt) + ans)

def equal():
    try:
        ipt = str(entry.get())
        if "x" in ipt:
            ipt = ipt.replace("x", "*")
        if "÷" in ipt:
            ipt = ipt.replace("÷", "/")
        ipt = eval(ipt)
        entry.delete(0, END)
        entry.insert(0, str(ipt))
        history.append(ipt)
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Can't divide by zero")
    except:
        entry.delete(0, END)
        entry.insert(0, "Syntax Error")

def first_page():
    global window, entry, history, f1, f2, revert_button
    _width = 4
    _pady = 4
    button_1 = Button(f1, text="1", width=_width, pady=_pady, command=lambda: button_input(1),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_2 = Button(f1, text="2", width=_width, pady=_pady, command=lambda: button_input(2),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_3 = Button(f1, text="3", width=_width, pady=_pady, command=lambda: button_input(3),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_4 = Button(f1, text="4", width=_width, pady=_pady, command=lambda: button_input(4),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_5 = Button(f1, text="5", width=_width, pady=_pady, command=lambda: button_input(5),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_6 = Button(f1, text="6", width=_width, pady=_pady, command=lambda: button_input(6),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_7 = Button(f1, text="7", width=_width, pady=_pady, command=lambda: button_input(7),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_8 = Button(f1, text="8", width=_width, pady=_pady, command=lambda: button_input(8),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_9 = Button(f1, text="9", width=_width, pady=_pady, command=lambda: button_input(9),
                      font=font.Font(family = 'Helvetica', size=20))
    button_0 = Button(f1, text="0", width=_width, pady=_pady, command=lambda: button_input(0),
                      font=font.Font(family = 'Helvetica', size = 20))
    button_add = Button(f1, text="+", width=_width, pady=_pady, command=lambda: button_input("+"),
                        font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_subs = Button(f1, text="-", width=_width, pady=_pady, command=lambda: button_input("-"),
                         font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_mult = Button(f1, text="x", width=_width, pady=_pady, command=lambda: button_input("x"),
                         font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_div = Button(f1, text="÷", width=_width, pady=_pady, command=lambda: button_input("÷"),
                        font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_brackets = Button(f1, text="( )", width=_width, pady=_pady, command=input_brackets,
                             font=font.Font(family='Helvetica', size=20), fg="green")
    button_point = Button(f1, text=".", width=_width, pady=_pady, command=lambda: button_input("."),
                          font=font.Font(family = 'Helvetica', size = 20))
    button_revert = Button(f1, image=revert_button, command= lambda: change_page(f2))
    button_equal = Button(f1, text="=", width=_width, pady=_pady, command= equal,
                          font=font.Font(family = 'Helvetica', size = 20), fg="white", bg="green")
    button_clear = Button(f1, text="C", width=_width, pady=_pady, command= clear,
                          font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_ans = Button(f1, text="Ans", width=_width, pady=_pady, command= last_ans,
                        font=font.Font(family = 'Helvetica', size = 20), fg="white", bg="red")
    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_0.grid(row=5, column=1)
    button_add.grid(row=1, column=3)
    button_subs.grid(row=2, column=3)
    button_mult.grid(row=3, column=3)
    button_div.grid(row=4, column=3)
    button_brackets.grid(row=1,column=2)
    button_revert.grid(row=1,column=1)
    button_point.grid(row=5,column=2)
    button_equal.grid(row=5, column=3)
    button_clear.grid(row=1, column=0)
    button_ans.grid(row=5,column=0)

def second_page():
    global window, entry, history, f2, f1, revert_button
    _width = 4
    _pady = 4
    button_1 = Button(f2, text="1", width=_width, pady=_pady, command=lambda: button_input(1),
                      font=font.Font(family='Helvetica', size=20))
    button_2 = Button(f2, text="2", width=_width, pady=_pady, command=lambda: button_input(2),
                      font=font.Font(family='Helvetica', size=20))
    button_3 = Button(f2, text="3", width=_width, pady=_pady, command=lambda: button_input(3),
                      font=font.Font(family='Helvetica', size=20))
    button_4 = Button(f2, text="4", width=_width, pady=_pady, command=lambda: button_input(4),
                      font=font.Font(family='Helvetica', size=20))
    button_5 = Button(f2, text="5", width=_width, pady=_pady, command=lambda: button_input(5),
                      font=font.Font(family='Helvetica', size=20))
    button_6 = Button(f2, text="6", width=_width, pady=_pady, command=lambda: button_input(6),
                      font=font.Font(family='Helvetica', size=20))
    button_7 = Button(f2, text="7", width=_width, pady=_pady, command=lambda: button_input(7),
                      font=font.Font(family='Helvetica', size=20))
    button_8 = Button(f2, text="8", width=_width, pady=_pady, command=lambda: button_input(8),
                      font=font.Font(family='Helvetica', size=20))
    button_9 = Button(f2, text="9", width=_width, pady=_pady, command=lambda: button_input(9),
                      font=font.Font(family='Helvetica', size=20))
    button_0 = Button(f2, text="0", width=_width, pady=_pady, command=lambda: button_input(0),
                      font=font.Font(family='Helvetica', size=20))
    button_a = Button(f2, text="a", width=_width, pady=_pady, command=lambda: button_input("+"),
                        font=font.Font(family='Helvetica', size=20), fg="green")
    button_s = Button(f2, text="s", width=_width, pady=_pady, command=lambda: button_input("-"),
                         font=font.Font(family='Helvetica', size=20), fg="green")
    button_q = Button(f2, text="q", width=_width, pady=_pady, command=lambda: button_input("x"),
                         font=font.Font(family='Helvetica', size=20), fg="green")
    button_f = Button(f2, text="f", width=_width, pady=_pady, command=lambda: button_input("÷"),
                        font=font.Font(family='Helvetica', size=20), fg="green")
    button_mod = Button(f2, text="%", width=_width, pady=_pady, command=lambda: button_input("%"),
                        font=font.Font(family='Helvetica', size=20), fg="green")
    button_point = Button(f2, text=".", width=_width, pady=_pady, command=lambda: button_input("."),
                          font=font.Font(family='Helvetica', size=20))
    button_revert = Button(f2, image=revert_button, command= lambda: change_page(f1))
    button_equal = Button(f2, text="=", width=_width, pady=_pady, command= equal,
                          font=font.Font(family='Helvetica', size=20), fg="white", bg="green")
    button_clear = Button(f2, text="C", width=_width, pady=_pady, command= clear,
                          font=font.Font(family='Helvetica', size=20), fg="green")
    button_ans = Button(f2, text="Ans", width=_width, pady=_pady, command= last_ans,
                        font=font.Font(family='Helvetica', size=20), fg="white", bg="red")
    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_0.grid(row=5, column=1)
    button_a.grid(row=1, column=3)
    button_s.grid(row=2, column=3)
    button_q.grid(row=3, column=3)
    button_f.grid(row=4, column=3)
    button_mod.grid(row=1, column=2)
    button_revert.grid(row=1, column=1)
    button_point.grid(row=5, column=2)
    button_equal.grid(row=5, column=3)
    button_clear.grid(row=1, column=0)
    button_ans.grid(row=5, column=0)


def main():
    global window, entry, history, f1, f2, revert_button, brackets_stack
    window = Tk()
    window.title("My Calculator")
    history = []
    brackets_stack = []
    revert_button = PhotoImage(file="images/revert.png")
    entry = Entry(window, width=19, borderwidth=5, justify="right", font=font.Font(family='Helvetica', size=20))
    entry.grid(row=0, column=0, columnspan=4)
    f1 = LabelFrame(window)
    f1.grid(row=1,column=0)
    f2 = LabelFrame(window)
    f2.grid(row=1,column=0)
    first_page()
    second_page()
    f1.tkraise()
    window.mainloop()
