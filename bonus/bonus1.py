import FreeSimpleGUI as ui

label1 = ui.Text("Select files to compress")
input1 = ui.InputText()
choose_button1 = ui.FilesBrowse("Choose")

label2 = ui.Text("Select destination folder")
input2 = ui.InputText()
choose_button2 = ui.FilesBrowse("Choose")

window = ui.Window("File compressor", layout=[[label1,input1,choose_button1],[label2,input2,choose_button2]])

window.read()
window.close()