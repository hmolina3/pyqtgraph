# -*- coding: utf-8 -*-
""" Programa que lee el puerto serial y espera una secuencia JSON con la estructura
    x: analogo0, y: 40, z: 30
    la cual es almacenada en forma de diccionario para posterior tratarlos como arrays
    y graficarlos a velocidad usando numpy y pyqtgraph"""

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial
import time
import json
import numpy as np

# Caracterizamos al puerto serie a utilziar
puerto = "/dev/cu.usbmodem14201"
baudrate = 9600

# Creamos el indice para que los almacene de la siguiente forma
signal = {'x': [], 'y': [], 'z': []}

# Intentamos conectar al pto. serie..... sino...FIN
try:
    ser = serial.Serial(puerto, baudrate)
except:
    print("Conexion fallida al puerto serial")
    exit()

# Creamos el set principal de la app y el widget
app = QtGui.QApplication([])
# Nombre de la ventana grafica
win = pg.GraphicsWindow(title="Grafica en tiempo real")
# Creacion del plot y su nombre
p = win.addPlot(title="Grafica tiempo real")
dataX = []
# print(signal.keys())
# Caracterizacion del grafico
curva = p.plot(pen ="b")
curva2 = p.plot(pen ="y")
curva3 = p.plot(pen ="w")
# Asignamos el rango del eje Y
p.setRange(yRange=[0, 120])

# Funcion que actualiza el plot con sus caracteristicas
def Update():
    # Esta es la cadena de caracteres leida por el puerto serial
    # en formato JSON.
    raw_data = ser.readline()
    # print(raw_data)
    try:
        # El modulo json permite convertir un string en formato JSON a
        # diccionarios de Python. Si el string no viene en el formato adecuado
        # o la informacion se corrompe, el programa nos lo reporta en
        # el bloque de excepcion ValueError;.
        json_data = json.loads(raw_data)
        for k in signal.keys():
            signal[k].append(json_data[k])
            # print(signal[k])
        # Actualizamos los datos y refrescamos la gráfica, si no hay valores
        # nos indica que la señal no contiene datos
        if len(signal[k]) > 0:
            # Obtiene los valores de las listas y obtiene el tamaño para el eje
            # de las X
            dataY = signal['x']
            dataY2 = signal['y']
            dataY3 = signal['z']
            dataX = np.arange(len(dataY))
            # Crea los array con numpy (mayor velocidad)
            dataY = np.array(dataY)
            dataY2 = np.array(dataY2)
            dataY3 = np.array(dataY3)
            # Traza las lineas (x, Y) de cada sensor
            curva.setData(dataX, dataY)
            curva2.setData(dataX, dataY2)
            curva3.setData(dataX, dataY3)
            #signal[k] = []
        else:
            print('señal sin datos')
            # print(signal[k])
    except ValueError:
        print('Datos corruptos: %s', raw_data)
    # Si el puerto sigue abierto, programamos otra llamada a la funcion para
    # volver a leer el puerto serial.

    QtGui.QApplication.processEvents()

# Se crea un hilo que esta actualizando lo mas rapido posible
# siempre que el puerto este abierto
if ser.is_open:
    t = QtCore.QTimer()
    t.timeout.connect(Update)
    t.start()
    # threading.Timer(10 / 10000., Update).start()
else:
    print('No se esta transmitiendo!')
pg.QtGui.QApplication.exec_()