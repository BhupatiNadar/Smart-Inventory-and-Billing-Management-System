import tkinter as tk

def Supplier_management_panel(USER):
    window=tk.Tk()
    window.title("Supplier Management")
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
    
    Add_button=tk.Button(CRUD_operation_button_frame,text='Add',font=('Ariel',15),width=10)
    Add_button.pack(padx=30,pady=20)
    
    Update_button=tk.Button(CRUD_operation_button_frame,text='Update',font=('Ariel',15),width=10)
    Update_button.pack(padx=30,pady=20)
    
    Delete_button=tk.Button(CRUD_operation_button_frame,text='Delete',font=('Ariel',15),width=10)
    Delete_button.pack(padx=30,pady=20)
    
    Clear_button=tk.Button(CRUD_operation_button_frame,text='Clear',font=('Ariel',15),width=10)
    Clear_button.pack(padx=30,pady=20)
    
    Supplier_Label_frame=tk.Frame(window)
    Supplier_Label_frame.pack(fill='x')
    
    tk.Label(Supplier_Label_frame,text='Supplier Detail:',font=('Ariel',20)).pack(side='left')
    
    
    window.mainloop()
    
# Supplier_management_panel((1, 'Admin@gmail.com', '8097', 'admin'))