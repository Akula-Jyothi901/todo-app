import FreeSimpleGUI as ui

label = ui.Text("Type in To-Do")
input_box = ui.InputText(tooltip="Enter todo")
add_button = ui.Button("Add")

window = ui.Window("My To-Do App",layout=[[label],[input_box, add_button]])
window.read()
window.close()