import random
def get_tasks(file="Task.txt"):
    with open(file, "r") as local_file:
        tasks = local_file.readlines()
    return tasks

def write_tasks(tasks, file="Task.txt"):
    with open(file, "w") as local_file:
        local_file.writelines(tasks)


def random_task(file="Task.txt"):
    with open(file, "r") as local_file:
        tasks = local_file.readlines()
    total_len = len(tasks)
    task_right_now = tasks[random.randint(0,(total_len-1))]
    return task_right_now
