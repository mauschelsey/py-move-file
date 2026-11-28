import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return

    action, source, target = command_list

    if action != "mv" or not os.path.isfile(source):
        return

    if "/" not in target:
        if os.path.isdir(target):
            destination = os.path.join(target, source)
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(destination, "w") as file_out:
                file_out.write(content)
            os.remove(source)
        else:
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(target, "w") as file_out:
                file_out.write(content)
            os.remove(source)
    elif target.endswith("/"):
        if os.path.isdir(target):
            destination = str(target) + str(source)
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(destination, "w") as file_out:
                file_out.write(content)
            os.remove(source)
        else:
            file_path = str(target) + str(source)
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(file_path, "w") as file_out:
                file_out.write(content)
            os.remove(source)
    else:
        new_file_path = target.split("/")
        for i in range(len(new_file_path) - 1):
            partial_path = "/".join(new_file_path[:i + 1])
            if not os.path.exists(partial_path):
                os.makedirs(partial_path, exist_ok=True)

        if os.path.isdir(target):
            destination = str(target) + str(source)
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(destination, "w") as file_out:
                file_out.write(content)
            os.remove(source)
        else:
            with open(source, "r") as file_in:
                content = file_in.read()
            with open(target, "w") as file_out:
                file_out.write(content)
            os.remove(source)
