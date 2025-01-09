#DANIYAL ARAIN

import os

class TodoTask:
    
    def __init__(self, name, description):
        
        self.name = name
        self.description = description
        self.completed = False
        self.next = None

class ToDoList:
    
    def __init__(self):
        
        self.head = None
        self.task_id_counter = 1

    def addTask(self, task_name, task_description):
        
            
        new_task = TodoTask(task_name, task_description)
        new_task.id = self.task_id_counter
        self.task_id_counter += 1         #Increment Counter

        if self.head is None:
            self.head = new_task
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = new_task
        print("Task added successfully to the to-do list!")

    def deleteTask(self, task_id):
                
        if self.head is None:
            print("No tasks to delete!")
            return

        if self.head.id == task_id:
            self.head = self.head.next
            print("Task deleted successfully!")
            return

        curNode = self.head
        prev = None
        while curNode:
            if curNode.id == task_id:
                prev.next = curNode.next
                print("Task deleted successfully!")
                return
            prev = curNode
            curNode = curNode.next
        print("Task not found!")

    def searchTask(self, task_id):
                
        curNode = self.head
        while curNode:
            if curNode.id == task_id:
                return curNode
            curNode = curNode.next
        return None

    def displayTasks(self, show_completed=False):
        
        
        if self.head is None:
            print("No tasks to display")
            return

        curNode = self.head
        while curNode:
            if show_completed or not curNode.completed:
                status = "Completed" if curNode.completed else "Not Completed"
                print(f"Task ID: {curNode.id} - Task: {curNode.name} - Status: {status}")
            curNode = curNode.next

    def markCompleted(self, task_id):
        
        task = self.searchTask(task_id)
        if task:
            task.completed = True
            print("Task marked as completed!")
        else:
            print("Task not found!")

            
            
def print_menu():
    print("\nTo-Do List Menu")
    print("1. Add Your Task")
    print("2. Display Your Tasks")
    print("3. Search Your Task")
    print("4. Delete  Your Task")
    print("5. Mark Task as Completed")
    print("6. Quit")
    print()

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_description = input("Enter the task description: ")
            todo_list.addTask(task_name, task_description)

        elif choice == "2":
            todo_list.displayTasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter the task ID to search: "))
                task = todo_list.searchTask(task_id)
                if task:
                    status = "Completed" if task.completed else "Not Completed"
                    print(f"Task found: Task ID: {task.id} - Task: {task.name} - Status: {status}")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter the task ID to delete: "))
                todo_list.deleteTask(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "5":
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                todo_list.markCompleted(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

    
        elif choice == "6":
            print("Quitting the program...")
            break

        else:
            print("Invalid Input! Please try again.")
