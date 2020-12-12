
import pygame
from random import randint
import Proyectil
class Invasor(pygame.sprite.Sprite):

    def __init__(self, posx, posy, distancia, imagen1, imagen2, Dificultad):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load(imagen1)
        self.imagenB = pygame.image.load(imagen2)
        self.listaImagenes = [self.imagenA, self.imagenB]
        self.posImagen = 0
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        self.listaDisparo = []
        self.velocidad = 20
        self.rect.top = posy
        self.rect.left = posx
        self.tiempoCambio = 1
        self.rangoDisparo = 1 + Dificultad             #Afecta dificultad del juego

        self.conquista = False

        self.derecha = True
        self.Contador = 0
        self.MaxDescenso = self.rect.top +40
        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posy - distancia

    def trayectoria(self):
        self.rect.top = self.rect.top -self.velocidadDisparo

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)

    def comportamiento(self,tiempo):
        #self.posImagen = int(tiempo % len(self.listaImagenes))
        if self.conquista == False:
            self.__movimientos()
            self.__ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen += 1
                self.tiempoCambio += 1

            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen = 0
    
    def __movimientos(self):
        if self.Contador < 3:
            self.__movimientoLateral()

        else:
            self.__Descenso()


    def __Descenso(self):
        if self.MaxDescenso == self.rect.top:
            self.Contador = 0
            self.MaxDescenso = self.rect.top + 40
        else:
            self.rect.top += 1
    def __movimientoLateral(self):
        if self.derecha:
           self.rect.left = self.rect.left + self.velocidad
           if self.rect.left > self.limiteDerecha:
               self.derecha = False
               self.Contador += 1
        else:
           self.rect.left = self.rect.left - self.velocidad
           if self.rect.left < self.limiteIzquierda:
               self.derecha = True
 
    def __ataque(self):
        if(randint(0,100)<self.rangoDisparo):
            self.__disparo()
    def __disparo(self):
        x,y = self.rect.center
        miProyectil=Proyectil.Proyectil(x,y,"Imagenes/disparob.jpg", False)
        self.listaDisparo.append(miProyectil)
