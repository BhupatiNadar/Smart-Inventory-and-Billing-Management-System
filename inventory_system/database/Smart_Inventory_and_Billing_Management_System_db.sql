create database Smart_Inventory_and_Billing_Management_System;

use Smart_Inventory_and_Billing_Management_System;

create table USER(
admin_id int primary key auto_increment,
username varchar (100) not null,
password varchar (100) not null,
role enum('admin','staff') default 'staff'
);

insert into user (username,password,role) value("Admin@gmail.com","8097",'admin');

select * from User;

-- # table --

INSERT INTO Supplier (Supplier_name, Supplier_contact, Supplier_email, Supplier_address) VALUES
('TechSource Pvt Ltd', '9876543210', 'contact@techsource.com', 'Mumbai, India'),
('Global Traders', '9123456780', 'info@globaltraders.com', 'Delhi, India'),
('Prime Electronics', '9988776655', 'support@primeelec.com', 'Bangalore, India'),
('Digital Hub', '9090909090', 'sales@digitalhub.com', 'Hyderabad, India'),
('Star Infotech', '9812345678', 'hello@starinfo.com', 'Chennai, India'),
('Rapid Suppliers', '9000011111', 'service@rapid.com', 'Pune, India'),
('Metro Distributors', '8787878787', 'metro@distributors.com', 'Kolkata, India'),
('Future Store', '8877665544', 'future@store.com', 'Jaipur, India'),
('Quality Supplies', '9955667788', 'quality@supply.com', 'Lucknow, India'),
('Best Electronics', '9099887766', 'contact@bestelec.com', 'Surat, India');


INSERT INTO Category (name) VALUES
('Laptop'),
('Mouse'),
('Keyboard'),
('Monitor'),
('Printer'),
('Headphones'),
('Speakers'),
('Smartphone'),
('Cable'),
('Accessories');


INSERT INTO Product (Product_name, cost_price, sell_price, category_id, supplier_id, Product_stock) VALUES
('HP Pavilion 15', 45000, 52000, 1, 1, 20),
('Dell Wireless Mouse', 300, 450, 2, 2, 100),
('Logitech Keyboard K120', 400, 600, 3, 3, 75),
('Samsung 24-inch Monitor', 7000, 8500, 4, 4, 30),
('Canon Inkjet Printer', 5000, 6200, 5, 5, 15),
('Sony Over-ear Headphones', 1500, 1990, 6, 6, 50),
('JBL Bluetooth Speaker', 1800, 2300, 7, 7, 40),
('Redmi Note 12', 10000, 12000, 8, 8, 25),
('HDMI Cable', 120, 200, 9, 9, 200),
('Sandisk 32GB Pen Drive', 300, 450, 10, 10, 150);


INSERT INTO customer_management (customer_name, Customer_email, total_purchase, Customer_phone_no) VALUES
('Rahul Sharma', 'rahul@gmail.com', 0, '9876543210'),
('Amit Verma', 'amit@gmail.com', 0, '9123456780'),
('Sneha Kapoor', 'sneha@gmail.com', 0, '9988776655'),
('Neha Singh', 'neha@gmail.com', 0, '9090909090'),
('Vikas Kumar', 'vikas@gmail.com', 0, '9812345678'),
('Manoj Das', 'manoj@gmail.com', 0, '9000011111'),
('Rita Mehta', 'rita@gmail.com', 0, '8787878787'),
('Pooja Patel', 'pooja@gmail.com', 0, '8877665544'),
('Arjun Rana', 'arjun@gmail.com', 0, '9955667788'),
('Kiran Yadav', 'kiran@gmail.com', 0, '9099887766');

INSERT INTO sales (customer_id, total_amount) VALUES
(1, 52000),
(2, 450),
(3, 600),
(4, 8500),
(5, 6200),
(6, 1990),
(7, 2300),
(8, 12000),
(9, 200),
(10, 450);

INSERT INTO sales_items (invoice_id, product_id, quantity, price) VALUES
(1, 1, 1, 52000),
(2, 2, 1, 450),
(3, 3, 1, 600),
(4, 4, 1, 8500),
(5, 5, 1, 6200),
(6, 6, 1, 1990),
(7, 7, 1, 2300),
(8, 8, 1, 12000),
(9, 9, 2, 400),
(10, 10, 1, 450);


SELECT 
    p.Product_id,
    p.Product_name,
    c.name AS Category_name,
    s.Supplier_name,
    p.cost_price,
    p.Product_stock
FROM Product p
JOIN Category c ON p.category_id = c.category_id
JOIN Supplier s ON p.supplier_id = s.Supplier_id;
