import time

def add(TASKS, task, i):
    readable_time = time.ctime()
    TASKS.update({
        i : {
            "id" : i,
            "description" : task,
            "status" : "todo",
            "createdAt" : readable_time,
            "updatedAt" : readable_time
        }
    })

def update(TASKS, id, task):
    readable_time = time.ctime()
    TASKS[id]["description"] = task
    TASKS[id]["updatedAt"] = readable_time

def delete(TASKS, id):
    del TASKS[id]

def mark_in_progress(TASKS, id):
    readable_time = time.ctime()
    TASKS[id]["status"] = "in-progress"
    TASKS[id]["updatedAt"] = readable_time

def mark_done(TASKS, id):
    readable_time = time.ctime()
    TASKS[id]["status"] = "done"
    TASKS[id]["updatedAt"] = readable_time

def list_tasks(TASKS, status=None):
    j = 0

    if not TASKS:
        print("No tasks. Add tasks using 'add <task>'")
        return

    if status:
        for i in TASKS:
            if TASKS[i]["status"] == status:
                print(f"Task {i}:")
                print(f"\tDescription: {TASKS[i]["description"]}")
                print(f"\tStatus: {TASKS[i]["status"]}")
                print(f"\tCreated at: {TASKS[i]["createdAt"]}")
                print(f"\tLast updated: {TASKS[i]["updatedAt"]}\n")
                j += 1
        if j < 1:
            print(f"No tasks with status '{status}'")

    else:
        for i in TASKS:
            print(f"Task {i}:")
            print(f"\tDescription: {TASKS[i]["description"]}")
            print(f"\tStatus: {TASKS[i]["status"]}")
            print(f"\tCreated at: {TASKS[i]["createdAt"]}")
            print(f"\tLast updated: {TASKS[i]["updatedAt"]}\n")


def show_help():
    print("\nList of commands:")
    print("\t- add <task>:                      Adds a new task")
    print("\t- update <id> <new description>:   Updates a tasks description")
    print("\t- delete <id>:                     Deletes a task")
    print("\t- mark-in-progress <id>:           Change status of task to in-progress")
    print("\t- mark-done <id>:                  Change status of task to done")
    print("\t- list:                            Lists all the tasks")
    print("\t- list <status>:                   Lists all tasks with specified status")
    print("\t- exit:                            Exit the program\n")