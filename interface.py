from tkinter import *
from tkinter import font

def button_input(char):
    ipt = entry.get()
    if char == 0:
        if len(ipt) > 0:
            entry.delete(0, END)
            entry.insert(0, str(ipt) + str(char))
    else:
        entry.delete(0, END)
        entry.insert(0, str(ipt) + str(char))

def clear():
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


def main():
    global window, entry, history
    window = Tk()
    history = []
    window.title("My Calculator")
    _width = 4
    _pady = 4
    entry = Entry(window, width=20, borderwidth=5, justify="right", font=font.Font(family = 'Helvetica', size = 20))
    entry.grid(row=0, column=0, columnspan=4)
    button_1 = Button(window, text="1", width=_width, pady=_pady, command=lambda: button_input(1), font=font.Font(family = 'Helvetica', size = 20))
    button_2 = Button(window, text="2", width=_width, pady=_pady, command=lambda: button_input(2), font=font.Font(family = 'Helvetica', size = 20))
    button_3 = Button(window, text="3", width=_width, pady=_pady, command=lambda: button_input(3), font=font.Font(family = 'Helvetica', size = 20))
    button_4 = Button(window, text="4", width=_width, pady=_pady, command=lambda: button_input(4), font=font.Font(family = 'Helvetica', size = 20))
    button_5 = Button(window, text="5", width=_width, pady=_pady, command=lambda: button_input(5), font=font.Font(family = 'Helvetica', size = 20))
    button_6 = Button(window, text="6", width=_width, pady=_pady, command=lambda: button_input(6), font=font.Font(family = 'Helvetica', size = 20))
    button_7 = Button(window, text="7", width=_width, pady=_pady, command=lambda: button_input(7), font=font.Font(family = 'Helvetica', size = 20))
    button_8 = Button(window, text="8", width=_width, pady=_pady, command=lambda: button_input(8), font=font.Font(family = 'Helvetica', size = 20))
    button_9 = Button(window, text="9", width=_width, pady=_pady, command=lambda: button_input(9), font=font.Font(family = 'Helvetica', size = 20))
    button_0 = Button(window, text="0", width=_width, pady=_pady, command=lambda: button_input(0), font=font.Font(family = 'Helvetica', size = 20))
    button_add = Button(window, text="+", width=_width, pady=_pady, command=lambda: button_input("+"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_subs = Button(window, text="-", width=_width, pady=_pady, command=lambda: button_input("-"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_mult = Button(window, text="x", width=_width, pady=_pady, command=lambda: button_input("x"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_div = Button(window, text="÷", width=_width, pady=_pady, command=lambda: button_input("÷"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_mod = Button(window, text="%", width=_width, pady=_pady, command=lambda: button_input("%"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_divint = Button(window, text="//", width=_width, pady=_pady, command=lambda: button_input("//"), font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_point = Button(window, text=".", width=_width, pady=_pady, command=lambda: button_input("."), font=font.Font(family = 'Helvetica', size = 20))
    button_equal = Button(window, text="=", width=_width, pady=_pady, command=equal, font=font.Font(family = 'Helvetica', size = 20), fg="white", bg="green")
    button_clear = Button(window, text="C", width=_width, pady=_pady, command=clear, font=font.Font(family = 'Helvetica', size = 20), fg="green")
    button_ans = Button(window, text="Ans", width=_width, pady=_pady, command=last_ans, font=font.Font(family = 'Helvetica', size = 20), fg="white", bg="red")
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
    button_mod.grid(row=1,column=1)
    button_divint.grid(row=1,column=2)
    button_point.grid(row=5,column=2)
    button_equal.grid(row=5, column=3)
    button_clear.grid(row=1, column=0)
    button_ans.grid(row=5,column=0)
    window.mainloop()