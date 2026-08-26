import sys
import shlex
import commands
import json

def main():

    TASKS = {}

    with open("TASKS.json") as f:
        y = f.read()
        if not y:
            i = int(0)
        else:
            TASKS = json.loads(y)
            key = list(TASKS.keys())
            key.reverse()
            i = int(key[0])

    while True:
        choice = input()

        if not choice:
            print("No command entered. Type 'help' to show list of commands")
            continue

        parsed = shlex.split(choice)
        length = int(len(parsed))
        command = parsed[0].upper()

        if command == "ADD":

            if length == 1:
                print("No task inputted. Type 'help' to show list of commands")
                continue
            elif length > 2:
                print('Too many inputs. For TASKS with more than one word, use quotations. Ex. "<task>"')
                continue
            else:
                i += 1
                task = parsed[1]
                commands.add(TASKS, task, i)
                print(f"'{task}' added successfully (ID: {i})")

        elif command == "UPDATE":

            if length == 1:
                print("No id or new description inputted. Type 'help' to show list of commands")
                continue
            if length == 2 or length > 3:
                print('Incorrect amount of values. For TASKS with more than one word, use quotations. Ex. "<task>"')
                continue
            else:
                id = int(parsed[1])
                task = parsed[2]
                commands.update(TASKS, id, task)
                print(f"Task (ID: {id}) updated to {task}")

        elif command == "DELETE":

            if length == 1:
                print("No id inputted. Type 'help' to show list of commands")
                continue
            elif length > 2:
                print("Too many values inputted. Type 'help' to show list of commands")
                continue
            else:
                id = int(parsed[1])
                commands.delete(TASKS, id)
                print(f"Task (ID: {id}) deleted successfully")

        elif command == "MARK-IN-PROGRESS":

            if length == 1:
                print("No id inputted. Type 'help' to show list of commands")
                continue
            elif length > 2:
                print("Too many values inputted. Type 'help' to show list of commands")
                continue
            else:
                id = int(parsed[1])
                commands.mark_in_progress(TASKS, id)
                print(f"Task (ID: {id}) marked as in-progress")

        elif command == "MARK-DONE":

            if length == 1:
                print("No id inputted. Type 'help' to show list of commands")
                continue
            elif length > 2:
                print("Too many values inputted. Type 'help' to show list of commands")
                continue
            else:
                id = int(parsed[1])
                commands.mark_done(TASKS, id)
                print(f"Task (ID: {id}) marked as done")

        elif command == "LIST":
            if length == 1:
                commands.list_TASKS(TASKS)
                continue
            elif length > 2:
                print("Too many values inputted. Type 'help' to show a list of commands")
                continue

            status = parsed[1].lower()
            if status == "todo" or status == "in-progress" or status == "done":
                commands.list_TASKS(TASKS, status)
            else:
                print("Incorrect status. Use 'todo', 'in-progress', or 'done'")

        elif command == "EXIT":
            sys.exit("Closing program.")

        elif command == "HELP":
            if length > 1:
                print("Too many inputs. Type 'help' to show a list of commands")
                continue
            else:
                commands.show_help()

        else:
            print("Invalid command. Type 'help' to show a list of commands")

        parsed.clear()

        x = json.dumps(TASKS)

        with open("TASKS.json", "wt") as f:
            f.write(x)

if __name__ == "__main__":
    main()