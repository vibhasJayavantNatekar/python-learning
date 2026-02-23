from tkinter import *

main = Tk()

ourmessage = "This is our Message"
messageVar = Message(main , text=ourmessage)
messageVar.config(bg="lightgreen")
messageVar.pack()

main.mainloop()
