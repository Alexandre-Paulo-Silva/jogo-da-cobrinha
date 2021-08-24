import pygame, sys, random # importando bibliotecas sys = sistema basico, random = elemento aleatorio
from pygame import surface #improtando pygame para supertice
from pygame import color  # importando a biblioteca 
from pygame.math import Vector2 #importanto a biblioteca math = matematica para o vetor2


class SKAKE:
    
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #posicionamento dos blocos da cobra
        self.direction = Vector2(1,0)
        self.new_block = False



    def draw_snake(self):

        
        for block in self.body: #percorrer o vetor
         x_pos = int(block.x * cell_size)
         y_pos = int(block.y * cell_size)
         block_rect = pygame.Rect(x_pos, y_pos,cell_size,cell_size)
         pygame.draw.rect(screen,(183,191,122), block_rect) #desenhando a cobra

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] #fanzendo uma copia do corpo da cobra 
            body_copy.insert(0,body_copy[0] + self.direction) #movendo a cobra para frente
            self.body = body_copy[:]
            self.new_block = False
        else:
        
            body_copy = self.body[:-1] #fanzendo uma copia do corpo da cobra 
            body_copy.insert(0,body_copy[0] + self.direction) #movendo a cobra para frente
            self.body = body_copy[:]
    
    def add_block(self): #mundando o bloco
        self.new_block = True
        

class FRUIT: #classe fruta
    def __init__(self): #criando funcao incial com o objeto self
        self.randomize() # para poder mover a fruta
    
    def draw_fruit(self): #criando funcao para desenhar a fruta
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size) ,cell_size,cell_size ) #passado a posicao da fruta com o tamanho
        #screen.blit(apple,fruit_rect) #posicionado a maça no vetor do retangulo
        pygame.draw.rect(screen, (126,166,114), fruit_rect) #desenhado o retangulo
    
    def randomize (self):
        self.x = random.randint(0,cell_number - 1) # eixo x forma aleatoria
        self.y = random.randint(0,cell_number - 1) # eixo y forma aleatoria
        self.pos = pygame.math.Vector2(self.x,self.y) #vetor bidimensonal
    


class MAIN():
    def __init__(self):
        self.snake = SKAKE() # instanciando a classe no objeto
        self.fruit = FRUIT() # instanciando a classe no objeto
     
    def update(self):
         self.snake.move_snake()  #movendo a cobra 
         self.ckeck_collision() # funcao colisao
         self.ckeck_fail()

    def draw_elements(self):
        self.fruit.draw_fruit() #chamado a funcao fruta
        self.snake.draw_snake() #chamado a funcao combra    
    
    def ckeck_collision(self): #vereficando colisao
        if self.fruit.pos == self.snake.body[0]: #Se a cabeca passar por cima maça some
           self.fruit.randomize() #modo randomico das frutas
           self.snake.add_block()
    
    def ckeck_fail(self): #vereficando a colisao com o cenario
        if not 0 <= self.snake.body[0].x < cell_number: # se passar do cenario 
            self.game_over()
        
        if not 0 <= self.snake.body[0].y < cell_number: # se passar do cenario 
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self): # funcao game over
        pygame.quit()
        sys.exit()


        


pygame.init() #inciando o pygame
pygame.display.set_caption('Jogo da Cobrinha') #alterado a barra de titulo 

#test_surface = pygame.Surface((100,200)) #criando superficie do game
#test_surface.fill(pygame.Color(0,0,255))
#test_rect = pygame.Rect(100,200,100,100) #retangulo de teste de colisao (x,y,w,h) 
#test_rect = test_surface.get_rect(topright=(200,250)) #alinhando o retangulo centro outro comando topright, center

cell_size = 34 #tamanho da celula 
cell_number = 20 #numero de celulas
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))  #criando a janela largura e altura
clock = pygame.time.Clock() #tempo do loop
#apple = pygame.image.load('graficos/apple.png').convert_alpha() #inseririndo a imagem da maçã

#fruit = FRUIT() #instaciando a class fruta
#snake = SKAKE() #instanciando a class cobra

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #criando o cornometro 150 milesimo de segundo

while True: # loop para nao feixa a janela 
    #desenhado todos os elementos do jogo

    for event in pygame.event.get(): #criando um event para feixar a tela 
        if event.type == pygame.QUIT: #se clicar no botao ele feixa a tela
            pygame.quit() # chamando a funçao sair 
            sys.exit() #funcao sys sao funcoes basicas do sistema
        if  event.type == SCREEN_UPDATE: 
           main_game.update()
        if event.type == pygame.KEYDOWN:# comando de movimento da cobra
            if event.key == pygame.K_UP: #para cima
               if main_game.snake.direction.y !=1 :
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT: #para direita
               if main_game.snake.direction.x !=1 :
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN: #para baixo
               if main_game.snake.direction.y !=1 :
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT: #para esquerda
               if main_game.snake.direction.x !=1 :
                main_game.snake.direction = Vector2(-1,0)
            
    ##screen.fill(pygame.Color('gold')) #colocado cor no elemento janela modo simple
    #test_rect.right +=1
    #pygame.draw.ellipse(screen,pygame.Color('red'), test_rect) #desenhando o retangulo da maçã ellipse redonda
    #screen.blit(test_surface,test_rect) #criado a superficie sobre a tela 

    screen.fill((175,215,80)) #colocado cor no elemento janela modo avançado
    main_game.draw_elements() #chamando a funcao main 
    pygame.display.update() #chamando a funcao do loop do display
    clock.tick(60) # limitado o numero de fps por segundo  