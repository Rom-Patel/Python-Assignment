import tkinter as tk
import webbrowser as wb
root=tk.Tk()

l1=tk.Label(root,text="Amazon Prime",
            font=("Times New Roman",25),
            width=30,bg="sky blue")
l1.grid()
e=tk.Entry(root,font=("Times New Roman",30),width=40)
e.grid()

def display():
    s=e.get()
    wb.open(f"https://www.primevideo.com/search/ref=atv_nb_sug?ie=UTF8&phrase={s}") 
    print("Navigating to amazon prime video search:",
          (f"https://www.primevideo.com/search/ref=atv_nb_sug?ie=UTF8&phrase=={s}"))

b1=tk.Button(root,text="Search",font=("Times New Roman",30),command=display)
b1.grid()

b=tk.Button(root,text="Close",font=("Times New Roman",30),command=root.destroy)
b.grid()
root.mainloop()

