import PySimpleGUI as userInterface
from functions import get_tasks, write_tasks

action_label = userInterface.Text("Type in a Task")
userinput = userInterface.InputText(tooltip="Enter Task", key="User")
add_button = userInterface.Button("Add")
list_of_tasks = userInterface.Listbox(values=get_tasks(), key="tasks",size=(45,10), enable_events=True)
edit_button = userInterface.Button("Edit")
complete_button = userInterface.Button("Complete")
exit_button = userInterface.Button("Exit")

col = [[edit_button],[complete_button]]

window = userInterface.Window("Task Manger", layout=[[action_label], [userinput,add_button], [list_of_tasks, userInterface.Column(col)], [exit_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["tasks"])
    match event:
        case "Add":
            value_to_add = values["User"] + "\n"
            print(value_to_add)
            tasks = get_tasks()
            tasks.append(value_to_add)
            write_tasks(tasks)
            window["tasks"].update(values=tasks)
        case "Edit":
            try:
                value_to_edit = values["tasks"][0]
                tasks = get_tasks()
                index = tasks.index(value_to_edit)
                tasks[index] = values["User"]
                write_tasks(tasks)
                window["tasks"].update(values=tasks)
            except IndexError:
                userInterface.popup("Please select an task", font=("Times New Roman", 10))
        case "tasks":
            window["User"].update(value=values['tasks'][0])
        case "Complete":
            try:
                value_to_complete = values["tasks"][0]
                tasks = get_tasks()
                tasks.remove(value_to_complete)
                write_tasks(tasks)
                window["tasks"].update(values=tasks)
                window["User"].update(value="")
            except IndexError:
                userInterface.popup("Please select an task", font=("Times New Roman", 10))
        case "Exit":
            break
        case userInterface.WIN_CLOSED:
            break

window.close()
