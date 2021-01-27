import sqlite3


class Data:

    def create_table(db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Users(uid INT UNIQUE,name TEXT,last_name TEXT,age INT)')
        connection.commit()
        connection.close()

    def Control_Data_UID(db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            new_uid = uid[0]+1
        return new_uid
            
        
    def Add_Data(data,db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users VALUES(?,?,?,?)',(data.uid,data.name,data.last_name,data.age))
        connection.commit()
        connection.close()

    def Delete_Data(uid,db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Users WHERE uid=?',(uid,))
        connection.commit()
        connection.close()

    def List_Data(db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            print(uid)

    def Search_Data(search_id,db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            if (search_id == uid[0]):
                return True
            else:
                return False

