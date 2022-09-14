import pygame
from settings import Settings as settings
from pygame import key

class InputHandler:

	def __init__(self):
		pass

	def listen(self,event,gm):
		key = pygame.key.name(event.key)
		# if main menu
		if not gm.game_running:

			# if space pressed: start new game
			if key == "space":
				gm.start_new_game()


		# if in game
		if gm.game_running:

			# if esc
			if key == "escape":
				gm.end_current_game()

			# if return
			if key == "return":
				if not gm.current_game.guessing == None:
					gm.current_game.guess_letter(gm.current_game.guessing)

			# if alphabetic and not longer than 1 eg "space"
			if key.isalpha() and len(key) == 1:
				gm.current_game.guessing = key