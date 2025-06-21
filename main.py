from task_tracker.task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\nCommands: add [priority] description, list, listall, done [num], delete [num], exit")
        command = input(">>> ").strip()

        if command == "exit":
            break

        elif command == "list":
            manager.list_tasks()

        elif command == "listall":
            manager.list_tasks(show_all=True)

        elif command.startswith("add "):
            parts = command.split(" ", 2)
            if len(parts) == 3 and parts[1].isdigit():
                manager.add_task(parts[2], priority=parts[1])
            else:
                manager.add_task(command[4:])  # everything after "add "

        elif command.startswith("done "):
            try:
                num = int(command.split()[1])
                manager.mark_done(num)
            except:
                print("Usage: done [task number]")

        elif command.startswith("delete "):
            try:
                num = int(command.split()[1])
                manager.delete_task(num)
            except:
                print("Usage: delete [task number]")

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
