import pygame
import player

pygame.init()

alto_ventana=400
ancho_ventana=400

screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
clock = pygame.time.Clock()
player=player.Knight((0, alto_ventana/2))

game_over = False

while game_over == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over=True

	player.handle_event(event)
	screen.fill(pygame.Color('gray'))
	screen.blit(player.image, player.rect)
	pygame.display.flip()
	clock.tick(10)


pygame.quit ()