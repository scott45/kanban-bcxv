__author__ = 'Scott Businge'

# import statements
from app import to_do
from tabulate import tabulate
import datetime


# class done
class List(to_do):
    # list to-do function that is to handle the listing of all to dos.
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

    # list to-do function that is to handle the listing of all being done.
    def list_doing(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='doing'")
        current = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table = []
        for row in current:
            columns = [row[0], row[1], row[2], row[3]]
            table.append(columns)
        print(tabulate(table, headers, tablefmt="fancy_grid"))

        self.db.commit()

    # list to-do function that is to handle the listing of all to dos.
    def list_done(self):

        self.cursor.execute("SELECT * FROM mydatabase WHERE task_label='done'")
        accomplished = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table_2 = []
        for row in accomplished:
            rec = [row[0], row[1], row[2], row[3]]
            table_2.append(rec)
        print(tabulate(table_2, headers, tablefmt="fancy_grid"))

        self.db.commit()

    # list to-do function that is to handle the listing of all recorded tasks regardless of label.
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


db = to_do()
