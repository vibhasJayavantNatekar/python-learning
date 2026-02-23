import tkinter as tk

root = tk.Tk()

label = tk.Label(root , text="First")

label.pack()

button = tk.Button(root,text="Submit" , width=25 , command=root.destroy )
button.pack()


root.mainloop()