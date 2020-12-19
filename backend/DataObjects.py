import psycopg2
class Customers:
    def __init__(slef,ConnectionData = None):
        if ConnectionData is None:
            self.ConnectionData = ConnectionData
    def insert(self,customers):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Customers(CustomerName,ContactName, Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s)"
            record_to_insert = (customers.CustomerName,customers.ContactName,customers.Address,customers.City,customers.PostalCode,customers.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Customers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
if __name__ == "__main__":
    print('this is data object package')
