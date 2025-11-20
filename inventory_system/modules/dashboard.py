import tkinter as tk

def Dasboard(USER):
    AdminPanel=tk.Tk()
    AdminPanel.state("zoomed")
    AdminPanel.title("Admin Panel")
    AdminPanel.config(bg="#f0f0f0")
    
    #-- fuction--
    def AddStafffuc():
        AdminPanel.destroy()
        from modules.NewStaff_module import NewStaff
        import tkinter as tk
        root=tk.Tk()
        NewStaff(root,USER)
        root.mainloop()
    #--END --
    
    #-- function--
    def LogOutFunc():
        AdminPanel.destroy()
        from modules.login import login
        import tkinter as tk
        root=tk.Tk()
        login(root)
        root.mainloop()
        
    def ProductManagementfunc():
        AdminPanel.destroy()
        from modules.product_module import productpanel
        productpanel(USER)
    
    def BillingAndPOSfunc():
        AdminPanel.destroy()
        from modules.billing_module import BillingAndPOS_panel
        BillingAndPOS_panel(USER)
        
    def CustomerManagementfunc():
        AdminPanel.destroy()
        from modules.customer_module import Customer_management_panel
        Customer_management_panel(USER)
    
    def SupplierManagementfunc():
        AdminPanel.destroy()
        from modules.supplier_module import Supplier_management_panel
        Supplier_management_panel(USER)
        
    #-- End of function --
    
    
    Header=tk.Frame(AdminPanel, bg="#d9d9d9", height=80)
    Header.pack(fill='x')
    Header.pack_propagate(False)
    
    tk.Label(Header,text="Dasboard",font=("Ariel",25),bg="#d9d9d9",pady=5).place(x=650)
    if USER[3]=='admin':
        AddStaff=tk.Button(Header,text="AddStaff",font=("Ariel",15),bg="#d9d9d9",command=AddStafffuc)
        AddStaff.place(x=1400,y=20)
    
    MainBody=tk.Frame(AdminPanel,width=1000,height=700,highlightbackground="lightgrey",highlightthickness=2)
    MainBody.pack(padx=10,pady=50)
    MainBody.pack_propagate(False)
    
    tk.Label(MainBody,text="Smart Inventry & Billing System",font=("Ariel",25)).place(x=150,y=20)
    tk.Label(MainBody,text=f"User:{USER[3]}",font=("Ariel",22)).place(x=800,y=20)
    
    if USER[3]=='admin':
    
        # -- Button --
        Product_management=tk.Button(MainBody,text="Product Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=ProductManagementfunc)
        Product_management.place(x=20,y=100)

        Supplier_management=tk.Button(MainBody,text="Supplier Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=SupplierManagementfunc)
        Supplier_management.place(x=500,y=100)

        Customer_management=tk.Button(MainBody,text="Customer Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=CustomerManagementfunc)
        Customer_management.place(x=20,y=250)

        Billing_POS=tk.Button(MainBody,text="Billing/POS",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=BillingAndPOSfunc)
        Billing_POS.place(x=500,y=250) 
    
        Sales_reports=tk.Button(MainBody,text="Sales Reports",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0)
        Sales_reports.place(x=20,y=400)   

        Logout_button=tk.Button(MainBody,text="Logout",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=LogOutFunc)
        Logout_button.place(x=500,y=400)     
    
    else:
        # -- Button --
        Product_management=tk.Button(MainBody,text="Product Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=ProductManagementfunc)
        Product_management.place(x=20,y=100)

        Supplier_management=tk.Button(MainBody,text="Supplier Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=SupplierManagementfunc)
        Supplier_management.place(x=500,y=100)

        Customer_management=tk.Button(MainBody,text="Customer Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=CustomerManagementfunc)
        Customer_management.place(x=20,y=250)

        Billing_POS=tk.Button(MainBody,text="Billing/POS",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=BillingAndPOSfunc)
        Billing_POS.place(x=500,y=250) 
    
        Sales_reports=tk.Button(MainBody,text="Sales Reports",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,state='disabled')
        Sales_reports.place(x=20,y=400)   

        Logout_button=tk.Button(MainBody,text="Logout",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=LogOutFunc)
        Logout_button.place(x=500,y=400)
    

    AdminPanel.mainloop()
# USER=(1, 'Admin@gmail.com', '8097', 'admin')
# AdminDasboard(USER)