task_list = []

def addtask():
    while True:
        tasks = input("What task would you like to add? type 'done' when complete >>\n") 
        if tasks.lower() == 'done':
            print ("Your task have been added")
            break
        else:
            task_list.append(tasks)
    print(f"'{tasks}' has been added!")


def viewtask():
    if not task_list:
        print("There are no task currently.")
    else:
        print (f"Here is your current To-do list: \n{task_list}")
        for index, tasks in enumerate(task_list, start=1):
            print(f"Task #{index}. {tasks}")


def deletetask():
    viewtask()
    try:
        deletedtasks = int(input("Please enter the # you want to delete.\n"))
        if deletedtasks >= 0 and deletedtasks < len(task_list):
            task_list.pop(deletedtasks)
            print (f"{deletedtasks} has been removed.")
        else:
            print("Task not found.")
    except:
        print("Invalid Input")

while True:
    print(''' 
          \nMain Menu:
          1. View Task
          2. Add Task
          3. Delete Completed task
          4. End To - Do list
           ''')
    try:
        user_input = int(input("How would you like to proceed? Please select a number 1-4 \n>>"))
        if user_input == 1:
            viewtask() 
        elif user_input == 2:
            addtask()
        elif user_input == 3:
            deletetask()
        elif user_input == 4:
            break
        else:
            print("Sorry, Invalid Input, please try again!")
    except ValueError:
        print("Please enter a number.")
print ("Thank you! Have a great day!")