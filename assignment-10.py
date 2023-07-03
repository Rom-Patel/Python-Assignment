import tkinter as tk
import webbrowser as wb
obj=tk.Tk()

e=tk.Entry(obj,font=("Times New Roman",30),width=40)
e.pack(anchor="center")

def display():
    s=e.get()
    wb.open(f"https://www.youtube.com/results?search_query={s}") 
    print("Navigating to youtube search:",(f"https://www.youtube.com/results?search_query={s}"))

b1=tk.Button(obj,text="Search",font=("Times New Roman",30),command=display)
b1.pack(anchor="center")

b=tk.Button(obj,text="Close",font=("Times New Roman",30),command=obj.destroy)
b.pack(anchor="sw")
obj.mainloop()

