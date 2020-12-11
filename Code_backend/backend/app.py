from flask import Flask
import os
import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)

dp_ip = os.getenv("db_ip")
ConnectionData = {}
ConectionData['user' = 'postgres']
ConnectionData['host'] = string(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'teamhhl'

@app.route("/")
def hello():
    c1 = bo.Customer(1,'DAU xanh','Peter','566 Nui Thanh', 'Da Nang','5000','VietNam')
    return c1.CustomerName
@app.route("/test_insert")
def test_inset():
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1,'DAU xanh','Peter','566 Nui Thanh', 'Da Nang','5000','VietNam')
    s1 = c2.insert(c1)
    return s1

if __name == "__main__":
    app.run(host='0.0.0.0',port=8080)