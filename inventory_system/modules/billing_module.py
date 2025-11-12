import tkinter as tk

def BillingAndPOS_panel():
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


    left_panel = tk.Frame(MainBody, bg='white', bd=2, relief='ridge', width=500, height=600)
    left_panel.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    left_panel.pack_propagate(False)
    tk.Label(left_panel, text='Billing Panel', font=('Ariel', 20, 'bold'), pady=8,bg='white').grid(row=0, column=0, columnspan=2)

    
    right_panel = tk.Frame(MainBody, bg='white', bd=2, relief='ridge', width=500, height=600)
    right_panel.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    right_panel.pack_propagate(False)
    tk.Label(right_panel, text='Cart / Bill Details', font=('Ariel', 20, 'bold'), pady=8,bg='white').grid(row=0, column=0, columnspan=3)

    window.mainloop()

BillingAndPOS_panel()
