from tkinter import *
from tkinter import messagebox
import base64 
import os

def secKey():
    global scr
    global seckey

    def proceed():
        if len(seckey.get())>=5:
            open_scren_window(seckey.get())
        else:
            messagebox.showerror("Set Secret Key","Secret should be five character long or more")

    # Create the first window
    scr = Tk()
    scr.geometry('350x300')
    scr.title('Set Secret Key')

    # Load image for the window icon
    img = PhotoImage(file='E:/py_projects/key.png')
    scr.iconphoto(False, img)

    Label(scr, text="Enter your secret key", fg="black", font=("Times New Roman", 12)).place(x=10, y=90)
    seckey = StringVar()
    Entry(scr, textvariable=seckey, width=35, bd=5, font=("arial", 12)).place(x=10, y=120)

    Button(scr, text="Next", height="2", width="20", bg="#01c1fa", fg="white", bd=5, command=proceed).place(x=95, y=160)

    scr.mainloop()

def open_scren_window(secret_key):
    def reset():
        txt.delete(1.0, END)
        txtval.set("Encrypted value will appear here")  
        txtval1.set("Decrypted value will appear here")

    def enc():
        global encrypt
        msg = txt.get(1.0, END).strip()  # Remove trailing newline characters
        encode_msg = msg.encode("ascii")
        bs64_bytes = base64.b64encode(encode_msg)
        encrypt = bs64_bytes.decode("ascii")
        txtval.set(encrypt)

    def dec():
        global decrypt
        msg = txt.get(1.0, END).strip()  # Remove trailing newline characters
        decode_msg = msg.encode("ascii")
        bs64_bytes = base64.b64decode(decode_msg)
        decrypt = bs64_bytes.decode("ascii")
        txtval1.set(decrypt)

    # Create the second window
    scren = Toplevel()
    scren.geometry('350x485')
    scren.title('Encrypt & Decrypt')
    img = PhotoImage(file='E:/py_projects/key.png')
    scren.iconphoto(False, img)

    # The value to encrypt or decrypt
    Label(scren, text="Enter value to encrypt or decrypt", fg="black", font=("Times New Roman", 12)).place(x=10, y=10)
    txt = Text(scren, font="Arial 12", bg="white", relief=GROOVE, wrap=WORD, bd=5)
    txt.place(x=10, y=40, width=330, height=100)
    
    # Enter your previously set secret key
    Label(scren, text="Your previously inserted secret key", fg="black", font=("Times New Roman", 12)).place(x=10, y=150)
    code = StringVar(value=secret_key)  # Initialize with the provided secret_key
    code_entry = Entry(scren, textvariable=code, width=35, bd=5, font=("arial", 12), show="*", state='readonly')
    code_entry.place(x=10, y=180)
    
    # Encrypted Value
    Label(scren, text="Encrypted Value", fg="black", font=("Times New Roman", 12)).place(x=10, y=220)
    txtval = StringVar(value="encrypted value will appear here")
    txt2 = Entry(scren, textvariable=txtval, width=39, bd=5, font=("Times New Roman", 12))
    txt2.place(x=10, y=250)

    # Decrypted Value
    Label(scren, text="Decrypted Value", fg="black", font=("Times New Roman", 12)).place(x=10, y=290)
    txtval1 = StringVar(value="decrypted value will appear here")
    txt3 = Entry(scren, textvariable=txtval1, width=39, bd=5, font=("Times New Roman", 12))
    txt3.place(x=10, y=320)
    
    # Buttons
    Button(scren, text="Encrypt", height="2", width="20", bg="#fa2401", fg="white", bd=5, command=enc).place(x=10, y=370)
    Button(scren, text="Decrypt", height="2", width="20", bg="green", fg="white", bd=5, command=dec).place(x=178, y=370)
    Button(scren, text="Reset", height="2", width="20", bg="#01c1fa", fg="white", bd=5, command=reset).place(x=95, y=430)
    
    scren.mainloop()

secKey()
