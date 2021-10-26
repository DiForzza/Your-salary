from tkinter import *
zp = 0
zp2 = 0

def click_button():
    global zp
    zp = int(message_entry.get())
    btn.destroy()
    #btn["state"] = DISABLED
    message_entry.destroy()
    label1.place(relx=.5, rely=.5, anchor="c")
   # label1.pack()
    zp = zp * 12 / 1972 / 60 / 60 / 10
    timer()

def timer():
    global zp
    global zp2
    zp2 = zp2 + zp
    zp2 = round(zp2, 2)
    label1['text'] = (f'Твоя зарплата\nв реальном времени:\n{zp2}')
    #buttonText.set(f'Итого: {zp2}')
    root.after(100, timer)

def make_invisible(widget):
   widget.pack_forget()

root = Tk()
root.title("Calculator")
root.geometry("400x300+500+300")
root.resizable(False, False)
message_entry = StringVar()
message_entry.set('50000')
message_entry = Entry(textvariable=message_entry, font="Arial 14", justify=CENTER)
message_entry.place(relx=.5, rely=.4, anchor="c")
buttonText = StringVar()
buttonText.set('Введи свою зарплату и нажми кнопку')
btn = Button(textvariable=buttonText, command=click_button, font="Arial 14")
btn.place(relx=.5, rely=.5, anchor="c")
label1 = Label(text="Hello Python", fg="#500", font="Arial 24")

root.mainloop()

