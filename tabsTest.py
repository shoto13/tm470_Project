import tkinter as tk
from tkinter import *

from tkinter import ttk

root = tk.Tk()

root.title("TAB WIDGGY")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


# LOAD URL FUNCTION
def url_button_clicked():
    print("something was done my geeeez")


tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")

# ttk.Label(tab1, text='Welcome to GeeksForGeeks').grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab2, text='Lets dive into the world of computers').grid(column=0, row=0, padx=30, pady=30)

#BUTTON1
but1 = ttk.Button(tab1, text="Gbutton 1", command=url_button_clicked)
but1.pack(fill='x', expand=True, pady=8)
# BUTTON2
but2 = ttk.Button(tab1, text="button 2", command=url_button_clicked)
but2.pack(fill='x', expand=True, pady=8)
# BUTTON3
but3 = ttk.Button(tab1, text="button 3", command=url_button_clicked)
but3.pack(fill='x', expand=True, pady=8)
# BUTTON4
but4 = ttk.Button(tab1, text="button 4", command=url_button_clicked)
but4.pack(fill='x', expand=True, pady=8)


# URL RUN BUTTON
tab2Button = ttk.Button(tab2, text="oh myfff", command=url_button_clicked)
tab2Button.pack(fill='x', expand=True, pady=8)

root.mainloop()
