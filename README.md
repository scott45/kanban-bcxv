# KanBan Console App btcmp xv


# Kanban App
KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task.

# Requirements
todo <task name> - Adds a task in the todo section

doing <task-id>  - Moves the task with task-id to the doing section.

done <task-id>  - Moves the task with task-id to the the done section

list todo  - Lists all tasks that are in the doing section

list doing  - Lists all tasks that are in the doing section

list done  - Lists all tasks that are in the done section

list all  - Lists all the three sections of the KanBan board side-by-side.

All data should be persisted in an SQLite database.

Syncing the items on the cloud with Firebase will earn extra credits.


# Installation
First create a virtual environment to install the application's dependencies:
```sh
$ pip install virtualenv
$ environment_name/Scripts/activate
$ cd environment_name
```
To get started with kanban, clone this repository: 
```sh
$ git clone https://github.com/scott45/kanban-bcxv
$ cd app
$ pip install -r requirements.txt
```

# Running the App
Kanban was built with python 3.4, therefore may not work properly on other Python versions.
```sh
$ ./python docpt.py
"""""""""""'Add, edit, delete, and keep track of your tasks'"""""""""
(kanban)
```

# Functionality
### `help` command
The help command lists all commands executed by kanban
```sh
(kanban) help
Documented commands :
========================================
to_do  help  quit  doing  done  list_all  delete
list_done  list_doing  list_to_do  list_all  edit
```

### `to_do` command
To add a task, use the to_do command:
```sh
(kanban) to_do <task_name>
Enter detail: 
Saved to-do input
Name: ---
Description: ---
```


### `doing` command
To add a task to the doing section, use the doing command:
```sh
(kanban) doing <task_id>
Moved to Doing
```


### `done` command
To add a task to the done section, use the done command:
```sh
(kanban) done <task_id>
Task accomplished
```

### `list_to_do` command
To list all tasks to the to_do section, use the list_to_do command:
```sh
(kanban) list_to_do
```

### `list_doing` command
To list all tasks in the doing section, use the list_doing command:
```sh
(kanban) list_doing
```

### `list_done` command
To list all tasks in the done section, use the list_done command:
```sh
(kanban) list_done
```

### `list_all` command
To list all tasks in the three section regardless of status label as of to_do, doing or done, use the list_all command:
```sh
(kanban) list_all
```

### `quit` command
To close or exit the kanban console application, a user can use the `quit` command:
```sh
(kanban) quit
'Thank you for using Kanban, Later'
```
Since you are still in a virtualenv, you could deactivate the environment:
```

# Extra Functionalities (done)

Synchronize the Sqlite database to Firebase
Edit a task
Delete a task
help command
quit command
