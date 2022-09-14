import random
from words import *
from game import Game
from image import Image
from settings import Settings as settings
from topic import Topic

class GameManager:

	def __init__(self,renderer):
		self.renderer = renderer
		self.topics = []

	current_game = None
	game_running = False

	def start_new_game(self):
		topic = self.select_topic()
		word = self.select_word(topic)
		self.current_game = Game(word, topic, self)
		self.game_running = True

	def initialize_topics(self):
		# init topic objects according to words file

		for i,topic in enumerate(TOPICS):
			topic = Topic()
			topic.set_name(TOPICS[i][0]) # first item in topic is name
			topic.set_words(TOPICS[i][1:]) # first item is name, so 1: is the words
			self.topics.append(topic)

	def select_topic(self):
		return self.topics[random.randrange(0, len(self.topics), 1)]

	def select_word(self, topic):
		return topic.get_words()[random.randrange(0, len(topic.get_words()), 1)]

	def update(self):
		# if no more tries left
		if self.current_game.wrong_guesses == settings.MAX_GUESSES:
			self.current_game.game_over(False)

		# if all letters are put in
		for letter in self.current_game.letters_in_word:
			if letter not in self.current_game.guessed_letters:
				return
		self.current_game.game_over(True)


	def end_current_game(self):
		current_game = None
		self.game_running = False

	def get_renderer(self):
		return self.renderer