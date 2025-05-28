todo_list=[]

#add task to todo_list
def add_task():
    task=input("Enter a task: ")
    todo_list.append({"Task":task,"Status":"Pending"})
    print("New task added successfully!!!")
    print("\n")

#function to view all tasks
def view_task():
    print("Your Todo List: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate (todo_list, 1):
            print(f"{index}: {task['Task']}-{task['Status']}")

    print("\n")

#Function to Remove a Task
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: "))-1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task}")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")


#Function to mark  a Task as done
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: "))-1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status']='Done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done")  
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")

def menu():
    while(True):
        print("1.Add a task")
        print("2.View all tasks")
        print("3.Remove a task")
        print("4.Marked as read")
        print("5.Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            mark_done()
        elif choice=="5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! try again!!!")
menu()
 

    




