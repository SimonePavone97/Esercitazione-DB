import mysql.connector


class DataBaseconnector:


    @classmethod
    def executeQuery(cls, query):
        cls.connection = mysql.connector.connect(
            host='localhost', user='root', passwd='Smemo2014.', port='3306', database='sakila')

        cursor = cls.connection.cursor()
        cursor.execute(query)

        return cursor.fetchall()

    @classmethod
    def close(cls):
        if cls.connection != None:
            cls.connection.close()
