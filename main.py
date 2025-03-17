import FreeSimpleGUI as ui

feet = ui.Text("Enter Feet: ")
feet_input = ui.InputText()

inches = ui.Text("Enter Inches: ")
inches_input = ui.InputText()

convert_button = ui.button("Convert")

window = ui.Window("Convertor",layout=[[feet,feet_input],[inches,inches_input],[convert_button]])

window.read()
window.close()