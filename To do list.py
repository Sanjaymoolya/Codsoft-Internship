import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack(pady=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task["completed"] else "Not Done"
            self.tasks_listbox.insert(tk.END, f"{idx}. {task['task']} [{status}]")
    
    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]]["task"] = new_task
                self.update_tasks_listbox()
                self.task_entry.delete(0, tk.END)
    
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()
    
    def mark_task_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_tasks_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
