class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        """View all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

    def mark_complete(self, task_number):
        """Mark a task as complete."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        """Delete a task from the list."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number!")

def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            task_manager.mark_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            task_manager.delete_task(task_number)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
