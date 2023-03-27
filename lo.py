import PySimpleGUI as sg
import openpyxl
import csv

# Crear la interfaz gráfica para seleccionar los archivos
layout = [[sg.Text('Archivo de origen: '), sg.Input(key='-INFILE-'), sg.FileBrowse()],
          [sg.Text('Archivo de destino: '), sg.Input(key='-OUTFILE-'), sg.FileSaveAs(file_types=(('Excel Files', '*.xlsx'),))],
          [sg.Button('Procesar'), sg.Button('Cancelar')]]

window = sg.Window('Procesamiento de archivo CSV', layout)

# Esperar a que el usuario seleccione los archivos
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancelar'):
        break
    if event == 'Procesar':
        infile = values['-INFILE-']
        outfile = values['-OUTFILE-']
        break

window.close()

# Procesar el archivo
wb = openpyxl.Workbook()
ws = wb.active
with open(infile, 'r') as f_in:
    reader = csv.reader(f_in)

    for row in reader:
        # Escribir los datos en el archivo de salida
        ws.append([row[0], row[3], row[4], row[6]])

wb.save(outfile)
