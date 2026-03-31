# Importa todas las funciones de la librería turtle (para gráficos)
from turtle import *

# Importa la función hsv_to_rgb para manejar colores en formato HSV
from colorsys import *

# Aumenta la velocidad de dibujo (menos animación, más rápido)
tracer(400)

# Establece el color de fondo en negro
bgcolor('black')

# Oculta la tortuga (el cursor)
hideturtle()

# Define el grosor del lápiz
pensize(2)

# Levanta el lápiz (no dibuja mientras se mueve)
penup()

# Mueve la tortuga a la posición (0, 100)
goto(0,100)

# Baja el lápiz para empezar a dibujar
pendown()

# Inicializa el valor del tono (hue) para los colores
h = 0.10

# Bucle principal que se repite 360 veces (genera la figura completa)
for i in range(360):
    
    # Cambia el color usando el sistema HSV convertido a RGB
    # h = tono, 1 = saturación máxima, 1 = brillo máximo
    color(hsv_to_rgb(h,1,1))
    
    # Incrementa el tono para ir cambiando el color (efecto arcoíris)
    h += 5/8

    # Segundo bucle que crea los patrones repetitivos
    for j in range(420):
        
        # Avanza 90 unidades
        forward(90)
        
        # Dibuja un círculo de radio 70 con 380 grados (más de una vuelta)
        circle(70, 380)
        
        # Retrocede 90 unidades (vuelve al punto anterior)
        backward(90)
        
        # Gira 40 grados a la derecha
        right(40)
        
        # Gira 17 grados adicionales a la derecha
        right(17)

# Mantiene la ventana abierta
done()