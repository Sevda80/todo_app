FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read the text file then return the list of to-do items. //This is doc-strings
    """
    with open(filepath, 'r') as local_file:
        """ Write in to-do items list in the text file."""
        local_todos = local_file.readlines()

    return local_todos


def write_todos( todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


if __name__ == "__main__":
    print('hello')
    print(get_todos())

