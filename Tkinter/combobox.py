import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

label = tk.Label(root, text="selected Item:")
label.pack(pady=10)

#create a Combobox widget
combo_box = ttk.Combobox(
    root,
    values=["Option 1" , "Option2" , "Option3"],
    state= "readonly"
)

combo_box.pack(pady=5)
combo_box.set("Option1")

combo_box.bind("<<ComboboxSelected>>" , select)
root.mainloop()


