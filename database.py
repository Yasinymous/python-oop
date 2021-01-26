import sqlite3


class Data:

    def create_table():
        connection = sqlite3.connect("user_db.db")
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Users(uid INT UNIQUE,name TEXT,last_name TEXT,age INT)')
        connection.commit()
        connection.close()

    def Control_Data_UID():
        connection = sqlite3.connect("user_db.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            new_uid = uid[0]+1
        return new_uid
            
        
    def Add_Data(data):
        connection = sqlite3.connect("user_db.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users VALUES(?,?,?,?)',(data.uid,data.name,data.last_name,data.age))
        connection.commit()
        connection.close()

        
        