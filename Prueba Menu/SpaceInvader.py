import pygame, sys
from pygame.locals import *

from Lose_Function import lose
from random import randint
from Clases import Nave
from Clases import Nave1
from Clases import Nave2
from Clases import Nave3
from Clases import Nave4
from Clases import Nave5
from Clases import Nave6
from Clases import Invasor as Enemigo


ancho = 900
alto = 400
listaEnemigo = []


def detenerTodo():
    for enemigo in  listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)

        enemigo.conquista = True


def cargarEnemigos(Dificultad): 
    posx = 100
    for x in range(1,5+Dificultad):
        enemigo = Enemigo(posx,100,40, "Imagenes/marcianoA.jpg","Imagenes/MarcianoB.jpg", Dificultad)
        listaEnemigo.append(enemigo)
        posx = posx+200
    
    posx = 100
    for x in range(1,5+Dificultad):
        enemigo2 = Enemigo(posx,0,40, "Imagenes/Marciano2A.jpg","Imagenes/Marciano2B.jpg", Dificultad)
        listaEnemigo.append(enemigo2)
        posx = posx+200

    posx = 100
    for x in range(1,5+Dificultad):
        enemigo3 = Enemigo(posx,-100,40, "Imagenes/Marciano3A.jpg","Imagenes/Marciano3B.jpg", Dificultad)
        listaEnemigo.append(enemigo3)
        posx = posx + 200

def SpaceInvader(Dificultad, ship_type):
    pygame.init()
    start_time = pygame.time.get_ticks()
    ventana =pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo = pygame.image.load("Imagenes/Fondo.jpg")
    Soundtrack = ["Sonidos/Soundtrack.mp3", "Sonidos/Soundtrack.mp3", "Sonidos/Soundtrack.mp3"]
    pygame.mixer.music.load(Soundtrack[Dificultad])  #Definir ruta
    pygame.mixer.music.play(3)
    Puntos = 0
    
    #Importar Nave

    if ship_type == "classic":
        jugador = Nave.naveEspacial(ancho,alto)
    elif ship_type == "space":
        jugador = Nave1.naveEspacial(ancho,alto)
    elif ship_type == "steel":
        jugador = Nave2.naveEspacial(ancho,alto)
    elif ship_type == "kappapride":
        jugador = Nave3.naveEspacial(ancho,alto)
    elif ship_type == "ice":
        jugador = Nave4.naveEspacial(ancho,alto)
    elif ship_type == "victorious":
        jugador = Nave5.naveEspacial(ancho,alto)
    elif ship_type == "cool":
        jugador = Nave6.naveEspacial(ancho,alto)


    
    miFuenteSistema = pygame.font.SysFont("Arial",30)
    cargarEnemigos(Dificultad)

    #DemoProyectil = Proyectil(ancho/2, alto-30)
    enJuego = True
    reloj = pygame.time.Clock()
    while True:
        tiempo = int(pygame.time.get_ticks()/1000)
        reloj.tick(60)
        #jugador.movimiento()
        #DemoProyectil.trayectoria()
        for evento in pygame.event.get():
            if evento.type ==QUIT:
                pygame.quit()
                sys.exit()

            if enJuego == True:
                if evento.type ==pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif evento.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif evento.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
        ventana.blit(ImagenFondo,(0,0))
        
        #DemoProyectil.dibujar(ventana)
        jugador.dibujar(ventana)   
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top <-10:
                    jugador.listaDisparo.remove(x)    
                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)
        
        if len(listaEnemigo) > 0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego = False
                    detenerTodo()
                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()

                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            detenerTodo()
                        if x.rect.top >900:
                            enemigo.listaDisparo.remove(x) 
                            Puntos = Puntos +1+Dificultad
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)
                                    Puntos = Puntos + 1 + Dificultad
                                    
        
        
        if enJuego == False:
            Texto = miFuenteSistema.render("Fin del juego, Puntos =" + str(Puntos), 0, (120,100,40))
            ventana.blit(Texto, (300,300))
            pygame.mixer.music.fadeout(3000)
            lose(Puntos,0, ship_type)
        pygame.display.update()
        

