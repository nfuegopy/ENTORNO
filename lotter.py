import random
import PySimpleGUI as sg

# Creamos una lista con los números del 1 al 49
numeros = [x for x in range(1, 50)]

# Creamos una lista vacía para almacenar los números adivinados
adivinados = []

# Creamos una ventana con PySimpleGUI
layout = [[sg.Text('Presiona el botón para adivinar los números de la lotería')],
          [sg.Button('Adivinar'), sg.Exit()]]

window = sg.Window('Lotería', layout)

# Iteramos mientras la ventana esté abierta
while True:
    event, values = window.read()
    
    # Si se presiona el botón de adivinar, elegimos seis números al azar
    if event == 'Adivinar':
        for i in range(6):
            numero_elegido = random.choice(numeros)
            adivinados.append(numero_elegido)
            numeros.remove(numero_elegido)
        
        # Mostramos una ventana con los números adivinados
        sg.popup("Los números adivinados son:", adivinados)
        
        # Reiniciamos las listas para volver a jugar
        adivinados = []
        numeros = [x for x in range(1, 50)]
    
    # Si se presiona el botón de salir, cerramos la ventana y salimos del programa
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

window.close()
