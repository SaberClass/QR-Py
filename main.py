import qrcode
from tkinter import *

FILE_NAME = "qr_code.png"
text = "https://www.youtube.com/watch?v=qg9IMJKnIAA"
entry = None

def generate_qr(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color = "white")

    image.save(file_name)

def submit_func(entry: Entry, window: Tk):
    global text

    if len(entry.get()) >= 3:
        text = entry.get()

    window.destroy()
    generate_qr(text, FILE_NAME)

def create_window():
    window = Tk()

    submit = Button(window, text="Submit",command=lambda: submit_func(entry, window))
    submit.pack(side=RIGHT)

    entry = Entry()
    entry.config(font=("Arial", 50))
    entry.config(bg="#111111")
    entry.config(fg="#00FF00")
    entry.pack()

    window.mainloop()



create_window()