import pygame

size = width, height = [800 / 2, 224]
posfondox = 0
posfondoy = 0
matrix = []
jugadores = pygame.sprite.Group()
jugadoresenemigos = pygame.sprite.Group()
barriles = pygame.sprite.Group()
balas = pygame.sprite.Group()
todos = pygame.sprite.Group()
reloj = pygame.time.Clock()

class Bala(pygame.sprite.Sprite):
    """docstring for Bala."""
    def __init__(self, matrix):
        pygame.sprite.Sprite.__init__(self)
        self.f = matrix
        self.image = self.f[4][0]
        self.rect = self.image.get_rect()

    def update(self):
        self.image = self.f[4][1]
        self.rect.x += 15


class Jugador(pygame.sprite.Sprite):
    """docstring for Jugador."""
    def __init__(self, matrix):
        pygame.sprite.Sprite.__init__(self)
        self.f = matrix
        self.image = self.f[1][0]
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 130
        self.index = 0
        self.action = 0
        self.direction = 0

    def update(self):
        if self.action == 0:
            self.image = self.f[1][self.index]
            self.index += 1
            if self.index >= 4:
                self.index = 0
        elif self.action == 1:
            self.image = self.f[7][self.index]
            self.index += 1
            if self.index >= 5:
                self.index = 0
                self.action = 0
        elif self.action == 2:
            self.image = self.f[2][self.index]
            self.index+=1
            if self.index >= 3:
                self.index=0
                self.action=0
        elif self.action == 3:
            self.image = self.f[0][self.index]
            self.index+=1
            if self.index >= 3:
                self.index=0
                self.action=0
                bala = Bala(matrix)
                bala.rect.x = self.rect.x + 20
                bala.rect.y = self.rect.y
                balas.add(bala)
                todos.add(bala)

        elif self.action == 4:
            self.image = self.f[8][self.index]
            self.index+=1
            #reloj.tick(50)
            for u in range(5):
                self.rect.y-=u
            if self.index >= 6:
                self.index=0
                self.action=0
                self.rect.y=130

        elif self.action == 5:
            self.image = self.f[9][self.index]
            self.index+=1
            if self.index >=1:
                self.index=0
                self.action=0
        elif self.action == 6:
            self.image = self.f[6][self.index]
            self.index+=1
            if self.index >=4:
                self.index=0
                self.action=0
        if self.action == 0 and self.direction == 1:
            self.image = self.f[3][self.index]
            self.index += 1
            if self.rect.x <= (width / 2):
                    self.rect.x += 10
            if self.index >=4:
                self.index = 0
                self.action = 0
                self.direction = 0
        elif self.action == 0 and self.direction == 2:
            self.image = self.f[3][self.index]
            self.index += 1
            if self.rect.x > (width / 3):
                self.rect.x -= 10
            if self.index >= 4:
                self.index = 0
                self.action = 0
                self.direction = 0


if __name__ == '__main__':
    pygame.init()
    imageFondo= pygame.image.load('source/fondo.png')
    pantalla = pygame.display.set_mode(size);
    pantalla.blit(imageFondo, [0, 0])
    imageSprite = pygame.image.load('source/ken.png')
    cantidadX = 7
    cantidadY = 10
    imageWidth = imageSprite.get_rect()[2]
    imageHeight = imageSprite.get_rect()[3]
    corteX = imageWidth / cantidadX
    print corteX
    corteY = imageHeight / cantidadY
    pygame.display.flip()

    #Recorto los sprite
    for y in range(cantidadY):
        matrix.append([])
        for x in range(cantidadX):
            cuadro = imageSprite.subsurface(corteX * x, corteY * y, corteX, corteY)
            matrix[y].append(cuadro)

    done = False
    jugador = Jugador(matrix)
    jugadores.add(jugador)
    todos.add(jugador)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.action = 0
                    jugador.direction = 1
                    jugador.index = 0
                    if jugador.rect.x >= width / 2:
                        posfondox-=10
                        if posfondox <= -400:
                            posfondox += 10
                            jugador.rect.x +=10
                            if jugador.rect.x >= width-70:
                                jugador.rect.x = width-70

                elif event.key == pygame.K_LEFT:
                    jugador.action = 0
                    jugador.direction = 2
                    jugador.index = 0
                    if jugador.rect.x <= width / 2:
                        posfondox += 10
                        if posfondox >= 0:
                            posfondox-=10
                            jugador.rect.x-=10
                            if jugador.rect.x <=0:
                                jugador.rect.x=0

                elif event.key == pygame.K_p:
                    jugador.action = 1
                    jugador.index = 0
                    jugador.direction = 0

                elif event.key == pygame.K_o:
                    jugador.action = 2
                    jugador.index = 0
                    jugador.direction=0

                elif event.key == pygame.K_SPACE:
                    jugador.action = 3
                    jugador.index = 0
                    jugador.direction=0

                elif event.key == pygame.K_w:
                    jugador.action = 4
                    jugador.direction = 0
                    jugador.index = 0
                    jugador.rect.y=130

                elif event.key == pygame.K_s:
                    jugador.action = 5
                    jugador.direction = 0
                    jugador.index = 0

                elif event.key == pygame.K_l:
                    jugador.action = 6
                    jugador.direction = 0
                    jugador.index = 0
                #elif event.key == pygame.K_UP:


        pantalla = pygame.display.set_mode(size);
        pantalla.blit(imageFondo, [posfondox, posfondoy])
        todos.draw(pantalla)
        todos.update()
        pygame.display.flip()
        reloj.tick(11)
