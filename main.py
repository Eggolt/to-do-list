"""
-Task
-List
"""
from list import List
def main():
    user = input('Input user name: ')
    todo = List(user)
    while True:
        action = input('Would you like to? 1) Add Task 2) Remove Task 3) Print List: ')
        if int(action) == 1:
            description = input('Enter task description: ')
            dueDate = input('Enter task dueDate (MM/DD/YYYY): ')
            todo.createTask(description, dueDate)
            print('Task Created')
        elif int(action) == 2:
            num = input('Which task would you like to remove?: ')
            todo.deleteTask(int(num))
        elif int(action) == 3:
            todo.printList()
        elif 'q' in action:
            break

if __name__ == "__main__":
  main()