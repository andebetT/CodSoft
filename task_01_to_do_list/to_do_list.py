print("well come to to do list app")
Task_list=[]
def add_task():
    new_task=input("please enter your new task")
    Task_list.append(new_task)
    print(f"you have added the task {new_task} successfully")
def delete_task():
    task = input("please enter your task you want to delete")
    if task in Task_list:
        Task_list.remove(task)
        print("you have deleted the task successfully")
    else:
        print(f"the task {task}is not found in the task list")
def list_task():
    print("here are list of task")
    for task in Task_list:
        print(task)
while True:
    print("please select one of the following option")
    print("select 1:to add new task")
    print("select 2:to delete task")
    print("select 3:to list the  task")
    print("select 4:to exit")
    choice=input("please enter your choice")
    if choice=="1":
        add_task()
    elif choice=="2":
        delete_task()
    elif choice=="3":
        list_task()
    elif choice=="4":
        print("than you for your vist")
        break
    else:
        print("please select among the given choice only")

