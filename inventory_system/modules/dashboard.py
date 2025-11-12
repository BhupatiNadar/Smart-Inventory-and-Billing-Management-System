import tkinter as tk

def AdminDasboard(USER):
    AdminPanel=tk.Tk()
    AdminPanel.state("zoomed")
    AdminPanel.title("Admin Panel")
    AdminPanel.config(bg="#f0f0f0")
    
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
        productpanel()
    
    def BillingAndPOSfunc():
        AdminPanel.destroy()
        from modules.billing_module import BillingAndPOS_panel
        BillingAndPOS_panel()
    #-- End of function --
    
    
    Header=tk.Frame(AdminPanel, bg="#d9d9d9", height=80)
    Header.pack(fill='x')
    Header.pack_propagate(False)
    
    tk.Label(Header,text="Dasboard",font=("Ariel",25),bg="#d9d9d9").pack(pady=10)
    
    MainBody=tk.Frame(AdminPanel,width=1000,height=700,highlightbackground="lightgrey",highlightthickness=2)
    MainBody.pack(padx=10,pady=50)
    MainBody.pack_propagate(False)
    
    tk.Label(MainBody,text="Smart Inventry & Billing System",font=("Ariel",25)).place(x=150,y=20)
    tk.Label(MainBody,text=f"User:{USER[3]}",font=("Ariel",22)).place(x=800,y=20)
    
    if USER[3]=='admin':
    
        # -- Button --
        Product_management=tk.Button(MainBody,text="Product Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=ProductManagementfunc)
        Product_management.place(x=20,y=100)

        Product_management=tk.Button(MainBody,text="Supplier Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0)
        Product_management.place(x=500,y=100)

        Product_management=tk.Button(MainBody,text="Customer Management",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0)
        Product_management.place(x=20,y=250)

        Product_management=tk.Button(MainBody,text="Billing/POS",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=BillingAndPOSfunc)
        Product_management.place(x=500,y=250) 
    
        Product_management=tk.Button(MainBody,text="Sales Reports",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=ProductManagementfunc)
        Product_management.place(x=20,y=400)   

        Product_management=tk.Button(MainBody,text="Logout",height=3,width=25,font=("Ariel",20),bg="#e2e2e2",relief="flat",borderwidth=0,command=LogOutFunc)
        Product_management.place(x=500,y=400)     
    
    

    AdminPanel.mainloop()
# USER=(1, 'Admin@gmail.com', '8097', 'admin')
# AdminDasboard(USER)