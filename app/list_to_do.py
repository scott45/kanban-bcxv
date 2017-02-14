__author__ = 'Scott Businge'

# import statements
from app import to_do
from tabulate import tabulate
import datetime


# class done
class List(to_do):

    # list to-do function that is to handle the listing of all to dos.
    def list_to_do(self):

        self.cursor.execute("SELECT * FROM todo WHERE task_label='todo'")
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

        self.cursor.execute("SELECT * FROM todo WHERE task_label='doing'")
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

        self.cursor.execute("SELECT * FROM todo WHERE task_label='done'")
        accomplished = self.cursor.fetchall()
        headers = ["id", "name", "detail", "label"]
        table_2 = []
        for row in accomplished:
            rec = [row[0], row[1], row[2], row[3]]
            table_2.append(rec)
        print(tabulate(table_2, headers, tablefmt="fancy_grid"))

        self.db.commit()
