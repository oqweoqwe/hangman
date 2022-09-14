import pygame
from settings import Settings as settings
from image import Image

class Renderer:

	def __init__(self, window):
		self.font = pygame.font.SysFont(settings.DEFAULT_FONT, 30)
		self.window = window

	def render_main_menu(self):
		surface = self.get_text_surface("PRESS SPACE TO PLAY")
		position = self.get_center_position(surface)
		self.render_text(surface, position)

	def render_win_screen(self, game):
		first_line_surface = self.get_text_surface("CONGRATULATIONS! YOU'VE WON")
		second_line_surface = self.get_text_surface(f"THE WORD WAS {game.get_word().upper()}. YOU GUESSED IT IN {game.guesses} GUESSES")

		first_line_pos = self.get_center_position(first_line_surface)
		second_line_pos = (settings.WIDTH / 2 - second_line_surface.get_width() / 2, settings.HEIGHT / 2 + second_line_surface.get_height() / 2)

		self.render_text(first_line_surface, first_line_pos)
		self.render_text(second_line_surface, second_line_pos)

	def render_lose_screen(self, game):
		first_line_surface = self.get_text_surface("YOU'VE LOST!")
		second_line_surface = self.get_text_surface(f"THE WORD WAS {game.get_word().upper()}")

		first_line_pos = self.get_center_position(first_line_surface)
		second_line_pos = (settings.WIDTH / 2 - second_line_surface.get_width() / 2, settings.HEIGHT / 2 + second_line_surface.get_height() / 2)

		self.render_text(first_line_surface, first_line_pos)
		self.render_text(second_line_surface, second_line_pos)

	def render_selected_letter(self, letter):
		surface = self.get_text_surface(letter)
		position = (settings.WIDTH / 2 - surface.get_width() / 2, settings.HEIGHT - surface.get_height() * 2)

		self.render_text(surface, position)

	def render_guessed_letters(self, guessed_letters):
		surface = self.get_text_surface(f'GUESSED LETTERS: {" ".join(guessed_letters)}')
		pos = (10, 10)

		self.render_text(surface, pos)

	def render_hangman_stage(self, game, box):
		image = self.get_hangman_image(game)
		if not image is None:
			position = (settings.WIDTH / 2 - image.get_width() / 2, settings.HEIGHT / 3)
			image.draw(self.window, position)
			if box:
				self.box(image, position)

	def box(self, image, position):
		x, y = position

		top_left = (x,y)
		top_right = (x + image.get_width(),y)
		bottom_left = (x, y + image.get_height())
		bottom_right = (x + image.get_width(),y + image.get_height())

		pygame.draw.line(self.window, settings.WHITE, top_left, top_right, 2)
		pygame.draw.line(self.window, settings.WHITE, bottom_left, bottom_right, 2)
		pygame.draw.line(self.window, settings.WHITE, top_left, bottom_left, 2)
		pygame.draw.line(self.window, settings.WHITE, top_right, bottom_right, 2)

	def render_correct_letters(self, game):
		length_of_word = len(game.get_word())
		length_of_lines = settings.WIDTH / 2 / (length_of_word * 2)

		for i in range(length_of_word):
			line_start_pos_x = (settings.WIDTH - 2 * length_of_lines * length_of_word) / 2 + 2 * i * length_of_lines + length_of_lines / 2
			line_start_pos_y = settings.HEIGHT * 2 / 3
			line_end_pos_x = (settings.WIDTH - 2 * length_of_lines * length_of_word) / 2 + length_of_lines + 2 * i * length_of_lines + length_of_lines / 2
			line_end_pos_y = settings.HEIGHT * 2 / 3

			if game.get_word()[i] in game.letters_in_word and game.get_word()[i] in game.guessed_letters:
				surface = self.get_text_surface(game.get_word()[i])

				letter_pos_x = line_start_pos_x + length_of_lines / 2 - surface.get_width() / 2
				letter_pos_y = line_start_pos_y - 45 # TODO avoid hard coding position values to allow implementation for resizing of window

				self.render_text(surface, (letter_pos_x, letter_pos_y))

			pygame.draw.line(self.window, settings.WHITE, (line_start_pos_x, line_start_pos_y), (line_end_pos_x, line_end_pos_y), 2)

	def render_topic(self, game):
		surface = self.get_text_surface(f"TOPIC: {game.topic.get_name().upper()}")
		position = (10, surface.get_height())

		self.render_text(surface, position)

	def get_hangman_image(self, game):
		match game.wrong_guesses:
			case 0:
				return Image("stage_zero")
			case 1:
				return Image("stage_one")
			case 2:
				return Image("stage_two")
			case 3:
				return Image("stage_three")
			case 4:
				return Image("stage_four")
			case 5:
				return Image("stage_five")
			case 6:
				return Image("stage_six")
			case 7:
				return Image("stage_seven")
			case 8:
				return Image("stage_eight")
			case 9:
				return Image("stage_nine")
		return None

	def get_text_surface(self, text, color=settings.WHITE):
		return self.font.render(text, True, color)

	def get_center_position(self, surface):
		center_x = settings.WIDTH / 2 - surface.get_width() / 2
		center_y = settings.HEIGHT / 2 - surface.get_height() / 2
		return (center_x, center_y)

	def render_text(self, surface, position):
		self.window.blit(surface, position)