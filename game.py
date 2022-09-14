from settings import Settings as settings
import time
import pygame

class Game:

	guessing = None
	game_over = False
	won = None

	def __init__(self, word, topic, gamemanager):
		self.word = word
		self.topic = topic
		self.letters_in_word = list(word)
		self.guessed_letters = []
		self.guessed_words = []
		self.wrong_guesses = 0
		self.guesses = 0
		self.gm = gamemanager

	def guess_letter(self,letter):
		# returns true if correct, false otherwise

		if letter in self.guessed_letters:
			# TODO letter already guessed
			self.wrong_guesses += 1
			self.guesses += 1
			return False
		
		if letter in self.letters_in_word:
			# TODO letter is in word
			self.guessed_letters.append(letter)
			self.guesses += 1
			return True

		# if letter hasn't been guessed and isn't right, remove a try, add to guessed_letters and return false
		self.guessed_letters.append(letter)
		self.wrong_guesses += 1
		self.guesses += 1

		return False

	def game_over(self, won): # param is bool: true if game is won, false otherwise
		self.game_over = True
		self.won = won
		if won:
			self.gm.get_renderer().render_win_screen(self)
			pygame.display.update()
			time.sleep(5)
			self.gm.end_current_game()
		else:
			self.gm.get_renderer().render_lose_screen(self)
			pygame.display.update()
			time.sleep(5)
			self.gm.end_current_game()

	def get_word(self):
		return self.word