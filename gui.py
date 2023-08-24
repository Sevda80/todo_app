import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
text_box = sg.InputText(tooltip='Enter a todo')
add_button = sg.Button("ADD")

window = sg.Window("My to-do app", layout=[[label], [text_box, add_button]])
window.read()
window.close()
