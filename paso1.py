import pandas as pd
from sklearn.linear_model import LinearRegression
import PySimpleGUI as sg

layout = [[sg.Text('Archivo de datos: '), sg.Input(key='-INFILE-'), sg.FileBrowse()],
          [sg.Button('Predecir'), sg.Button('Cancelar')]]

window = sg.Window('Predicción de números de lotería', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancelar'):
        break
    if event == 'Predecir':
        infile = values['-INFILE-']
        break

window.close()
data = pd.read_csv('Resultados.csv', header=None)
y = data.iloc[:, -5:]
X = data.iloc[:, 1:6]

print(y)
print(X)

model = LinearRegression()
model.fit(X, y)

last_row = data.tail(1)
prediction = model.predict([last_row.iloc[:, 1:6].values.tolist()[0]])

sg.popup(f'Los números más probables para el próximo sorteo son: {prediction[0][0]:.0f}, {prediction[0][1]:.0f}, {prediction[0][2]:.0f}, {prediction[0][3]:.0f}, {prediction[0][4]:.0f}')
