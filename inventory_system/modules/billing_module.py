import tkinter as tk

def BillingAndPOS_panel(USER):
    window = tk.Tk()
    window.title("Billing & POS")
    window.state('zoomed')
    window.config(bg="#ececec")

    Header = tk.Frame(window, height=60, pady=10, bg='#d9d9d9')
    Header.pack(fill='x')
    Header.pack_propagate(False)
    tk.Label(Header, text="Billing/POS", font=('Ariel', 25, 'bold'), padx=20, bg='#d9d9d9', fg="#333").pack(fill='x')


    MainBody = tk.Frame(window, bg='#f5f5f5', bd=2, relief='groove')
    MainBody.pack(padx=20, pady=20, fill='both', expand=True)

# -- left column--
    left_panel = tk.Frame(MainBody, bg='white', bd=2, relief='ridge', width=500, height=600)
    left_panel.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    left_panel.pack_propagate(False)
    tk.Label(left_panel, text='Billing Panel', font=('Ariel', 20, 'bold'), pady=8,bg='white').grid(row=0, column=0, columnspan=2)
    
    tk.Label(left_panel,text="Select Product",font=('Ariel',15),pady=10,bg='white').grid(row=1,column=0)
    select_product=tk.Entry(left_panel,borderwidth=1,relief='solid',font=('Ariel', 15))
    select_product.grid(row=1,column=1, padx=5, pady=8)
    
    tk.Label(left_panel,text="Quantity",font=('Ariel',15),pady=10,bg='white').grid(row=2,column=0)
    Quantity_entry=tk.Entry(left_panel,borderwidth=1,relief='solid',font=('Ariel', 15))
    Quantity_entry.grid(row=2,column=1,padx=5,pady=8)
    
    Add_to_product=tk.Button(left_panel,text="Add to Cart",font=('Ariel',15))
    Add_to_product.grid(row=3,column=1)
    
    
#-- end of left column
    
    right_panel = tk.Frame(MainBody, bg='white', bd=2, relief='ridge', width=500, height=600)
    right_panel.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    right_panel.pack_propagate(False)

    tk.Label(right_panel,text='Cart / Bill Details',font=('Ariel', 20, 'bold'),pady=8,bg='white').grid(row=0,column=0,columnspan=2)

    Box_for_product = tk.Frame(right_panel,bg='grey',width=800,height=350)
    Box_for_product.grid(row=1,column=0,columnspan=3,padx=20,pady=20)
    
    Money_calculation=tk.Frame(right_panel,width=200,bg="White",padx=300)
    Money_calculation.grid(row=2,column=0)

    tk.Label(Money_calculation,text='Sub Total:',font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5).grid(row=0,column=0)
    Sub_total=tk.Label(Money_calculation,text="0.00",font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5)
    Sub_total.grid(row=0,column=1)
    
    tk.Label(Money_calculation,text='Discount:',font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5).grid(row=1,column=0)
    Discount=tk.Label(Money_calculation,text="0.00",font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5)
    Discount.grid(row=1,column=1)   

    tk.Label(Money_calculation,text='Tax:',font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5).grid(row=2,column=0)
    Tax=tk.Label(Money_calculation,text="0.00",font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5)  
    Tax.grid(row=2,column=1) 
    
    tk.Label(Money_calculation,text='Total:',font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5).grid(row=3,column=0)
    Tax=tk.Label(Money_calculation,text="0.00",font=('Ariel', 14, 'bold'),bg='white',padx=5,pady=5)  
    Tax.grid(row=3,column=1)  
    
    Generate_invoice=tk.Button(Money_calculation,text="Generate Invoice",font=('Ariel',14)) 
    Generate_invoice.grid(row=4,column=1,columnspan=2,pady=10)
    window.mainloop()

# BillingAndPOS_panel()
