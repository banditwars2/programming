from tkinter import *
import datetime
now = datetime.datetime.now()
seconds = now.second
window = Tk()
def refresh():
       window.quit()
       exec(open("./Homepage.py").read())
label = Label(window, text = str(seconds))
button = Button(window, text = "Click here to refresh",command = refresh)
label.pack()
button.pack()
window.mainloop()