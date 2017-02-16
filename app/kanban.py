__author__ = 'Scott Businge'

# import statements
import sqlite3
import datetime as datetime
import time as guage
from tabulate import tabulate
import json
import csv
from firebase import firebase
from time import sleep
from tqdm import tqdm

# class definition
class ToDo(object):
    # initiation method
    def __init__(self):

        self.datetime = datetime
        self.time = guage
        self.data = 'mydatabase.db'

        self.conn = sqlite3.connect(self.data)
        self.cursor = self.conn.cursor()

        try:
            self.conn.execute('''CREATE TABLE mydatabase
                             (task_id INTEGER PRIMARY KEY,
                             task_name TEXT NOT NULL,
                             task_detail TEXT NOT NULL,
                             task_label TEXT,
                             task_on DATETIME NOT NULL,
                             time_off DATETIME NOT NULL ,
                             time_taken DATETIME NOT NULL )''')

        except sqlite3.OperationalError:
            print("database still initialising the data")

            # function to perform task_add

    def to_do(self, name, detail):
        self.conn.execute('INSERT INTO mydatabase(task_name, task_detail, task_label) VALUES (?,?,?)', (name,
                                                                                                      detail, 'todo'))
        self.conn.commit()
        print("Saved to-do input")
        print("Name: {}\nDescription: {}".format(name, detail))

    # current function for doing that is to handle all tasks being done now.

    def doing(self, task_id):

        begin_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
        task = 'SELECT task_id from mydatabase WHERE task_id = {}'.format(task_id)
        self.conn.execute(task)
        result = self.cursor.fetchone()

        if not result:
            print("Sorry the task doesn't exist")

        move = 'UPDATE mydatabase SET task_label = "doing",task_on ="{}" WHERE task_id = {}'.format(begin_time,
                                                                                                    task_id)
        self.conn.execute(move)
        self.conn.commit()
        return "Moved to Doing"

        # done function for done that is to handle all tasks that are done.3

    def done(self, task_id):
        end_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
        sort = 'UPDATE mydatabase SET task_label = "done",time_off ="{}" WHERE task_id = {}'.format(end_time,
                                                                                                    task_id)
        self.conn.execute(sort)
        self.conn.commit()
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

            self.conn.execute(difference)
            self.conn.commit()

    def list_todo(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='todo'")
        all = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        tablet = []
        for row in all:
            rows = [row[0], row[1], row[2], row[3]]
            tablet.append(rows)
        print(tabulate(tablet, headers, tablefmt="fancy_grid"))

        self.conn.commit()

    # list done function that is to handle the listing of all doing
    def list_doing(self):
        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='doing'")
        accomplished = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table_2 = []
        for row in accomplished:
            rec = [row[0], row[1], row[2], row[3]]
            table_2.append(rec)
        print(tabulate(table_2, headers, tablefmt="fancy_grid"))

    # list done function that is to handle the listing of all done.
    def list_done(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='done'")
        accomplished = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table_2 = []
        for row in accomplished:
            rec = [row[0], row[1], row[2], row[3]]
            table_2.append(rec)
        print(tabulate(table_2, headers, tablefmt="fancy_grid"))

    def edit(self, task_id, name, detail):
        task = 'SELECT task_id from mydatabase WHERE task_id = {}'.format(task_id)
        self.cursor.execute(task)
        result = self.cursor.fetchone()
        if not result:
            return "Task does not exits"

        self.conn.execute('UPDATE  mydatabase SET task_name = ?,task_detail = ? WHERE task_id = ?', (name, detail, task_id))
        self.conn.commit()
        print("Edited and saved to-do input")
        print("Name: {}\nDescription: {}".format(name, detail))

    def delete(self, task_id):
        remove = 'DELETE FROM mydatabase WHERE task_id = {}'.format(task_id)
        self.conn.execute(remove)
        print("Deleted Name: {}".format(task_id))

    # A method to implement sycnching notes with firebase
    def sync(self):
        self.cursor.execute("SELECT * FROM mydatabase")
        result_rows = self.cursor.fetchall()
        fiybase = firebase.FirebaseApplication('https://scott-kanban.firebaseio.com/')
        result = fiybase.post('/', json.dumps(result_rows))
        print('Hold on as your data is being synced!')
        self.conn.commit()
        for i in tqdm(range(200)):
            sleep(0.01)
        print('Sync complete')
'''
    # A method to implement exporting notes
    def export(self):
        file_name = input("kindly provide a name to the notes: ")
        cur = self.conn.cursor()
        cur.execute("SELECT content->'name' as name, content->'detail' as detail from mydatabse")
        result_rows = cur.fetchall()
        with open(file_name + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'detail'])
            writer.writerows(result_rows)
        print('Tasks are being exported')
        for i in tqdm(range(200)):
            sleep(0.01)
        cur.close()
        self.conn.commit()

    def import_file(self):
        # Check to see first the given directory is correct
        try:
            file_name = input('kindly key in the file location: ')
            with open(file_name, 'rb') as csvfile:
                rows = csv.reader(csvfile, quotechar='|')
                for row in rows:
                    self.save_imported_tasks(row[0], row[1])
            # Just for a good UI
            print('Tasks are being imported')

            for i in tqdm(range(200)):
                sleep(0.01)

            print('Complete')
        # if the directory given is wrong
        except IOError:
            print('File not found')

    # A utility function to insert data read from a csv
    def save_imported_tasks(self, name, detail):
        cur = self.conn.cursor()
        json_data = {"name": name, "detail": detail}
        cur.execute("""INSERT INTO mydatabase(content) VALUES (%s)""", [json.dumps(json_data)])
        cur.close()
        self.conn.commit()

    # list all function that is to handle the listing of all recorded tasks regardless of label.
    def list_all(self):
        self.cursor.execute("SELECT * FROM mydatabase ")
        all_rows = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table = []
        for row in all_rows:
            task_id = row[0]
            task_name = row[1]
            task_detail = row[2]
            task_label = row[3]

            rec = [task_id, task_name, task_detail, task_label]
            table.append(rec)

        print(tabulate(table, headers, tablefmt="fancy_grid"))
'''

db = ToDo()
# db.list_all()
# db.to_do(name="oop", detail="inheritance")
# db.doing(task_on=datetime, task_id=1)
# db.done(time_off=datetime, task_id=1)
# db.list_to_do()
