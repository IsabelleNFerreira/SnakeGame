import pygame

azul = (50, 100, 213)

vermelho = (219, 31, 31)

tela_width = 400  #largura da tela
tela_height = 200  #altura da tela

dis = pygame.display.set_mode((tela_width, tela_height))

position_x = 200
position_y = 100
d = 10

pygame.display.set_caption("---- Snake ----")

dis.fill(azul)
clock = pygame.time.Clock()

def desenha_cobra():
  pygame.draw.rect(dis, vermelho, [position_x, position_y, d, d])

def mover_cobra(position_x, position_y):
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

  position_x = position_x + delta_x
  position_y = position_y + delta_y

  return position_x, position_y

while True:
  pygame.display.update()
  desenha_cobra()
  position_x, position_y = mover_cobra(position_x, position_y)
  clock.tick(1)