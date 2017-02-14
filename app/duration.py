__author__ = 'Scott Businge'

# import statements
from app import to_do
import datetime


# class done
class Duration(to_do):
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
