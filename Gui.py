import PySimpleGUI as userInterface
import random
from functions import get_tasks, write_tasks, random_task

action_label = userInterface.Text("Type in a Task")
userinput = userInterface.InputText(tooltip="Enter Task", key="User")
add_button = userInterface.Button("Add")
list_of_tasks = userInterface.Listbox(values=get_tasks(), key="Tasks",size=(45,10), enable_events=True)
edit_button = userInterface.Button("Edit")
complete_button = userInterface.Button("Complete")
random_button = userInterface.Button("Random")
exit_button = userInterface.Button("Exit")
random_label = userInterface.Text("", key="random")

col = [[edit_button],[complete_button],[random_button]]

window = userInterface.Window("Task Manger", layout=[[action_label], [userinput,add_button], [list_of_tasks, userInterface.Column(col)], [exit_button, random_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["Tasks"])
    match event:
        case "Add":
            value_to_add = values["User"].replace("\n","") + "\n"
            if(value_to_add.strip() == ""):
                userInterface.popup("Please write an task", font=("Times New Roman", 10))
                continue
            print(value_to_add)
            tasks = get_tasks()
            tasks.append(value_to_add)
            write_tasks(tasks)
            window["Tasks"].update(values=tasks)
            window["random"].update(value="")
        case "Edit":
            try:
                value_to_edit = values["Tasks"][0]
                tasks = get_tasks()
                index = tasks.index(value_to_edit)
                if(value_to_edit != values["User"]):
                    tasks[index] = values["User"] + "\n"
                write_tasks(tasks)
                print(tasks)
                window["Tasks"].update(values=tasks)
                window["random"].update(value="")
            except IndexError:
                userInterface.popup("Please select an task", font=("Times New Roman", 10))
        case "Tasks":
            window["User"].update(value=values['Tasks'][0])
        case "Random":
            task_right_now = random_task()
            window["random"].update(value=f"Random task to complete: {task_right_now}")
        case "Complete":
            try:
                value_to_complete = values["Tasks"][0]
                tasks = get_tasks()
                tasks.remove(value_to_complete)
                write_tasks(tasks)
                window["Tasks"].update(values=tasks)
                window["User"].update(value="")
                window["random"].update(value="")
            except IndexError:
                userInterface.popup("Please select an task", font=("Times New Roman", 10))
        case "Exit":
            break
        case userInterface.WIN_CLOSED:
            break

window.close()
