import os
import shutil
import time
import PySimpleGUI as sg
from values import *
from preparing import *
from sorting import *
import logging

layout = [
    [sg.Text('Folder:'), sg.InputText(key='-FOLDER-'), sg.FolderBrowse('Choose folder')],
    [sg.Button('Sort'), sg.Button('Exit')],
]

window = sg.Window('File Sorter', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Sort':
        logging.log(1, '-------------------------------------')
        prepare(values['-FOLDER-'])
        sort_files()