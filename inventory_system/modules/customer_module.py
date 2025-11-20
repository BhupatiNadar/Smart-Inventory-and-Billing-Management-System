import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def Customer_management_panel(USER):
    window=tk.Tk()
    window.title("Customer Management")
    window.state('zoomed')
    
    #--fuction for Add,update,delete,clear --
    def Addfunc():
        Customer_name=Name_Entry.get()
        Customer_phone_no=Phone_Entry.get()
        Customer_email=Email_Entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('''
                       insert into customer_management (customer_name ,Customer_email ,Customer_phone_no) values (%s,%s,%s)
                       ''',(Customer_name,Customer_email,Customer_phone_no))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Customer Added')
        Clearfunc()
        TableLoad()
        
    def Deletefunc():
        CustomerID=Customer_id_Entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('Delete from customer_management where Customer_id =%s',(CustomerID,))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Customer Deleted')
        Clearfunc()
        TableLoad()
    
    def Clearfunc():
        Customer_id_Entry.delete(0,tk.END)
        Name_Entry.delete(0,tk.END)
        Phone_Entry.delete(0,tk.END)
        Email_Entry.delete(0,tk.END)
        
    def Updatefunc():
        Customer_name=Name_Entry.get()
        Customer_phone_no=Phone_Entry.get()
        Customer_email=Email_Entry.get()
        CustomerID=Customer_id_Entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('''
                       update customer_management
                       set customer_name =%s,Customer_email =%s,Customer_phone_no =%s
                       where Customer_id =%s
                       ''',(Customer_name,Customer_email,Customer_phone_no,CustomerID))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Customer updated')
        Clearfunc()
        TableLoad()
              
    
    #--END--
    
    #--function st --
    def BackButtonfun(USER):
        window.destroy()
        from modules.dashboard import Dasboard
        Dasboard(USER)
    
    #--end of function--
    
    Header=tk.Frame(window,height=60,bg="#d9d9d9")
    Header.pack(fill='x')
    Header.pack_propagate(False)
    BackButton=tk.Button(Header,text="Back>",font=('Ariel',15),command=lambda:BackButtonfun(USER))
    BackButton.pack(side='right',padx=20)
    
    tk.Label(Header,text="Customer Management",font=('Ariel',20),bg="#d9d9d9").pack(side='left')
    
    InputValueFrame=tk.Frame(window,height=400)
    InputValueFrame.pack(fill='x')
    
    tk.Label(InputValueFrame,text="Customer Id:",font=('Ariel',20)).grid(row=0,column=0,padx=10,pady=10)
    Customer_id_Entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Customer_id_Entry.grid(row=0,column=1,padx=10,pady=10)
    
    tk.Label(InputValueFrame,text="Name:",font=('Ariel',20)).grid(row=1,column=0,padx=10,pady=10)
    Name_Entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Name_Entry.grid(row=1,column=1,padx=10,pady=10)
    
    tk.Label(InputValueFrame,text="Phone:",font=('Ariel',20)).grid(row=2,column=0,padx=10,pady=10)
    Phone_Entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Phone_Entry.grid(row=2,column=1,padx=10,pady=10)
    
    tk.Label(InputValueFrame,text="Email:",font=('Ariel',20)).grid(row=3,column=0,padx=10,pady=10)
    Email_Entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Email_Entry.grid(row=3,column=1,padx=10,pady=10)
    state_val = "disabled" if USER[3] == "staff" else "normal"
    CRUD_operation_button_frame=tk.Frame(window,height=80)
    CRUD_operation_button_frame.pack(fill='x')
    
    Add_button=tk.Button(CRUD_operation_button_frame,text='Add',font=('Ariel',15),width=10,command=Addfunc)
    Add_button.pack(side='left',padx=30)
    
    Update_button=tk.Button(CRUD_operation_button_frame,text='Update',font=('Ariel',15),width=10,command=Updatefunc)
    Update_button.pack(side='left',padx=30)
    
    Delete_button=tk.Button(CRUD_operation_button_frame,text='Delete',font=('Ariel',15),width=10,command=Deletefunc,state=state_val)
    Delete_button.pack(side='left',padx=30)
    
    Clear_button=tk.Button(CRUD_operation_button_frame,text='Clear',font=('Ariel',15),width=10,command=Clearfunc)
    Clear_button.pack(side='left',padx=30)
    
    Customer_detail_frame=tk.Frame(window)
    Customer_detail_frame.pack(fill='both',pady=20,padx=20)
    Customer_detail_frame.pack_propagate(False)
    tk.Label(Customer_detail_frame,text='Table:Customer List',font=('Ariel',20)).grid(row=0,column=0)
    
    Table_frame=tk.Frame(window)
    Table_frame.pack(pady=20,side='left')
    
    style = ttk.Style()
    style.theme_use("clam")
    
    style.configure(
        "Custom.Treeview",
        background="#ffffff",
        foreground="#000000",
        rowheight=32,
        fieldbackground="#ffffff",
        font=("Ariel", 13)
    )

    style.configure(
        "Custom.Treeview.Heading",
        font=("Ariel", 15, "bold"),
        background="#d9d9d9",
        foreground="black"
    )

    style.map(
        "Custom.Treeview",
        background=[("selected", "#b3d9ff")],
        foreground=[("selected", "black")]
    )
    
    columns = ("id", "name", "email","PhoneNo")
    
    Tree = ttk.Treeview(
        Table_frame,
        columns=columns,
        show="headings",
        height=12,
        style="Custom.Treeview"
    )
    
    Tree.heading("id", text="Customer ID")
    Tree.heading("name", text="Name")
    Tree.heading("email", text="Email")
    Tree.heading("PhoneNo", text="Mobile No")

    Tree.column("id", width=250, anchor="center")
    Tree.column("name", width=250)
    Tree.column("email", width=200)
    Tree.column("PhoneNo", width=250, anchor="center")
    
    Tree.pack(side="left")
    
    scrollbar = ttk.Scrollbar(Table_frame, orient="vertical", command=Tree.yview)
    scrollbar.pack(side="right", fill="y")
    Tree.configure(yscrollcommand=scrollbar.set)
    
    def Customerfunc():
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute("""
                       select Customer_id ,customer_name ,Customer_email ,Customer_phone_no from customer_management
                       """)
        datas=cursor.fetchall()
        conn.close()
        return datas
    
    def TableLoad():
        for item in Tree.get_children():
            Tree.delete(item)
            
        for row in Customerfunc():
            Tree.insert("",tk.END,values=row)
            
    TableLoad()
    
    window.mainloop()
    
# Customer_management_panel((1, 'Admin@gmail.com', '8097', 'admin'))