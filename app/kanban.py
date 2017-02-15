__author__ = 'Scott Businge'

# import statements
import sqlite3
import datetime as datetime
import time as guage
from tabulate import tabulate


# class definition
class ToDo(object):
    # initiation method
    def __init__(self):

        self.datetime = datetime
        self.time = guage
        self.data = 'mydatabase.db'

        self.db = sqlite3.connect(self.data)
        self.cursor = self.db.cursor()

        try:
            self.db.execute('''CREATE TABLE mydatabase
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_detail TEXT NOT NULL,
                             task_label TEXT ,
                             task_on DATETIME,
                             time_off DATETIME,
                             time_taken DATETIME)''')

        except sqlite3.OperationalError:
            pass

            # function to perform task_add

    def to_do(self, name, detail):
        self.db.execute('INSERT INTO mydatabase(task_name, task_detail, task_label) VALUES (?,?,?)', (name,
                                                                                                      detail, 'todo'))
        self.db.commit()
        print("Saved to-do input")
        print("Name: {}\nDescription: {}".format(name, detail))

    # current function for doing that is to handle all tasks being done now.

    def doing(self, task_id, task_on):
        if task_on:
            begin_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
            move = 'UPDATE mydatabase SET task_label = "doing",task_on ="{}" WHERE task_id = {}'.format(begin_time,
                                                                                                        task_id)
            self.db.execute(move)
            self.db.commit()
            print("Moved to Doing")

            # done function for done that is to handle all tasks that are done.3

    def done(self, task_id, time_off):
        if time_off:
            end_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
            sort = 'UPDATE mydatabase SET task_label = "done",time_off ="{}" WHERE task_id = {}'.format(end_time,
                                                                                                        task_id)
            self.db.execute(sort)
            self.db.commit()
            print("Task accomplished")

            # list to-do function that is to handle the listing of all to dos.

    # duration function that is to handle the time taken on a task.

    def duration(self, time_taken):
        get = self.cursor.execute("SELECT* FROM todo WHERE task_label = 'done'")
        accomplished = self.cursor.fetchall()
        for row in accomplished:
            off = (row[5])
            on = (row[4])
            off_obj = datetime.datetime.strptime(off, '%Y-%m-%d %H:%M:%S')
            on_obj = datetime.datetime.strptime(on, '%Y-%m-%d %H:%M:%S')
            duration = off_obj - on_obj
            difference = 'UPDATE mydatabase SET time_taken ="{}" WHERE task_id = {}'.format(str(duration), row[0])

            self.db.execute(difference)
            self.db.commit()

    def list_to_do(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='todo'")
        all = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        tablet = []
        for row in all:
            rows = [row[0], row[1], row[2], row[3]]
            tablet.append(rows)
        print(tabulate(tablet, headers, tablefmt="fancy_grid"))

        self.db.commit()

    # current function for doing that is to handle all tasks being done now.
    def doing(self, task_id, task_on):
        if task_on:
            begin_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
            move = 'UPDATE mydatabase SET task_label = "doing",task_on ="{}" WHERE task_id = {}'.format(begin_time,
                                                                                                        task_id)
            self.db.execute(move)
            self.db.commit()
            print("Moved to Doing")

    # list done function that is to handle the listing of all to dos.
    def list_done(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='done'")
        accomplished = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table_2 = []
        for row in accomplished:
            rec = [row[0], row[1], row[2], row[3]]
            table_2.append(rec)
        print(tabulate(table_2, headers, tablefmt="fancy_grid"))

    # list all function that is to handle the listing of all recorded tasks regardless of label.
    def list_all(self):
        self.cursor.execute("SELECT * FROM mydatabase ")
        all_rows = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label", "time"]
        table = []
        for row in all_rows:
            task_id = row[0]
            task_name = row[1]
            task_detail = row[2]
            task_label = row[3]

            time_taken = "Not started"

            if task_label == 'doing':
                time_taken = "Started"
            elif task_label == 'done':
                off = (row[5])
                on = (row[4])
                off_obj = datetime.datetime.strptime(off, '%Y-%m-%d %H:%M:%S')
                on_obj = datetime.datetime.strptime(on, '%Y-%m-%d %H:%M:%S')
                time_taken = off_obj - on_obj

            rec = [task_id, task_name, task_detail, task_label, time_taken]
            table.append(rec)

        print(tabulate(table, headers, tablefmt="fancy_grid"))


db = ToDo()
# db.to_do(name="oop", detail="inheritance")
# db.doing(task_on=datetime, task_id=1)
# db.done(time_off=datetime, task_id=1)
# db.list_to_do()
