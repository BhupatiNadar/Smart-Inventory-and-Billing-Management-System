import tkinter as tk
from tkinter import ttk


def NewStaff(window,USER):
    window.title("New Staff")
    window.geometry("400x300")
    window.config(bg="#f0f0f0")
    window.grid_columnconfigure(0, weight=1)
    
    def Backfunc(USER):
        window.destroy()
        from modules.dashboard import Dasboard
        Dasboard(USER)

    def AddUser():
        email=email_entry.get()
        passward=pass_entry.get()
        category_value=category_entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute("insert into user (username,password,role) value(%s,%s,%s)",(email,passward,category_value))
        conn.commit()
        conn.close()
        clearfunc()
    
    def clearfunc():
        email_entry.delete(0,tk.END)
        pass_entry.delete(0,tk.END)
        category_entry.current(1)
        
    
    Header = tk.Frame(window, bg="#d9d9d9")
    Header.grid(row=0, column=0, columnspan=3, sticky="ew")  
    
    tk.Label(Header, text="New User", bg="#d9d9d9",
             font=("Arial", 15), anchor='center').pack(pady=10, fill='x') 
    
    tk.Label(window, text="Email:", bg="#f0f0f0",
             font=("Arial", 15)).grid(row=1, column=0)
    email_entry = tk.Entry(window, font=("Ariel", 15))
    email_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=8)
    
    tk.Label(window, text="passward:", bg="#f0f0f0",
             font=("Arial", 15)).grid(row=2, column=0)
    pass_entry = tk.Entry(window, font=("Ariel", 15))
    pass_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=8)
    
    category = ("admin", "staff")
    tk.Label(window, text="Category", font=('Ariel', 15)).grid(row=3, column=0)
    category_entry = ttk.Combobox(window, font=('Ariel', 15),
                                  values=category, state='readonly')
    category_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=8)
    category_entry.current(1)
    
    tk.Button(window, text="AddUser", font=("Arial", 12),
              width=10, command=AddUser).grid(row=4, column=1)
    tk.Button(window, text="back", font=("Arial", 12),
              width=10, command=lambda:Backfunc(USER)).grid(row=4, column=2)
    
    window.mainloop()
