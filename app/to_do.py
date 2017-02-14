__author__ = 'Scott Businge'

# import statements
import sqlite3 as db
import datetime as datetime
import time as guage


# class definition
class ToDo(object):
    # initiation method
    def __init__(self):

        self.datetime = datetime
        self.time = guage
        self.data = 'mydatabase.db'

        self.db = db.connect(self.data)
        self.cursor = self.db.cursor()

        try:
            self.db.execute('''CREATE TABLE to_do
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_detail TEXT NOT NULL,
                             task_label TEXT ,
                             task_on DATETIME,
                             time_off DATETIME,
                             time_taken DATETIME)''')

        except db.OperationalError:
            pass

# function to perform task_add
