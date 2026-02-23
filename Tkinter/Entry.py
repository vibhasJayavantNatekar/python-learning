import tkinter as tk

root = tk.Tk()
root.title("Input form")

tk.Label(root , text = "First Name").grid(row=0 , column=0)
tk.Label(root , text="Last name").grid(row =1 , column=0)

entry1 = tk.Entry(root).grid(row=0 , column=1)

#tk.Entry() : Creates a single - line text input box.

#grid() : Arranges widgets in rows and columns


entry2 = tk.Entry(root).grid(row=1 , column=1)




root.mainloop()