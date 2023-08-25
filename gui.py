import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
text_box = sg.InputText(tooltip='Enter a todo', key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [text_box, add_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
    elif event == sg.WIN_CLOSED:
        break


window.close()
