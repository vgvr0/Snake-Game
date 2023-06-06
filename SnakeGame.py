import pygame
import random

# Dimensiones de la ventana del juego
ancho_ventana = 640
alto_ventana = 480

# Tamaño de cada segmento de la serpiente y de la comida
tamanio_segmento = 20

# Velocidad de movimiento de la serpiente
velocidad = 15

# Colores
color_fondo = (0, 0, 0)
color_serpiente = (0, 255, 0)
color_comida = (255, 0, 0)

def juego_serpiente():
    pygame.init()
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Juego de la Serpiente")

    reloj = pygame.time.Clock()

    # Inicialización de la serpiente
    serpiente = []
    serpiente.append((ancho_ventana // 2, alto_ventana // 2))
    direccion = "derecha"

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ancho_ventana - tamanio_segmento) / tamanio_segmento) * tamanio_segmento
    comida_y = round(random.randrange(0, alto_ventana - tamanio_segmento) / tamanio_segmento) * tamanio_segmento

    fin_juego = False

    while not fin_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_juego = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direccion != "derecha":
                    direccion = "izquierda"
                elif event.key == pygame.K_RIGHT and direccion != "izquierda":
                    direccion = "derecha"
                elif event.key == pygame.K_UP and direccion != "abajo":
                    direccion = "arriba"
                elif event.key == pygame.K_DOWN and direccion != "arriba":
                    direccion = "abajo"

        if direccion == "izquierda":
            serpiente[0] = ((serpiente[0][0] - velocidad) % ancho_ventana, serpiente[0][1])
        elif direccion == "derecha":
            serpiente[0] = ((serpiente[0][0] + velocidad) % ancho_ventana, serpiente[0][1])
        elif direccion == "arriba":
            serpiente[0] = (serpiente[0][0], (serpiente[0][1] - velocidad) % alto_ventana)
        elif direccion == "abajo":
            serpiente[0] = (serpiente[0][0], (serpiente[0][1] + velocidad) % alto_ventana)

        ventana.fill(color_fondo)

        pygame.draw.rect(ventana, color_comida, (comida_x, comida_y, tamanio_segmento, tamanio_segmento))

        for segmento in serpiente:
            pygame.draw.rect(ventana, color_serpiente, (segmento[0], segmento[1], tamanio_segmento, tamanio_segmento))

        pygame.display.update()

        if serpiente[0] == (comida_x, comida_y):
            comida_x = round(random.randrange(0, ancho_ventana - tamanio_segmento) / tamanio_segmento) * tamanio_segmento
            comida_y = round(random.randrange(0, alto_ventana - tamanio_segmento) / tamanio_segmento) * tamanio_segmento
            serpiente.append((serpiente[-1][0], serpiente[-1][1]))

        for segmento in serpiente[1:]:
            if segmento == serpiente[0]:
                fin_juego = True

        serpiente.insert(0, serpiente[0])
        serpiente.pop()

        reloj.tick(30)

    pygame.quit()

juego_serpiente()
