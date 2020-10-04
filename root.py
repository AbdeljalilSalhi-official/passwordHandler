#@abdeljalilsalhi
from tkinter import *
import os, random, pyperclip
import pandas as pd

root = Tk(className="Password Generator @abdeljalilsalhi")
root.iconphoto(True, PhotoImage(file="icon.png"))
root.configure(bg="black")
root.resizable(width=False, height=False)

chars1 = "abcdefghijklmnopqrstuvwxyz"
chars2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chars3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{[|`@]}+%§/?!$*^."
length = StringVar()
password = ''

def checkGEN():
    pswdGENtext.delete(0.0, END)
    if pswdLEVELradioVar.get() == chars1:
        easyGEN()
    elif pswdLEVELradioVar.get() == chars2:
        normalGEN()
    elif pswdLEVELradioVar.get() == chars3:
        hardGEN()
    else:
        noneGEN()
    
def easyGEN():
    global password, chars1
    password = ''
    length = int(pswdLENGTHspinboxVar.get())
    for i in range(length):
        password += random.choice(chars1)
    pyperclip.copy(password)
    pswdGENtext.insert(END, password)

def normalGEN():
    global password, chars2
    password = ''
    length = int(pswdLENGTHspinboxVar.get())
    for i in range(length):
        password += random.choice(chars2)
    pyperclip.copy(password)
    pswdGENtext.insert(END, password)

def hardGEN():
    global password, chars3
    password = ''
    length = int(pswdLENGTHspinboxVar.get())
    for i in range(length):
        password += random.choice(chars3)
    pyperclip.copy(password)
    pswdGENtext.insert(END, password)
    

def noneGEN():
    pswdGENtext.insert(END, "Choose PASSWORD LEVEL")

def saveGEN():
    global password
    csvDir = "C:/@abdeljalilsalhi/"
    csvFilename = "data.csv"
    csvPath = os.path.join(csvDir, csvFilename)
    if not os.path.isdir(csvDir):
        os.mkdir(csvDir)
        csvFile = open(csvPath, 'w+')
        csvFile.write("PASSWORD, NOTES\n")
        csvFile.close()
    notes = pswdNOTESentryVar.get()
    csvFile = open(csvPath, 'a+')
    pswdGENtextVar = pswdGENtext.get(0.0, END)
    csvFile.write("{}, {}\n".format(pswdGENtextVar.strip('\n'), notes))
    csvFile.close()

def showNOTES():
    global root2Text
    csvDir = "C:/@abdeljalilsalhi/"
    csvFilename = "data.csv"
    csvPath = os.path.join(csvDir, csvFilename)
    root2 = Tk(className="show Notes @abdeljalilsalhi")
    root2.configure(bg="black")
    root2.resizable(width=False, height=False)
    root2Title = Label(root2, text="SHOW NOTES", bg="black", fg="#ff1100")
    root2Title.grid(row=0, column=1, sticky=W)
    root2Text = Text(root2, height=20, width=50, wrap=WORD)
    root2Text.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
    root2Clear = Button(root2, text="CLEAR", cursor="cross", command=clearNOTES,
                        bg="black", fg="#ff1100", pady=5)
    root2Clear.grid(row=2, column=0)
    df = pd.read_csv(csvPath)
    code = df.head()
    root2Text.delete(0.0, END)
    root2Text.insert(END, code)
    root2.mainloop()

def clearNOTES():
    global root2Text
    csvDir = "C:/@abdeljalilsalhi/"
    csvFilename = "data.csv"
    csvPath = os.path.join(csvDir, csvFilename)
    csvFile = open(csvPath, 'w+')
    csvFile.write("PASSWORD, NOTES\n")
    csvFile.close()
    root2Text.delete(0.0, END)

rootTitle = Label(root, text="Password Handler @abdeljalilsalhi", font=32, bg="black", fg="#ff1100")
rootTitle.grid(row=0, column=1)
#PASSWORD GENERATOR FRAME
pswdGENframe = LabelFrame(root, text="PASSWORD GENERATOR", fg="#ff1100", bg="black")
pswdGENframe.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
pswdLENGTHlabel = Label(pswdGENframe, text="LENGTH", fg="#ff1100", bg="black")
pswdLENGTHlabel.grid(row=0, column=0, sticky=W)
pswdLENGTHspinboxVar = StringVar()
pswdLENGTHspinbox = Spinbox(pswdGENframe, textvariable=pswdLENGTHspinboxVar,from_=8, to=360, width=9)
pswdLENGTHspinbox.grid(row=0, column=1)
pswdLEVELlabel = Label(pswdGENframe, text="PASSWORD LEVEL", fg="#ff1100", bg="black")
pswdLEVELlabel.grid(row=1, column=0, sticky=W)
pswdLEVELradioVar = StringVar()
pswdLEVELradio1 = Radiobutton(pswdGENframe, text="[1] EASY", variable=pswdLEVELradioVar, value=chars1,
                              fg="#ff1100", bg="black", activebackground="black", activeforeground="#ff1100")
pswdLEVELradio1.grid(row=1, column=1)
pswdLEVELradio2 = Radiobutton(pswdGENframe, text="[2] NORMAL", variable=pswdLEVELradioVar, value=chars2,
                              fg="#ff1100", bg="black", activebackground="black", activeforeground="#ff1100")
pswdLEVELradio2.grid(row=1, column=2)
pswdLEVELradio3 = Radiobutton(pswdGENframe, text="[3] HARD", variable=pswdLEVELradioVar, value=chars3,
                              fg="#ff1100", bg="black", activebackground="black", activeforeground="#ff1100")
pswdLEVELradio3.grid(row=1, column=3)
pswdGENtext = Text(pswdGENframe, height=4, width=50, wrap=WORD)
pswdGENtext.grid(row=2, column=0, columnspan=4)
pswdNOTESlabel = Label(pswdGENframe, text="NOTES", fg="#ff1100", bg="black")
pswdNOTESlabel.grid(row=3, column=0, sticky=E)
pswdNOTESentryVar = StringVar()
pswdNOTESentry = Entry(pswdGENframe, textvariable=pswdNOTESentryVar, width=40)
pswdNOTESentry.grid(row=3, column=1, columnspan=3, sticky=W, pady=20)
pswdGENgen = Button(pswdGENframe, text="GENERATE", cursor="cross", command=checkGEN,
                     bg="black", fg="#ff1100", pady=5)
pswdGENgen.grid(row=4, column=0)
pswdGENsave = Button(pswdGENframe, text="SAVE", cursor="cross", command=saveGEN,
                     bg="black", fg="#ff1100", pady=5)
pswdGENsave.grid(row=4, column=2)
pswdSHOW = Button(root, text="SHOW NOTES", cursor="cross", command=showNOTES,
                  bg="black", fg="#ff1100", pady=5)
pswdSHOW.grid(row=2, column=2, sticky=E)

root.mainloop()
