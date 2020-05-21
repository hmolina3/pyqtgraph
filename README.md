# pyqtgraph

Programa que lee el puerto serial y espera una secuencia JSON con la estructura:
    <br> x: analogo0, y: 40, z: 30 <br>
si la estructura no corresponde a la anterior o se corrompo el programa no toma los 
datos e infomra en pantalla.
La  estructura es almacenada en forma de diccionario para posterior tratarlos como arrays
y graficarlos a velocidad usando numpy y pyqtgraph.

El archivo "ino" es una implementación para leer un puerto analogo
y enviarla por serial dentro de la estructura:
    x: analogo0, y: 40, z: 30

se han colocado como constantes 40 y 30 pero se pueden sustituir por variables de otros puertos 
análogos y enviar en la estructura anterior, de igual forma se pueden incorporar mas variables como 
sea necesario.  
