import FreeSimpleGUI as ui
from convert import converts

ui.theme("black")

feet = ui.Text("Enter Feet: ")
feet_input = ui.InputText(key= "feetvalue")

inches = ui.Text("Enter Inches: ")
inches_input = ui.InputText(key = "inchesvalue")

convert_button = ui.Button("Convert")
Exit_button = ui.Button("Exit")

meter_output = ui.Text("", key="ouput")

window = ui.Window("Convertor",
                   layout=[[feet,feet_input],
                           [inches,inches_input],
                           [convert_button,Exit_button, meter_output]])

while True:
    try:
        event,values = window.read()
        feetinput = float(values["feetvalue"])
        inchesinput = float(values["inchesvalue"])

        result = converts(feetinput, inchesinput)
        window["output"].update(value=f"{result} m", text_color="white")

    except ValueError:
        ui.popup("Please provide two numbers", font=("Helvetica", 10))

window.close()