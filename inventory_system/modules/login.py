import tkinter as tk
from tkinter import messagebox
from database.db_connection import create_connection 
from modules.dashboard import AdminDasboard

def login(window):
    window.title("Login")
    window.geometry("400x300")
    window.config(bg="#f0f0f0")
    
    def VerifyUser():
        username=username_entry.get()
        password=password_entry.get()
        
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute("Select * from Admin where username=%s And password=%s",(username,password))
        USER=cursor.fetchone()
        print(USER)
        conn.close()
        
        if USER[3]=="admin":
            messagebox.showinfo("Login Success", "Welcome Admin!")
            window.destroy()
            AdminDasboard(USER)
            
        elif USER[3]=='staff':
            messagebox.showinfo("Login Success", "Welcome staff!")
        else:
            messagebox.showinfo("Login Failed", "Invalid username or password")
            
            
    main_frame = tk.Frame(window, bg="#f0f0f0")
    main_frame.pack(expand=True, fill="both")


    Header = tk.Frame(main_frame, bg="#d9d9d9", height=60)
    Header.pack(fill="x")
    Header.pack_propagate(False)

 
    tk.Label(main_frame, text="Smart Inventory System", bg="#f0f0f0",font=("Arial", 20)).pack(pady=10)

   
    user_frame = tk.Frame(main_frame, bg="#f0f0f0")
    user_frame.pack(fill="x", pady=5)
    tk.Label(user_frame, text="Username", font=("Arial", 14), bg="#f0f0f0").pack(side='left')
    username_entry = tk.Entry(user_frame, font=("Arial", 14))
    username_entry.pack(side='left', fill='x', expand=True, padx=10)

    pass_frame = tk.Frame(main_frame, bg="#f0f0f0")
    pass_frame.pack(fill="x", pady=5)
    tk.Label(pass_frame, text="Password", font=("Arial", 14), bg="#f0f0f0").pack(side='left')
    password_entry = tk.Entry(pass_frame, font=("Arial", 14), show="*")
    password_entry.pack(side='left', fill='x', expand=True, padx=10)


    btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
    btn_frame.pack(pady=15)
    
    tk.Button(btn_frame, text="Login", font=("Arial", 12), width=10,command=VerifyUser).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Exit", font=("Arial", 12), width=10, command=window.destroy).grid(row=0, column=1, padx=5)