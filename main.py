import pygame
from settings import Settings as settings
from gamemanager import GameManager
from inputhandler import InputHandler
from renderer import Renderer

pygame.init()

class Main:

	WINDOW = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
	pygame.display.set_caption(settings.CAPTION)

	renderer = Renderer(WINDOW)
	gm = GameManager(renderer)
	ih = InputHandler()

	def main(window,ih,gm,renderer): # params are inputhandler, gamemanager, renderer
		run = True
		clock = pygame.time.Clock()

		gm.initialize_topics()

		# game loop
		while run:
			clock.tick(60)
			window.fill(settings.BLACK) # clear screen

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					ih.listen(event,gm)
			
			# render, update
			
			# main menu loop
			if not gm.game_running:
				renderer.render_main_menu()

			# ingame loop
			if gm.game_running:
				gm.update()
				game = gm.current_game
				renderer.render_hangman_stage(game, True)
				renderer.render_selected_letter(game.guessing)
				renderer.render_guessed_letters(game.guessed_letters)
				renderer.render_correct_letters(game)
				renderer.render_topic(game)

			pygame.display.update()

		pygame.quit()

	if __name__ == "__main__":
		main(WINDOW,ih,gm,renderer)