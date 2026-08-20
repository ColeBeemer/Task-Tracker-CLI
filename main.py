import time
import sys
import shlex

TASKS = {}

def add(task, i):
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

def update(id, task):
    TASKS[id]["description"] = task

def delete(id):
    del TASKS[id]

def mark_in_progress(id):
    TASKS[id]["status"] = "in-progress"

def mark_done(id):
    TASKS[id]["status"] = "done"

def list(status=None):

    if status:
        for i in TASKS:
            if TASKS[i]["status"] == status:
                print(f"Task {i}:")
                print(f"\tDescription: {TASKS[i]["description"]}")
                print(f"\tStatus: {TASKS[i]["status"]}")
                print(f"\tCreated at: {TASKS[i]["createdAt"]}")
                print(f"\tLast updated: {TASKS[i]["updatedAt"]}\n")
    else:
        for i in TASKS:
            print(f"Task {i}:")
            print(f"\tDescription: {TASKS[i]["description"]}")
            print(f"\tStatus: {TASKS[i]["status"]}")
            print(f"\tCreated at: {TASKS[i]["createdAt"]}")
            print(f"\tLast updated: {TASKS[i]["updatedAt"]}\n")

def main():
    i = int(0)
    while True:
        choice = input()
        parsed = shlex.split(choice)
        length = int(len(parsed))
        command = parsed[0].upper()

        if command == "ADD":
            i += 1
            task = parsed[1]
            add(task, i)
            print(f"Task added successfully (ID: {i})\n")

        elif command == "UPDATE":
            id = int(parsed[1])
            task = parsed[2]
            update(id, task)
            print(f"Task (ID: {id}) updated to {task}\n")

        elif command == "DELETE":
            id = int(parsed[1])
            delete(id)
            print(f"Task (ID: {id}) deleted successfully\n")

        elif command == "MARK-IN-PROGRESS":
            id = int(parsed[1])
            mark_in_progress(id)
            print(f"Task (ID: {id}) marked as in-progress\n")

        elif command == "MARK-DONE":
            id = int(parsed[1])
            mark_done(id)
            print(f"Task (ID: {id}) marked as done\n")

        elif command == "LIST":
            if length == 1:
                list()
            else:
                status = parsed[1]
                list(status)

        elif command == "EXIT":
            sys.exit("Closing program.")

        parsed.clear()

if __name__ == "__main__":
    main()