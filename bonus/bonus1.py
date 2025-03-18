import FreeSimpleGUI as ui
from zipcreator import make_archive

ui.theme("Black")

label1 = ui.Text("Select files to compress")
input1 = ui.InputText()
choose_button1 = ui.FileBrowse("Choose", key = "file")

label2 = ui.Text("Select destination folder")
input2 = ui.InputText()
choose_button2 = ui.FolderBrowse("Choose", key = "folder")

Extract_button = ui.button("Extract")
Output_label = ui.Text("", key = "Output", text_color="green")

compress_button = ui.Button("Compress")

window = ui.Window("File compressor",
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],
                           [compress_button]
                           [Extract_button,Output_label]])

while True:
    event, values =window.read()
    print(event)
    print(values)
    filepath = values["file"].split(";")
    folderpath = values["folder"]
    make_archive(filepath,folderpath)

window.close()