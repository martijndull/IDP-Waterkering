from tkinter import *
import tkinter.messagebox as tm

def login():

    root_l = Tk()
    root_l.title("Login")
    root_l.attributes("-topmost", 1)
    root_l.attributes("-toolwindow",1)
    root_l.resizable(0,0)
    root_l.focus_force()
    lf = LabelFrame(root_l)

    def _login_btn_clickked():
        #print("Clicked")
        username = entry_1.get()
        password = entry_2.get()

        #print(username, password)

        if username == "admin" and password == "admin":
            result = tm.askquestion("Afsluiten", "Weet u zeker dat u het programma af wilt sluiten?", icon='warning')
            if result == 'yes':
                sys.exit()
            elif result == 'no':
                root_l.destroy()

        else:
            tm.showerror("Fout", "Verkeerde gebruikersnaam of wachtwoord")

    label_1 = Label(lf, text="Gebruikersnaam")
    label_2 = Label(lf, text="Wachtwoord")

    entry_1 = Entry(lf)
    entry_2 = Entry(lf, show="*")

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    logbtn = Button(lf, text="Login", command = _login_btn_clickked)
    logbtn.grid(columnspan=2)

    lf.pack()
    root_l.mainloop()
