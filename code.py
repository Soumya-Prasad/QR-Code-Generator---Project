from tkinter import*
from tkinter import messagebox
import pyqrcode
window=Tk()
window.title("QR code generator")
window.config(bg="#FAF0E6")
def generate_QR():
    if len(user_input.get())!=0:
        global qr,img
        qr=pyqrcode.create(user_input.get())
        img=BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning("warning","fields are required!")
    try:
        display_code()
    except:
        pass
def display_code():
    img_lbl.config(image=img)
    output.config(text="QR:"+user_input.get())

l=Label(window,text="Enter the text or URL:",font="Times 15",fg="#560319",bg="#FAF0E6",padx=20,pady=10)
l.pack()
user_input=StringVar()
e=Entry(window,textvariable=user_input,width=50,font="Times 15",fg="black")
e.pack(padx=30,pady=20)
b=Button(window,text="Generate QR",font="Times 15",bg="#DBE9FA",fg="#560319",command=generate_QR)
b.pack(padx=40,pady=30)
img_lbl=Label(window,bg="white")
img_lbl.pack()
output=Label(window,text="",bg="#FAF0E6")
output.pack()
window.mainloop()