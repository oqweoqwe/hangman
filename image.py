import pygame

class Image:

	def __init__(self, name):
		self.image = pygame.image.load(f"./resources/{name}.png")

	def draw(self, window, position):
		window.blit(self.image, position)

	def get_width(self):
		return self.image.get_width()

	def get_height(self):
		return self.image.get_height()