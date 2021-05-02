import pygame
import random

azul = (50, 100, 213)
vermelho = (219, 31, 31)
verde = (0, 255, 0)

tela_width = 400  #largura da tela
tela_height = 400  #altura da tela

dis = pygame.display.set_mode((tela_width, tela_height))

# Posições iniciais da cobra na tela
position_x = 200
position_y = 100
d = 10
lista_cobra = [[position_x, position_y]]
dx = 0
dy = 0

#A posição inicial da comida é gerada randomicamente
x_comida = round(random.randrange(0, 400 - d) / 20) * 20
y_comida = round(random.randrange(0, 400 - d) / 20) * 20

pygame.display.set_caption("---- Snake ----")
dis.fill(azul)   #Projeta a tela nas proporçoes e cor indicadas
clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
  dis.fill(azul)
  for unidade in lista_cobra:
    pygame.draw.rect(dis, vermelho, [unidade[0], unidade[1], d, d])

def mover_cobra(dx, dy, lista_cobra):   #A cobra, após o primeiro clique para iniciar, se movimenta sozinha e sua direção é comandada pelo usuário
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:    #Identifica a tecla/direção
      if event.key == pygame.K_LEFT:
        dx = -d
        dy = 0
      elif event.key == pygame.K_RIGHT:
        dx = d
        dy = 0
      elif event.key == pygame.K_UP:
        dx = 0
        dy = -d
      elif event.key == pygame.K_DOWN:
        dx = 0
        dy = d
  
  # A cada clique o quadrado é movido de acordo com sua quantidade
  # Por exemplo, ao se deslocar para uma direção, o espaço ocupado anteriormente pela ultima posição será atualizado e voltará a cor azul
  x_novo = lista_cobra[-1][0] + dx
  y_novo = lista_cobra[-1][1] + dy

  lista_cobra.append([x_novo, y_novo])  #Adiciona as novas posições de x e y
  del lista_cobra[0]  # deleta a ultima posição ao ser deslocado
  return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
  head = lista_cobra[-1]

  x_novo = head[0] + dx
  y_novo = head[1] + dy

  if (head[0] == x_comida) and (head[1] == y_comida):  #Se a posição inicial da cobra "head" passar pela posição ocupada pela comida
    lista_cobra.append([x_novo, y_novo])    #a lista de posições/o tamanho da cobra aumenta e uma nova posição é criada
    x_comida = round(random.randrange(0, 400 - d) / 20) * 20  #A posição da nova comida também é criada randomicamente
    y_comida = round(random.randrange(0, 400 - d) / 20) * 20
  pygame.draw.rect(dis, verde, [x_comida, y_comida, d, d])
  return x_comida, y_comida, lista_cobra

while True:  #Enquanto o jogo não estiver finalizado
  pygame.display.update()
  desenha_cobra(lista_cobra)
  dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
  x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)
  clock.tick(10)  #velocidade de movimentação