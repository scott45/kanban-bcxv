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


