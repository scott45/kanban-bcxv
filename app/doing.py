__author__ = 'Scott Businge'

# import statements
from app.to_do import ToDo
import datetime
import time as guage


# class doing
class Doing(ToDo):
    # current function for doing that is to handle all tasks being done now.
    def doing(self, task_id, task_on):
        if task_on:
            begin_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
            move = 'UPDATE mydatabase SET task_label = "doing",task_on ="{}" WHERE task_id = {}'.format(begin_time,
                                                                                                        task_id)
            self.db.execute(move)
            self.db.commit()
            print("Moved to Doing")
