import tkinter as tk
from tkinter import ttk
from database.db_connection import create_connection
from tkinter import messagebox

def productpanel(USER):
    window = tk.Tk()
    window.title("Product Management")
    window.state('zoomed')

    bg_color = "#f0f0f0"
    entry_bg = "white"
    font_color = "#222222"
    button_bg = "#e0e0e0"
    window.configure(bg=bg_color)
    
    #---add,update,delete,clear func--
    def Add_product_func():
        ProductName=Name.get()
        CostPrice=cost_price.get()
        CategoryName=category_entry.get()
        SupplierName=supplier_entry.get()
        Stock=stock_entry.get()
        SellingPrice=int(CostPrice)+50
        
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('Select Supplier_id from supplier where Supplier_name = %s ',(SupplierName,))
        SupplierID=cursor.fetchone()
        cursor.execute('Select category_id  from category where name  = %s ',(CategoryName,))
        CategoryID=cursor.fetchone()
        cursor.execute(
        '''
        INSERT INTO product
        (Product_name, cost_price, sell_price, category_id, supplier_id, Product_stock)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''',
        (ProductName, CostPrice, SellingPrice, CategoryID[0], SupplierID[0], Stock)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Product Added')
        loadTable()
        Clearfunc()
        
    def delete_product_func():
        ProductID=product_id.get()
        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('Delete from product where Product_id =%s',(ProductID,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Product Deleted')
        loadTable()
        Clearfunc()
        
    def Clearfunc():
        product_id.delete(0,tk.END)
        Name.delete(0,tk.END)
        cost_price.delete(0,tk.END)
        category_entry.current(0)
        supplier_entry.current(0)
        stock_entry.delete(0,tk.END)
        
    def update_product_func():
        ProductID=product_id.get()
        ProductName=Name.get()
        CostPrice=cost_price.get()
        CategoryName=category_entry.get()
        SupplierName=supplier_entry.get()
        Stock=stock_entry.get()
        SellingPrice=int(CostPrice)+50

        from database.db_connection import create_connection
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute('Select Supplier_id from supplier where Supplier_name = %s ',(SupplierName,))
        SupplierID=cursor.fetchone()
        cursor.execute('Select category_id  from category where name  = %s ',(CategoryName,))
        CategoryID=cursor.fetchone()
        
        cursor.execute('''
                       update product
                       set Product_name =%s,cost_price =%s,sell_price =%s,category_id =%s,supplier_id=%s,Product_stock=%s
                       where Product_id =%s 
                       ''',(ProductName, CostPrice, SellingPrice, CategoryID[0], SupplierID[0], Stock,ProductID))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Product Updated')
        Clearfunc()
        loadTable()
        
        
        
        
    #---END--

    # ---------------- Back Button ----------------
    def BackButtonfun(USER):
        window.destroy()
        from modules.dashboard import Dasboard
        Dasboard(USER)

    Header = tk.Frame(window, height=60, pady=10, bg='#d9d9d9')
    Header.pack(fill='x')
    Header.pack_propagate(False)

    tk.Label(Header, text="Product Management", font=('Ariel', 20), bg='#d9d9d9').pack(side='left')
    BackButton = tk.Button(Header, text="Back>", font=('Ariel', 15), padx=10, pady=10,
                           command=lambda: BackButtonfun(USER))
    BackButton.pack(side='right', padx=20)

    # ---------------- Main Body ----------------
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

    # ---------------- Category DB ----------------
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM category")
    datas = cursor.fetchall()
    category = [d[1] for d in datas]
    conn.close()

    tk.Label(MainBody, text="Category", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=0, column=3, sticky='w', padx=5, pady=8)
    category_entry = ttk.Combobox(MainBody, font=('Ariel', 15), values=category, state='readonly')
    category_entry.grid(row=0, column=4, padx=5, pady=8)
    category_entry.current(0)

    # ---------------- Supplier DB ----------------
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM supplier")
    datas = cursor.fetchall()
    supplier = [d[1] for d in datas]
    conn.close()

    tk.Label(MainBody, text='Supplier', bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=1, column=3, sticky='w', padx=5, pady=8)
    supplier_entry = ttk.Combobox(MainBody, font=('Ariel', 15), values=supplier, state='readonly')
    supplier_entry.grid(row=1, column=4, padx=5, pady=8)
    supplier_entry.current(0)

    tk.Label(MainBody, text="Stock", bg=bg_color, fg=font_color, font=('Ariel', 15)).grid(row=2, column=3, sticky='w', padx=5, pady=8)
    stock_entry = tk.Entry(MainBody, bg=entry_bg, relief='solid', borderwidth=1, font=('Ariel', 15))
    stock_entry.grid(row=2, column=4, padx=5, pady=8)

    # ---------------- Buttons ----------------
    Bttn = tk.Frame(MainBody, bg=bg_color)
    Bttn.grid(row=3, column=0, columnspan=5, pady=20, sticky='w')

    btn_font = ('Ariel', 12)
    btn_width = 12
    state_val = "disabled" if USER[3] == "staff" else "normal"
    tk.Button(Bttn, text="Add", bg=button_bg, font=btn_font, width=btn_width,command=Add_product_func).pack(side="left", padx=6)
    tk.Button(Bttn, text="Update", bg=button_bg, font=btn_font, width=btn_width,command=update_product_func).pack(side="left", padx=6)
    tk.Button(Bttn, text="Delete", bg=button_bg, font=btn_font, width=btn_width,command=delete_product_func,state=state_val).pack(side="left", padx=6)
    tk.Button(Bttn, text="Clear", bg=button_bg, font=btn_font, width=btn_width,command=Clearfunc).pack(side="left", padx=6)

    # ---------------- Table Frame ----------------
    TableFrame = tk.Frame(MainBody, bg=bg_color)
    TableFrame.grid(row=5, column=0, columnspan=5, pady=20)

    # ---------------- Treeview Style ----------------
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

    # ---------------- Treeview ----------------
    columns = ("id", "name", "category", "supplier", "price", "stock")

    Tree = ttk.Treeview(
        TableFrame,
        columns=columns,
        show="headings",
        height=12,
        style="Custom.Treeview"
    )

    Tree.heading("id", text="Product ID")
    Tree.heading("name", text="Name")
    Tree.heading("category", text="Category")
    Tree.heading("supplier", text="Supplier")
    Tree.heading("price", text="Cost Price")
    Tree.heading("stock", text="Stock")

    Tree.column("id", width=150, anchor="center")
    Tree.column("name", width=250)
    Tree.column("category", width=180)
    Tree.column("supplier", width=200)
    Tree.column("price", width=150, anchor="center")
    Tree.column("stock", width=120, anchor="center")

    Tree.pack(side="left")

    scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=Tree.yview)
    scrollbar.pack(side="right", fill="y")
    Tree.configure(yscrollcommand=scrollbar.set)

    # ---------------- Load Product Table ----------------
    def Productfunc():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.Product_id, p.Product_name, c.name AS Category_name,
                   s.Supplier_name, p.cost_price, p.Product_stock 
            FROM Product p 
            JOIN Category c ON p.category_id = c.category_id 
            JOIN Supplier s ON p.supplier_id = s.Supplier_id;
        """)
        datas = cursor.fetchall()
        conn.close()
        return datas
    
    def loadTable():
        for item in Tree.get_children():
            Tree.delete(item)

        for row in Productfunc():
            Tree.insert("", tk.END, values=row)
    
    loadTable()

    window.mainloop()
