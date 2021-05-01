import pygame

azul = (50, 100, 213)

vermelho = (219, 31, 31)

tela_width = 400  #largura da tela
tela_height = 200  #altura da tela

dis = pygame.display.set_mode((tela_width, tela_height))

position_x = 200
position_y = 100
d = 10

lista_cobra = [[position_x, position_y]]

pygame.display.set_caption("---- Snake ----")

dis.fill(azul)
clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
  dis.fill(azul)
  for unidade in lista_cobra:
    pygame.draw.rect(dis, vermelho, [unidade[0], unidade[1], d, d])

def mover_cobra(lista_cobra):
  delta_x = 0
  delta_y = 0

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        delta_x = -d
        delta_y = 0
      elif event.key == pygame.K_RIGHT:
        delta_x = d
        delta_y = 0
      elif event.key == pygame.K_UP:
        delta_x = 0
        delta_y = -d
      elif event.key == pygame.K_DOWN:
        delta_x = 0
        delta_y = d

  x_novo = lista_cobra[-1][0] + delta_x
  y_novo = lista_cobra[-1][1] + delta_y

  lista_cobra.append([x_novo, y_novo])

  del lista_cobra[0]

  return lista_cobra

while True:
  pygame.display.update()
  desenha_cobra(lista_cobra)
  lista_cobra = mover_cobra(lista_cobra)
  clock.tick(1)