from tkinter import *

counter = 0
def update():
    global counter,var_text
    counter += 1
    var_text.set(str(counter%3))

root = Tk()
root.geometry("300x300")
root.title('UI')

var_text = StringVar()
var_text.set('0')
btn = Button(root, width=20,bg='#3498db',fg='#ffffff',relief=FLAT,command=update,textvariable=var_text)
btn.grid(pady=100,row=1,column=0)
Grid.columnconfigure(root, 0, weight=1)

root.mainloop()
