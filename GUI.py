import FreeSimpleGUI as ui

label = ui.Text("Type in To-Do")
input_box = ui.InputText(tooltip="Enter todo")
add_button = ui.Button(size=10, image_source="add.png")

window = ui.Window("My To-Do App",
                   layout=[[label],[input_box, add_button]],
                   font = ("Helvetica", 10))

event = window.read()
print(event)
window.close()