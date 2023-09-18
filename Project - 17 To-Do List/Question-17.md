# **Question 17: Implement a To-Do List**

Create a simple command-line to-do list program in Python. 
Your program should allow users to perform the following operations:

1. Add a task: Users should be able to add tasks to their to-do list.
2. View tasks: Users should be able to view their current to-do list.
3. Mark a task as done: Users should be able to mark tasks as done or completed.
4. Delete a task: Users should be able to delete tasks from their to-do list.

You should implement these operations using functions and a list to store the tasks.
Here's a sample interaction with the program:

````
To-Do List Program
-------------------

1. Add a task
2. View tasks
3. Mark a task as done
4. Delete a task
5. Quit

Enter your choice: 1
Enter the task: Buy groceries
Task added successfully!

Enter your choice: 1
Enter the task: Clean the house
Task added successfully!

Enter your choice: 2
To-Do List:
1. Buy groceries
2. Clean the house

Enter your choice: 3
Enter the task number to mark as done: 1
Task 'Buy groceries' marked as done!

Enter your choice: 4
Enter the task number to delete: 2
Task 'Clean the house' deleted!

Enter your choice: 2
To-Do List:
1. Buy groceries

Enter your choice: 5
Goodbye!
````


You can continue adding more tasks, marking them as done, and deleting them until you choose to quit the program (option 5).

Your program should be user-friendly and handle different input cases gracefully (e.g., invalid task numbers, empty task list).