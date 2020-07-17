import sqlite3
from sqlite3 import Error
# The CRUD class contains all the essential querys to create, read, update and delete tables


class CRUD:
    def __init__(self, database):
        self.database = database

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)

    def create_customerTable(self):
        query = """ CREATE TABLE contact (
                    cust_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT ,
                    phone TEXT,
                    address1 TEXT, 
                    address2 TEXT, 
                    address3 TEXT, 
                    towncity TEXT, 
                    postcode TEXT,
                    company TEXT,
                    detail TEXT
                    )
                    """
        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query)
        conn.commit()


    def insert_customer(self, cust_id, first_name, last_name, email,phone_num,
                        add1, add2, add3, towncity, postcode, company, detail):
        query = """INSERT INTO contact (cust_id, first_name, last_name, email, phone, address1, address2, address3, towncity, postcode, company, detail)
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query, (cust_id, first_name, last_name, email, phone_num, add1, add2, add3, towncity, postcode, company, detail))
        conn.commit()


    def read_all(self, table_name):
        query = "SELECT * FROM {}".format(table_name)

        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()

        for row in rows:
            print(row)

    def update_table(self, table_name, column_name, update_data, cust_id):
        query = "UPDATE {} SET {} = ? WHERE cust_id =?".format(table_name, column_name)

        conn = self.create_connection()
        c = conn.cursor()
        c.execute(query, (update_data, cust_id))
        conn.commit()

    def delete_table(self, table_name, cust_id):
        query = "DELETE FROM {} WHERE cust_id = {}".format(table_name, cust_id)

        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(query)
            conn.commit()
        except:
            print('ERROR')
    
 

if __name__ == "__main__":
    app = CRUD('crud.db')
    app.create_connection()
    