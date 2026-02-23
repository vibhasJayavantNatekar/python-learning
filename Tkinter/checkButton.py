import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root , text= "Male" , variable=var1).grid(row=0 , sticky=tk.W)

tk.Checkbutton(root , text="Female" , variable=var2).grid(row=1 , sticky=tk.W)

#tk.IntVar() : Stores the checkbox state (1 or 0)

#grid() : Aligns widgets in rows and columns.

#sticky=tk.W : Aligns the checkbox to the left


root.mainloop()
