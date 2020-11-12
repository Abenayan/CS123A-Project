from tkinter import *
from tkinter import filedialog as fd
from pathlib import Path

root = Tk()

file1 = StringVar()
file1.set("File1")
file2 = StringVar()
file2.set("File2")
filename1 = ""
filename2 = ""


root.geometry('400x400')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


def buttonClick1():
    global filename2
    seqeunce1 = fd.askopenfilename()
    path = Path(seqeunce1)
    file1.set(path.name)
    filename2 = path.name


def buttonClick2():
    global filename2
    seqeunce1 = fd.askopenfilename()
    path = Path(seqeunce1)
    file2.set(path.name)
    filename2 = path.name



chooseFileButton1 = Button(topFrame, command=buttonClick1, text = "Choose file")
chooseFileButton1.pack()
labelFile1 = Label(topFrame, textvariable=file1)
labelFile1.pack()

chooseFileButton2 = Button(topFrame, command=buttonClick2,text = "Choose file")
chooseFileButton2.pack()
labelFile2 = Label(topFrame, textvariable=file2)
labelFile2.pack()

runMSA = Button(topFrame, text = "Run MSA")
runMSA.pack()

root.mainloop()


print(filename2)
print(type(filename2))