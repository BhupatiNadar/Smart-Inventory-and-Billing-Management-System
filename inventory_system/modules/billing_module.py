import tkinter as tk
from tkinter import ttk

def BillingAndPOS_panel(USER):
    window = tk.Tk()
    window.title("Billing & POS")
    window.state('zoomed')
    window.config(bg="#ececec")
    
    #--function st --
    def BackButtonfun(USER):
        window.destroy()
        from modules.dashboard import Dasboard
        Dasboard(USER)
    
    #--end of function--

    Header = tk.Frame(window, height=60, pady=10, bg='#d9d9d9')
    Header.pack(fill='x')
    Header.pack_propagate(False)
    tk.Label(Header, text="Billing/POS", font=('Ariel', 25, 'bold'), padx=20, bg='#d9d9d9', fg="#333").pack(side='left')
    BackButton=tk.Button(Header,text="Back>",font=('Ariel',15),padx=10,pady=10,command=lambda:BackButtonfun(USER))
    BackButton.pack(side='right',padx=20)


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

    Table_frame=tk.Frame(right_panel)
    Table_frame.pack(pady=(50,0))
    
    style = ttk.Style()
    style.theme_use("clam")
    
    style.configure(
        "Custom.Treeview",
        background="#ffffff",
        foreground="#000000",
        rowheight=32,
        fieldbackground="#ffffff",
        font=("Ariel", 10)
    )

    style.configure(
        "Custom.Treeview.Heading",
        font=("Ariel", 10, "bold"),
        background="#d9d9d9",
        foreground="black"
    )

    style.map(
        "Custom.Treeview",
        background=[("selected", "#b3d9ff")],
        foreground=[("selected", "black")]
    )
    
    columns = ("id", "name", "sellprice", "CategoryId", "ProductStock")

    Tree = ttk.Treeview(
    Table_frame,
    columns=columns,
    show="headings",
    height=10,
    style="Custom.Treeview"
    )

    Tree.heading("id", text="Product Id")
    Tree.heading("name", text="Product Name")
    Tree.heading("sellprice", text="Sell Price")
    Tree.heading("CategoryId", text="Category Id")
    Tree.heading("ProductStock", text="Product Stock")
    
    Tree.column("id", width=100, anchor="center")
    Tree.column("name", width=100)
    Tree.column("sellprice", width=100)
    Tree.column("CategoryId", width=100, anchor="center")
    Tree.column("ProductStock", width=100)
    
    Tree.pack(side="left")
    
    scrollbar = ttk.Scrollbar(Table_frame, orient="vertical", command=Tree.yview)
    scrollbar.pack(side="right", fill="y")
    Tree.configure(yscrollcommand=scrollbar.set)
    
    products=[(1,"Bhupati",500,"tec","1")]#testing data
    
    for row in products:
        Tree.insert("",tk.END,values=row)

    Money_calculation = tk.Frame(right_panel, width=200, bg="white")
    Money_calculation.pack(side='left',padx=20, pady=20)


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

# BillingAndPOS_panel((1, 'Admin@gmail.com', '8097', 'admin'))
