def get_tasks(file="Task.txt"):
    with open(file, "r") as local_file:
        tasks = local_file.readlines()
    return tasks

def write_tasks(tasks, file="Task.txt"):
    with open(file, "w") as local_file:
        local_file.writelines(tasks)
