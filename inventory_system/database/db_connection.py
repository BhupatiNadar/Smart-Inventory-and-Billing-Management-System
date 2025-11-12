import mysql.connector # type: ignore

def create_connection():
    try:
        conn = mysql.connector.connect(
        host="localhost",        
        user="root",            
        password="Bhupati",
        database=" Smart_Inventory_and_Billing_Management_System")
        
        return conn
    except mysql.connector as err:
        print(f"Error:{err}")
        return None
         