import sqlite3
from aifc import Error


class DatabaseManager:


    def create_connection(db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
                return conn

    def database_create(self, conn):
        c = conn.cursor()  # saved in py file
        # CREATE TABLE RIGHT HAND
        sql= 'CREATE DATABASE IF NOT EXISTS "User_Data.db"';
        c.execute(sql)
        c.execute('''CREATE TABLE RIGHT_HAND
             ([INDEX] INTEGER PRIMARY KEY,[FORCE] float, [FLEX] float , [ACCELERATION] float)''')
        c.execute('''CREATE TABLE LEFT_HAND
                 ([INDEX] INTEGER PRIMARY KEY,[FORCE] float, [FLEX] float , [ACCELERATION] float)''')
        c.execute('''CREATE TABLE RIGHT_LEG
                 ([INDEX] INTEGER PRIMARY KEY,[FORCE] float, [FLEX] float , [ACCELERATION] float)''')
        c.execute('''CREATE TABLE LEFT_LEG
                 ([INDEX] INTEGER PRIMARY KEY,[FORCE] float, [FLEX] float , [ACCELERATION] float)''')
        c.execute('''CREATE TABLE USER_LOGIN
                 ([INDEX] INTEGER PRIMARY KEY,[USERNAME] String, [PASSWORD] String , [ACCELERATION] float)''')
        conn.commit()

        return conn

    def database_insert(self, conn, table_name, values):
        if table_name == 'LEFT_HAND':
            c = conn.cursor()
            sql = ''' INSERT INTO LEFT_HAND(INDEX,FORCE,FLEX,ACCELERATION)
                      VALUES(?,?,?,?,?,?) '''
            c.execute(sql, values)
            conn.commit()

        if table_name == 'RIGHT_HAND':
            c = conn.cursor()
            sql = ''' INSERT INTO RIGHT_HAND(INDEX,FORCE,FLEX,ACCELERATION)
                          VALUES(?,?,?,?,?,?) '''
            c.execute(sql, values)
            conn.commit()

        if table_name == 'LEFT_LEG':
            c = conn.cursor()
            sql = ''' INSERT INTO LEFT_LEG(INDEX,FORCE,FLEX,ACCELERATION)
                          VALUES(?,?,?,?,?,?) '''
            c.execute(sql, values)
            conn.commit()
        if table_name == 'RIGHT_LEG':
            c = conn.cursor()
            sql = ''' INSERT INTO RIGHT_LEG(INDEX,FORCE,FLEX,ACCELERATION)
                          VALUES(?,?,?,?,?,?) '''
            c.execute(sql, values)
            conn.commit()
