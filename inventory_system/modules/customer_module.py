import tkinter as tk

def Customer_management_panel(USER):
    window=tk.Tk()
    window.title("Customer Management")
    window.state('zoomed')
    
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
    
    CRUD_operation_button_frame=tk.Frame(window,height=80)
    CRUD_operation_button_frame.pack(fill='x')
    
    Add_button=tk.Button(CRUD_operation_button_frame,text='Add',font=('Ariel',15),width=10)
    Add_button.pack(side='left',padx=30)
    
    Update_button=tk.Button(CRUD_operation_button_frame,text='Update',font=('Ariel',15),width=10)
    Update_button.pack(side='left',padx=30)
    
    Delete_button=tk.Button(CRUD_operation_button_frame,text='Delete',font=('Ariel',15),width=10)
    Delete_button.pack(side='left',padx=30)
    
    Clear_button=tk.Button(CRUD_operation_button_frame,text='Clear',font=('Ariel',15),width=10)
    Clear_button.pack(side='left',padx=30)
    
    Customer_detail_frame=tk.Frame(window)
    Customer_detail_frame.pack(fill='both',pady=20,padx=20)
    Customer_detail_frame.pack_propagate(False)
    tk.Label(Customer_detail_frame,text='Table:Customer List',font=('Ariel',20)).grid(row=0,column=0)
    window.mainloop()
    
Customer_management_panel((1, 'Admin@gmail.com', '8097', 'admin'))