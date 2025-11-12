import tkinter as tk
from tkinter import ttk

def productpanel():
    window = tk.Tk()
    window.title("Product Management")
    window.state('zoomed') 
    

    bg_color = "#f0f0f0"       
    entry_bg = "white"
    font_color = "#222222"     
    button_bg = "#e0e0e0"   

    window.configure(bg=bg_color)
    
    Header=tk.Frame(window,bg='#d9d9d9',padx=20,pady=20)
    Header.pack(fill='x')
    tk.Label(Header,text="Product Management",font=('Ariel',25),bg='#d9d9d9').pack()
    
    MainBody = tk.Frame(window, bg=bg_color, padx=20, pady=20)
    MainBody.pack(fill='both', expand=True)
    
   
    tk.Label(MainBody, text="Product ID", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=0, column=0, sticky='w', padx=5, pady=8)
    product_id = tk.Entry(MainBody, bg=entry_bg, relief='solid', borderwidth=1, font=('Ariel', 15))
    product_id.grid(row=0, column=1, padx=5, pady=8)
    
    tk.Label(MainBody, text='Name', bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=1, column=0, sticky='w', padx=5, pady=8)
    Name = tk.Entry(MainBody, bg=entry_bg, relief='solid', borderwidth=1, font=('Ariel', 15))
    Name.grid(row=1, column=1, padx=5, pady=8)
    
    tk.Label(MainBody, text="Cost Price", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=2, column=0, sticky='w', padx=5, pady=8)
    cost_price = tk.Entry(MainBody, bg=entry_bg, relief='solid', borderwidth=1, font=('Ariel', 15))
    cost_price.grid(row=2, column=1, padx=5, pady=8)
    
    MainBody.grid_columnconfigure(2, minsize=40) 
    
    category = [
    "Electronics",
    "Groceries",
    "Stationery",
    "Home Appliances",
    "Furniture",
    "Clothing",
    "Footwear",
    "Cosmetics",
    "Beverages",
    "Toys",
    "Sports Equipment",
    "Automobile Accessories",
    "Medical Supplies",
    "Hardware Tools",
    "Cleaning Supplies"
    ]
    tk.Label(MainBody, text="Category", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=0, column=3, sticky='w', padx=5, pady=8)
    category_entry = ttk.Combobox(MainBody, font=('Ariel', 15), values=category, state='readonly')
    category_entry.grid(row=0, column=4, padx=5, pady=8)
    category_entry.current(0) 

    supplier = [
    "TechWorld Distributors",
    "FreshMart Wholesale",
    "PaperPlus Stationery Co.",
    "HomeComfort Appliances",
    "Urban Furniture Hub",
    "StyleWear Fashions",
    "StepRight Footwear Ltd.",
    "Glow Cosmetics Pvt. Ltd.",
    "CoolDrinks Beverages",
    "ToyLand Traders",
    "FitGear Sports Supply",
    "AutoZone Parts Co.",
    "MediCare Suppliers",
    "ToolMaster Hardware",
    "CleanIt Hygiene Solutions"
    ]
    tk.Label(MainBody, text='Supplier', bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=1, column=3, sticky='w', padx=5, pady=8)
    supplier_entry = ttk.Combobox(MainBody, font=('Ariel', 15), values=supplier, state='readonly')
    supplier_entry.grid(row=1, column=4, padx=5, pady=8)
    supplier_entry.current(0)  
    
    tk.Label(MainBody, text="Stock", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=2, column=3, sticky='w', padx=5, pady=8)
    stock_entry = tk.Entry(MainBody, bg=entry_bg, relief='solid', borderwidth=1, font=('Ariel', 15))
    stock_entry.grid(row=2, column=4, padx=5, pady=8)
    
    Bttn = tk.Frame(MainBody, bg=bg_color)
    Bttn.grid(row=3, column=0, columnspan=5, pady=20, sticky='w')
    
    btn_font = ('Ariel', 12)
    btn_width = 12
    
    Add = tk.Button(Bttn, text="Add",bg=button_bg, relief='raised', borderwidth=1,font=btn_font, width=btn_width)
    Add.pack(side="left", padx= 6) 
    
    Update = tk.Button(Bttn, text="Update",bg=button_bg, relief='raised', borderwidth=1,font=btn_font, width=btn_width)
    Update.pack(side="left", padx=6)
    
    Delete = tk.Button(Bttn, text="Delete",bg=button_bg, relief='raised', borderwidth=1,font=btn_font, width=btn_width)
    Delete.pack(side="left", padx=6)
    
    Clear = tk.Button(Bttn, text="Clear",bg=button_bg, relief='raised', borderwidth=1,font=btn_font, width=btn_width)
    Clear.pack(side="left", padx=6)
    
    ProductTable = tk.Frame(MainBody, bg=bg_color, bd=1)
    ProductTable.grid(row=4, column=0, columnspan=5, pady=20, sticky='nsew')

    product_detail = ['Product ID', 'Name', 'Category', 'Supplier', 'Cost Price', 'Stock']

    for j, col_name in enumerate(product_detail):
        tk.Label(
            ProductTable,
            text=col_name,
            font=('Ariel', 12, 'bold'),
            bg='#d9d9d9',
            fg='black',
            relief='ridge',
            width=20,
            height=2
        ).grid(row=0, column=j,sticky='nsew')

    window.mainloop()
    
productpanel()