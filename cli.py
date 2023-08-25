# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print(now)

while True:

    userAction = input("Enter show, add, edite, complete or exit: ")
    userAction = userAction.strip()
    # remove spaces

    if userAction.startswith('add'):

        todo = userAction[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif userAction.startswith('show') or userAction.startswith('display'):

        todos = functions.get_todos()

        """
        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
       """

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif userAction.startswith('edit'):
        try:

            number = int(userAction[5:])
            number = number - 1

            todos = functions.get_todos()

            newTodo = input("Enter new todo: ")
            todos[number] = newTodo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Command is not valid.")
            continue

    elif userAction.startswith('complete'):
        try:

            number = int(userAction[9:])

            todos = functions.get_todos()

            index = number - 1

            todoToRemove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todoToRemove} was removed from the list.'

            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif userAction.startswith('exit'):
        break

    else:
        print("Command is not valid!")
        
