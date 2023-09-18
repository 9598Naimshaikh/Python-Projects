# Question 17: Implement a To-Do List

# please question definition check to `Question-17.md` files.


class TodoList:

    def __init__(self):
        self.task = []

    def add_task(self):
        """Add to task as a todolist"""
        task = input('Enter a task which do you want to add: ')
        self.task.append(task)
        print(f'Your task {task!r} successfully added!')

    def view_task(self):
        """Display the todolist tasks."""
        print("To-Do List")
        for index, task in enumerate(self.task, start=1):
            print(f'{index}. {task}')

    def mark_task_as_done(self):
        """mark tasks as done or completed."""
        task_num = int(input('Enter the task number which do you want to done: '))
        for index, task in enumerate(self.task, start=1):
            if task_num == index:
                print(f"Task {task!r} marked done.!")

    def delete_task(self):
        """Delete the task as giving user task number"""
        task_num = int(input("Enter the task number which do you want to delete: "))
        for index, task in enumerate(self.task, start=1):
            if task_num == index:
                self.task.remove(task)
                print(f'Task {task!r} deleted!')


todo1 = TodoList()

# todo1.add_task()
# todo1.add_task()
# todo1.view_task()
# todo1.mark_task_as_done()
# todo1.delete_task()
# todo1.view_task()


if __name__ == "__main__":
    print("To-Do List Program")
    print("-------------------")

    while True:
        print("\n1. Add a task \
            \n2. View tasks \
            \n3. Mark a task as done \
            \n4. Delete a task \
            \n5. Quit\n")

        choice = int(input("Enter choice $$: "))

        if choice == 1:
            todo1.add_task()
        elif choice == 2:
            todo1.view_task()
        elif choice == 3:
            todo1.mark_task_as_done()
        elif choice == 4:
            todo1.delete_task()
        elif choice == 5:
            print("GoodBye")
            break
