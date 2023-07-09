import webbrowser as wb
import tkinter as tk
from tkinter import *
root=tk.Tk()


root.title("ENQUIRY FORM")

def navigate_to_faq():
    selected_source = source_var.get()
    
    if selected_source == "Educative":
        wb.open("https://www.educative.io/blog/python-faq-answer-common-python-questions")
    elif selected_source == "Stack Overflow":
        wb.open("https://stackoverflow.com/questions/tagged/python")
    else:
        print("Error! Can't display your content")
        pass

l1=tk.Label(root,text="First Name",
           font=("Times New Roman",20))
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
l2=tk.Label(root,text="Last Name",
           font=("Times New Roman",20))
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
e2.grid()
l3=tk.Label(root, text="Where did you hear about the pyhton course?",
           font=("Times New Roman",20))
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",20),width=25)
source_var = StringVar(root)
source_var.set("Educative")
o=tk.OptionMenu(root, source_var, "Educative", "Stack Overflow",)
o.grid()


l4=tk.Label(root,text="",
           font=("Times New Roman",20))
l4.grid()

# b=tk.Button(root, text="Submit", command=navigate_to_faq).pack()
            
b=tk.Button(root,text="SUBMIT",font=("TIMES NEW ROMAN",15,),
            command=navigate_to_faq,bg="green",
            activebackground="black")
b.grid()


tk.mainloop()
