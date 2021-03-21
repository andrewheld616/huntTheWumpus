import pygame

# defining variables to easily call 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hunt The Wumpus")

WHITE = (255, 255, 255)

FPS = 60

# function to set the colour of the window
def draw_window():
		WIN.fill((WHITE))
		pygame.display.update()

# function that controls most gameplay
def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		# caps FPS at definied value
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()

	pygame.quit()


if __name__ == "__main__":
	main()
