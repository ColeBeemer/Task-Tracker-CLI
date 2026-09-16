import sys          # For exiting the program
import shlex        # For parsing user input
import commands     # Extra file with methods for commands
import json         # For importing/exporting JSON file

def main():

    TASKS = {}  # Initialize empty dictionary for TASKS

    # Open file
    with open("TASKS.json") as f:
        y = f.read()    # Read the JSON
        if not y:
            i = int(0)  # If JSON file is empty, set initial ID to 0
        else:
            TASKS = json.loads(y)       # load JSON file into TASKS
            key = list(TASKS.keys())    # Get just the keys into a list
            key.reverse()               # Flip the list so the last key is first
            i = int(key[0])             # Set initial ID to the first key in the list

    while True:
        choice = input("> ")

        if not choice:
            print("No command entered. Type 'help' to show list of commands")
            continue

        parsed = shlex.split(choice)    # Grab the input and turn into a list
        length = int(len(parsed))       # Get the length for error handling
        command = parsed[0].upper()     # The first item in the input is the command

        # ===== COMMANDS =====

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
            elif length == 2 or length > 3:
                print('Incorrect amount of values. For TASKS with more than one word, use quotations. Ex. "<task>"')
            else:
                id = parsed[1]
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
                id = parsed[1]
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
                id = parsed[1]
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
                id = parsed[1]
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