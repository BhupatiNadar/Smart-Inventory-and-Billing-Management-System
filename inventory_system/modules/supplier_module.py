import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def Supplier_management_panel(USER):
    window=tk.Tk()
    window.title("Supplier Management")
    window.state('zoomed')
    
    #-- function St for CRUD Operation --
    def Addfunc():
        SupplierName=Name_entry.get()
        SupplierContact=Contact_entry.get()
        SupplierEmail=Email_entry.get()
        SupplierAddress=Address_entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('insert into supplier (Supplier_name ,Supplier_contact ,Supplier_email ,Supplier_address) values (%s,%s,%s,%s)',(SupplierName,SupplierContact,SupplierEmail,SupplierAddress))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Supplier Added')
        Clearfunc()
        Tableload()
        
    def Deletefunc():
        SupplierID=Supplire_id_entry.get()
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('delete from supplier where Supplier_id =%s ',(SupplierID,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Supplier deleted')
        Clearfunc()
        Tableload()
        
    def Updatefunc():
        SupplierID=Supplire_id_entry.get()
        SupplierName=Name_entry.get()
        SupplierContact=Contact_entry.get()
        SupplierEmail=Email_entry.get()
        SupplierAddress=Address_entry.get()
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('update supplier set Supplier_name =%s,Supplier_contact =%s,Supplier_email =%s,Supplier_address =%s where Supplier_id =%s ',(SupplierName,SupplierContact,SupplierEmail,SupplierAddress,SupplierID))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Supplier updated')
        Clearfunc()
        Tableload()
        
    
    def Clearfunc():
        Supplire_id_entry.delete(0,tk.END)
        Name_entry.delete(0,tk.END)
        Contact_entry.delete(0,tk.END)
        Email_entry.delete(0,tk.END)
        Address_entry.delete(0,tk.END)  
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
    
    tk.Label(Header,text="Supplier Management",font=('Ariel',20),bg="#d9d9d9").pack(side='left')   
    
    Frame_for_input_and_button=tk.Frame(window)
    Frame_for_input_and_button.pack(fill='x')
    
    InputValueFrame=tk.Frame(Frame_for_input_and_button,height=400)
    InputValueFrame.grid(row=0,column=0)
    
    tk.Label(InputValueFrame,text='Supplier Id:',font=('Ariel',20),width=15,anchor='e' ).grid(row=0,column=0,padx=10,pady=10)
    Supplire_id_entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Supplire_id_entry.grid(row=0,column=1,padx=10,pady=10)
    
    tk.Label(InputValueFrame,text='Name:',font=('Ariel',20),width=15,anchor='e').grid(row=1,column=0,padx=10,pady=10)
    Name_entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Name_entry.grid(row=1,column=1,padx=10,pady=10)
    
    tk.Label(InputValueFrame,text='Contact:',font=('Ariel',20),width=15,anchor='e').grid(row=2,column=0,padx=10,pady=10)
    Contact_entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Contact_entry.grid(row=2,column=1,padx=10,pady=10)

    tk.Label(InputValueFrame,text='Email:',font=('Ariel',20),width=15,anchor='e').grid(row=3,column=0,padx=10,pady=10)
    Email_entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Email_entry.grid(row=3,column=1,padx=10,pady=10)

    tk.Label(InputValueFrame,text='Address:',font=('Ariel',20),width=15,anchor='e').grid(row=4,column=0,padx=10,pady=10)
    Address_entry=tk.Entry(InputValueFrame,font=('Ariel',18))
    Address_entry.grid(row=4,column=1,padx=10,pady=10)
    
    CRUD_operation_button_frame=tk.Frame(Frame_for_input_and_button)
    CRUD_operation_button_frame.grid(row=0,column=1,padx=40)
    
    Add_button=tk.Button(CRUD_operation_button_frame,text='Add',font=('Ariel',15),width=10,command=Addfunc)
    Add_button.pack(padx=30,pady=20)
    
    Update_button=tk.Button(CRUD_operation_button_frame,text='Update',font=('Ariel',15),width=10,command=Updatefunc)
    Update_button.pack(padx=30,pady=20)
    
    Delete_button=tk.Button(CRUD_operation_button_frame,text='Delete',font=('Ariel',15),width=10,command=Deletefunc)
    Delete_button.pack(padx=30,pady=20)
    
    Clear_button=tk.Button(CRUD_operation_button_frame,text='Clear',font=('Ariel',15),width=10,command=Clearfunc)
    Clear_button.pack(padx=30,pady=20)
    
    Supplier_Label_frame=tk.Frame(window)
    Supplier_Label_frame.pack(fill='x')
    
    tk.Label(Supplier_Label_frame,text='Supplier Detail:',font=('Ariel',20)).pack(side='left')
    
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
    
    columns = ("id", "name", "contact", "email", "address")
    
    Tree = ttk.Treeview(
        Table_frame,
        columns=columns,
        show="headings",
        height=12,
        style="Custom.Treeview"
    )
    
    Tree.heading("id", text="Supplier ID")
    Tree.heading("name", text="Name")
    Tree.heading("contact", text="Contact")
    Tree.heading("email", text="Email")
    Tree.heading("address", text="Address")

    Tree.column("id", width=150, anchor="center")
    Tree.column("name", width=250)
    Tree.column("contact", width=180)
    Tree.column("email", width=200)
    Tree.column("address", width=150, anchor="center")

    Tree.pack(side="left")
    
    scrollbar = ttk.Scrollbar(Table_frame, orient="vertical", command=Tree.yview)
    scrollbar.pack(side="right", fill="y")
    Tree.configure(yscrollcommand=scrollbar.set)
    
    def Supplierfuc():
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute(""" select Supplier_id,Supplier_name ,Supplier_contact,Supplier_email,Supplier_address from supplier""")
        datas=cursor.fetchall()
        conn.close()
        return datas
    
    def Tableload():
        for item in Tree.get_children():
            Tree.delete(item)
            
        for row in Supplierfuc():
            Tree.insert("",tk.END,values=row)
            
    Tableload()
        
    window.mainloop()
    
# Supplier_management_panel((1, 'Admin@gmail.com', '8097', 'admin'))