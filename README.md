# CongNgheWeb

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
