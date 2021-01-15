import psycopg2
from BusinessObject import Customer as CustomerEntity
from BusinessObject import Employee as EmployeeEntity
from BusinessObject import Supplier as SupplierEntity
from BusinessObject import Category as CategoryEntity
from BusinessObject import Order as OrderEntity
from BusinessObject import OrderDetail as OrderDetailEntity
from BusinessObject import Product as ProductEntity
from BusinessObject import Shipper as ShipperEntity

class Customer:
    def __init__(self,ConnectionData):
        self.ConnectionData = ConnectionData
    # Hàm insert thông tin customer vào bảng Customers
    def insert(self,customer):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Customers(CustomerName,ContactName, Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s)"
            record_to_insert = (customer.CustomerName,customer.ContactName,customer.Address,customer.City,customer.PostalCode,customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Customers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

        # Hàm lấy tất hàng có trong bảng Custumers
        def get_all(self):
            con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Customers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CustomerEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self,customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM Customers WHERE Customerid=%s"

            cur.execute(sql,(customer.CustomerID, ))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = CustomerEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    # Hàm update giá trị Custimer cho bảng Customers
    def update(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Customers SET Customername=%s,Contactname=%s, address=%s,City=%s, Postalcode=%s, Country=%s WHERE Customerid=%s"
            cur.execute(sql,(customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country, customer.CustomerID))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Updated Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    # Hàm xóa khách hàng với
    def delete(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  Customers WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
class Employee:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  Employees(lastname, firstname, birthdate, photo, notes) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  Employees successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  Employees"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = EmployeeEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  Employees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = EmployeeEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  employees SET lastname=%s, firstname=%s, birthdate=%s, photo=%s, notes=%s WHERE employeeid=%s"
            cur.execute(sql, (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes, employee.EmployeeID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  employees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Supplier:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, supplier):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  suppliers(Suppliername, ContactName, Address, City, PostalCode, Country, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            record_to_insert = (supplier.SupplierName, supplier.ContactName, supplier.Address, supplier.City, supplier.PostalCode, supplier.Country, supplier.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  suppliers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  suppliers"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = SupplierEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  suppliers WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = SupplierEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  suppliers SET suppliername=%s, contactname=%s, address=%s, city=%s, postalcode=%s, country=%s, phone=%s WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierName, supplier.ContactName, supplier.Address, supplier.City, supplier.PostalCode, supplier.Country, supplier.Phone, supplier.SupplierID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated supplier', 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  suppliers WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted supplier', 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
class Category:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  categories(categoryname, description) VALUES (%s, %s)"
            record_to_insert = (category.CategoryName, category.Description)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  categories successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  categories"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CategoryEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  categories WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = CategoryEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  categories SET categoryname=%s, description=%s WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryName, category.Description, category.CategoryID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated category', 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  categories WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted category', 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Order:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  orders(customerid, employeeid, orderdate, shipperid) VALUES (%s, %s, %s, %s)"
            record_to_insert = (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  orders successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  orders"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  orders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  orders SET customerid=%s, employeeid=%s, orderdate=%s, shipperid=%s WHERE orderid=%s"
            cur.execute(sql, (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID, order.OrderID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  orders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class OrderDetail:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  orderdetails(orderid, productid, quantity) VALUES (%s, %s, %s)"
            record_to_insert = (orderr.OrderID, orderr.ProductID, orderr.Quantity)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  orderdetails successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  orderdetails"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderDetailEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  orderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderDetailEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  orderdetails SET orderid=%s, productid=%s, quantity=%s WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderID, orderr.ProductID, orderr.Quantity, orderr.OrderDetailID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  orderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order detail', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Product:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, product):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  products(ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  Products successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  products"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ProductEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  products WHERE productid=%s"
            cur.execute(sql, (product.ProductID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = ProductEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  products SET productname=%s, supplierid=%s, categoryid=%s, unit=%s, price=%s WHERE productid=%s "
            cur.execute(sql,(product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price, product.ProductID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated product', 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  products WHERE productid=%s"
            cur.execute(sql,(product.ProductID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Product", 200
            con.close()
            return "Product ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Shipper:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, shipper):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO  shippers(ShipperID, ShipperName, Phone) VALUES (%s, %s, %s)"
            record_to_insert = (shipper.ShipperID, shipper.ShipperName, shipper.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert  Shippers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  shippers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ShipperEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM  shippers WHERE shipperid=%s"
            cur.execute(sql, (shipper.ShipperID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = ShipperEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Shipper ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE  shippers SET shippername=%s, phone=%s WHERE shipperid=%s "
            cur.execute(sql,(shipper.ShipperName, shipper.Phone, shipper.ShipperID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated shipper', 200
            con.close()
            return 'Shipper ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM  shippers WHERE shipperid=%s"
            cur.execute(sql,(shipper.ShipperID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Shipper", 200
            con.close()
            return "Shipper ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
if __name__ == "__main__":
    print('this is data object package')
