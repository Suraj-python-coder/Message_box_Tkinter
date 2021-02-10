# Message Box and Exception Handling:
# ===================================

import tkinter as tk       
from tkinter import ttk 
from tkinter import messagebox as m_box
win = tk.Tk() 

# label frame:
label_frame = ttk.LabelFrame(win, text='Contact Details')
label_frame.grid(row=0, column=0, padx=40, pady=10)

# labels:
name_label = ttk.Label(label_frame, text='Enter your Name please : ', font=('Helvetica',10,'bold'))
age_label = ttk.Label(label_frame, text='Enter your Age please : ', font=('Helvetica',10,'bold'))

# entry box variables:
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes:
name_entry = ttk.Entry(label_frame, width=36, textvariable= name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable= age_var)

# Grid:
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

def submit():
    # m_box.showinfo('title','content of this message box')   # here showinfo is the methode inside the messagebox module
    # m_box.showerror('title','content of this message box')  # showerror this is another methode in messagebox , it gives us messagebox
    # m_box.showwarning('title','content of this message box') # showworning

    name = name_var.get()
    age = age_var.get()

    if name=='' or age=='':
        m_box.showerror('Error','Please fill both name and age ')
    else:
        try:
            # age = 'kjdfa'
            # age = 22
            age = int(age)
        except ValueError:
            m_box.showerror('Error','Only digits are allowed in age field')
        else:
            if age < 18:
                m_box.showwarning('WORNING!!','you are not 18, visit this content on your own risk')
            print(f'{name} : {age}')







# submit button:
submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1,columnspan=2,padx=20)

win.mainloop()