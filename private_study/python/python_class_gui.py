from tkinter import *

class MyDialog:
    def __init__(self, parent):
        Label(parent, text="값입력").pack()
        
        self.e = Entry(parent)
        self.e.pack(padx=5)
        
        self.b = Button(parent, text="확인", command=self.ok_click)
        self.b.pack(pady=5)
        
    def ok_click(self):
        print("value is", self.e.get())

root = Tk()

a = MyDialog(Tk())
a = MyDialog(Tk())
a = MyDialog(root)
root.mainloop