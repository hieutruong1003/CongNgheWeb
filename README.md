# CongNgheWeb

<<<<<<< HEAD
## Thành Viên Nhóm HHL:
## 1. Trương Văn Hiếu
## 2. Phạm Trung Hoài
## 3. Phan Thanh Lâm

# Entity

## Bảng Customer
* CustomerID: int
* CustomerName: string
* ContactName: string
* Address: string
* City: string
* PostalCode: string
* Country: string

## Bảng Categories
* CategoryID: serial
* CategoryName: string
* Description: string

## Bảng Shippers
* ShipperID: serial
* ShipperName: string
* Phone: string

## Bảng Suppliers
* SupplierID: string
* SupplierName: string
* ContactName: string
* Address: string
* City: string
* PostalCode: string
* Country: string
* Phone: string

## Bảng Employees
* EmployeeID: int
* LastName: string
* FirstName: string
* Birthdate: date
* Photo: string
* Notes: string

## Bảng Products
* ProductID: int
* ProductName: string
* Unit: string
* Price: int
* SupplierID: int
* CategoryID: int

## Bảng Orders
* OrderID: int
* CustomerID: int
* EmployeeID: int
* OrderDate: date
* ShipperID: int

## Bảng Orderdetails
* OrderDetailID: int
* OrderID: int
* ProductID: int
* QUantity: int

# API
## Customer
### Create a Customer
* Request
    * Method: POST
    * Endpoint: /customer/insert
    * Body:
        * CustomerID: int
        * CustomerName: string
        * ContactName: string
        * Adress: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message
### GET all Customer
* Request
    * Method: POST
    * Endpoint: /customer/all
    * Body:
        * CustomerID: int
        * CustomerName: string
        * ContactName: string
        * Adress: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /customer/update/:customer_id
    * Body:
        * CustomerID: int
        * CustomerName: string
        * ContactName: string
        * Adress: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /customer/delete/:customer_id
* Response: message
### Get a customer
* Request
    * Method: POST
    * Endpoint: /customer/get/:customer_id
    * Body:
        * CustomerID: int
        * CustomerName: string
        * ContactName: string
        * Adress: string
        * City: string
        * PostalCode: string
        * Country: string
* Response: Message

## Employees
### Create a Employees
* Request
    * Method: POST
    * Endpoint: /employee/insert
    * Body:
        * EmployeeID: int
        * LastName: string
        * FirstName: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message
### GET all Employees
* Request
    * Method: POST
    * Endpoint: /employee/all
    * Body:
        * EmployeeID: int
        * LastName: string
        * FirstName: string
        * Birthdate: string
        * Photo: string
        * Notes: string
* Response: Message
### Update a Employee
* Request:
    * Method: PUT
    * Endpoint: /employee/update/:employee_id
    * Body:
        * EmployeeID: int
        * LastName: string
        * FirstName: string
        * Birthdate: string
        * Photo: string
        * Notes: string
* Response: Message

### Delete a Employee
* Request:
    * Method: DELETE
    * Endpoint: /employee/delete/:employee_id
* Response: message
### Get a Employee
* Request
    * Method: POST
    * Endpoint: /employee/get/:employee_id
    * Body:
        * EmployeeID: int
        * LastName: string
        * FirstName: string
        * Birthdate: string
        * Photo: string
        * Notes: string
* Response: Message

## Suppliers
### Create a Supplier
* Request
    * Method: POST
    * Endpoint: /employee/insert
    * Body:
        * SuppliersID: int
        * LastName: string
        * FirstName: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message
### GET all Supplier
* Request
    * Method: POST
    * Endpoint: /supplier/all
    * Body:
        * SuppliersID: int
        * SupplierName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
        * Phone: string
* Response: Message
### Update a Supplier
* Request:
    * Method: PUT
    * Endpoint: /supplier/update/:supplier_id
    * Body:
        * SuppliersID: int
        * SupplierName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
        * Phone: string
* Response: Message

### Delete a Supplier
* Request:
    * Method: DELETE
    * Endpoint: /supplier/delete/:supplier_id
* Response: message
### Get a Supplier 
* Request
    * Method: POST
    * Endpoint: /supplier/get/:supplier_id
    * Body:
        * SuppliersID: int
        * SupplierName: string
        * ContactName: string
        * Address: string
        * City: string
        * PostalCode: string
        * Country: string
        * Phone: string
* Response: Message

## Categorys
### Create a Category
* Request
    * Method: POST
    * Endpoint: /category/insert
    * Body:
        * CategoryID: int
        * CategoryName: string
        * Description: string
* Response: Message
### GET all Category
* Request
    * Method: POST
    * Endpoint: /category/all
    * Body:
        * CategoryID: int
        * CategoryName: string
        * Description: string
* Response: Message
### Update a Category
* Request:
    * Method: PUT
    * Endpoint: /category/update/:category_id
    * Body:
        * CategoryID: int
        * CategoryName: string
        * Description: string
* Response: Message

### Delete a Category
* Request:
    * Method: DELETE
    * Endpoint: /category/delete/:category_id
* Response: message
### Get a Category 
* Request
    * Method: POST
    * Endpoint: /category/get/:category_id
    * Body:
        * CategoryID: int
        * CategoryName: string
        * Description: string
* Response: Message

## Order
### Create a Order
* Request
    * Method: POST
    * Endpoint: /order/insert
    * Body:
        * OrderID: int
        * CustomerID: int
        * EmployeeID: int
        * OrderDate: date
        * ShipperID: int
* Response: Message
### GET all Order
* Request
    * Method: POST
    * Endpoint: /order/all
    * Body:
        * OrderID: int
        * CustomerID: int
        * EmployeeID: int
        * OrderDate: date
        * ShipperID: int
* Response: Message
### Update a Order
* Request:
    * Method: PUT
    * Endpoint: /order/update/:order_id
    * Body:
        * OrderID: int
        * CustomerID: int
        * EmployeeID: int
        * OrderDate: date
        * ShipperID: int
* Response: Message

### Delete a Order
* Request:
    * Method: DELETE
    * Endpoint: /order/delete/:order_id
* Response: message
### Get a Order 
* Request
    * Method: POST
    * Endpoint: /order/get/:order_id
    * Body:
        * OrderID: int
        * CustomerID: int
        * EmployeeID: int
        * OrderDate: date
        * ShipperID: int
* Response: Message

## Orderdetails
### Create a Orderdetail
* Request
    * Method: POST
    * Endpoint: /order_detail/insert
    * Body:
        * OrderDetailID: int
        * OrderID: int
        * ProductID: int
        * Quantity: int
* Response: Message
### GET all Orderdetail
* Request
    * Method: POST
    * Endpoint: /order_detail/all
    * Body:
        * OrderDetailID: int
        * OrderID: int
        * ProductID: int
        * Quantity: int
* Response: Message
### Update a Orderdetail
* Request:
    * Method: PUT
    * Endpoint: /ororder_detailder/update/:odd_id
    * Body:
        * OrderDetailID: int
        * OrderID: int
        * ProductID: int
        * Quantity: int
* Response: Message

### Delete a Orderdetail
* Request:
    * Method: DELETE
    * Endpoint: /order_detail/delete/:odd_id
* Response: message
### Get a Orderdetail 
* Request
    * Method: POST
    * Endpoint: /order_detail/get/:odd_id
    * Body:
        * OrderDetailID: int
        * OrderID: int
        * ProductID: int
        * Quantity: int
* Response: Message

## Product
### Create a Product
* Request
    * Method: POST
    * Endpoint: /product/insert
    * Body:
        * ProductID: int
        * ProductName: string
        * SupplierID: int
        * CategoryID: int
        * Unit: string
        * Price: int
* Response: Message
### GET all Product
* Request
    * Method: POST
    * Endpoint: /product/all
    * Body:
        * ProductID: int
        * ProductName: string
        * SupplierID: int
        * CategoryID: int
        * Unit: string
        * Price: int
* Response: Message
### Update a Product
* Request:
    * Method: PUT
    * Endpoint: /product/update/:product_id
    * Body:
        * ProductID: int
        * ProductName: string
        * SupplierID: int
        * CategoryID: int
        * Unit: string
        * Price: int
* Response: Message

### Delete a Product
* Request:
    * Method: DELETE
    * Endpoint: /product/delete/:product_id
* Response: message
### Get a Product 
* Request
    * Method: POST
    * Endpoint: /product/get/:product_id
    * Body:
        * ProductID: int
        * ProductName: string
        * SupplierID: int
        * CategoryID: int
        * Unit: string
        * Price: int
* Response: Message

## Shipper
### Create a Shipper
* Request
    * Method: POST
    * Endpoint: /shipper/insert
    * Body:
        * ShipperID: int
        * ShupperName: string
        * Phone: string
* Response: Message
### GET all Shipper
* Request
    * Method: POST
    * Endpoint: /shipper/all
    * Body:
        * ShipperID: int
        * ShupperName: string
        * Phone: string
* Response: Message
### Update a Shipper
* Request:
    * Method: PUT
    * Endpoint: /shipper/update/:shipper_id
    * Body:
        * ShipperID: int
        * ShupperName: string
        * Phone: string
* Response: Message

### Delete a Shipper
* Request:
    * Method: DELETE
    * Endpoint: /shipper/delete/:shipper_id
* Response: message
### Get a Shipper 
* Request
    * Method: POST
    * Endpoint: /shipper/get/:shipper_id
    * Body:
        * ShipperID: int
        * ShupperName: string
        * Phone: string
* Response: Message

=======
## Chào Bạn!!!
## Trương Văn Hiếu
## Phạm Trung Hoài
## Phan Thanh Lâm

#câu lệnh docker
sudo docker build -t backend . (build project)
sudo docker run -d --name backend --env dp_ip=10.0.2.15 -p 8080:8080 backend (chạy)
sudo docker stop backend
sudo docker rm backend
sudo docker rm --force backend

#lenh kết nối csdl
sudo docker exec -it coredb bash
#postgres
//sudo docker run -d --restart unless-stopped --name coredb -e POSTGTRES_PASSWORD=postgres -e POSGRESS_DB=postgres -v ~northwind db:var/lib/postgresql/data -p 5432:5432 postgres
sudo docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
sudo docker exec -it my-postgres bash
psql -U postgres
\l(liệt kê danh sách database) - \c database(connect)
CREATE TABLE TblCustomers (
    CustomerID SERIAL PRIMARY KEY,
    CustomerName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255)
);

CREATE TABLE tblcategories (
    CategoryID SERIAL PRIMARY KEY,
    CategoryName varchar(255),
    Description varchar(255)
);

CREATE TABLE tblshippers (
    ShipperID SERIAL PRIMARY KEY,
    ShipperName varchar(255),
    Phone varchar(255)
);

CREATE TABLE tblsuppliers (
    SupplierID SERIAL PRIMARY KEY,
    SupplierName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255),
    Phone varchar(255)
);

CREATE TABLE tblemployees (
    EmployeeID SERIAL PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    Birthdate DATE,
    Photo varchar(255),
    Notes varchar(255)
);

CREATE TABLE tblproducts (
    ProductID SERIAL PRIMARY KEY,
    ProductName varchar(255),
    Unit varchar(255),
    Price int,
    SupplierID int,
    CategoryID int
);

CREATE TABLE tblorders (
    OrderID SERIAL PRIMARY KEY,
    CustomerID int,
    EmployeeID int,
    OrderDate DATE,
    ShipperID int
);

CREATE TABLE tblorderdetails (
    OrderDetailID SERIAL PRIMARY KEY,
    OrderID int,
    ProductID int,
    Quantity int
);
>>>>>>> main
