__author__ = 'Scott Businge'

# import statements
from app import to_do
import datetime
import time as guage


# class done
class Done(to_do):
    # done function for done that is to handle all tasks that are done.3
    def done(self, task_id, task_off):
        if task_off:
            end_time = datetime.datetime.fromtimestamp(guage.time()).strftime('%Y-%m-%d %H:%M:%S')
            sort = 'UPDATE mydatabase SET task_status = "done",time_stop ="{}" WHERE task_id = {}'.format(end_time,
                                                                                                       task_id)
            self.db.execute(sort)
            self.db.commit()
            print("Task accomplished")
