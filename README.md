# Python-project-spring-25-clark4de-git

Intro

This script's purpose to to act as a Todo List Manager that enters tasks into a SQLite database where they can be managed. You are able to add tasks to the database; list out the tasks in the database filtering by due date, completion status, or just by due date descending (which is default); complete tasks in the database; and delete tasks from the database.

Documentation

The four main features of this script are the Add, List, Complete, and Delete features. The usage of this script is as follows: todolist.py [-h] {add,list,complete,delete} ... An argument {add,list,complete,delete} is required and each has their own usage which can be shown by running todolist.py {add,list,complete,delete} -h.

The Add argument requires another argument task which is a string. It also has an optional option of --due DATE which reuires the DATE argument to be numeric characters formatted as MM-DD-YYYY.

The List argument does not require other options/arguments and can run to list out the tasks in the database by due date descending. There are optional options of --due DATE which filters for a specific due date among the tasks and --completed [0,1] which filters based on completion status with 0 = incomplete and 1 = complete.

The Complete argument requires a task_id (which is the primary key associated with the task) argument to mark a task as complete.

The Delete argument requires a task_id (which is the primary key associated with the task) argument to delete a task from the database.