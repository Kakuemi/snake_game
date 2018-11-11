import pygame
import player
import food

class Game_Window(object):
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((400,400),0,32)
		self.clock = pygame.time.Clock()
		self.player = player.Snake(400,400)
		self.Food = food.Food()

		self.font = pygame.font.SysFont('Courier New',40)

	def game_over(self):
		running = True
		time = 0
		while running :
			time += self.clock.tick()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.KEYDOWN and time > 1500:
					running = False
			self.screen.fill((0,0,0))
			text = self.font.render('GAME OVER ',True,(255,0,0))
			self.screen.blit(text,(200-text.get_width()/2,200-text.get_height()))
			t2 = 'POINT : ' + str(self.player.point)
			text2 = self.font.render(t2,True,(255,0,0))
			self.screen.blit(text2,(200-text2.get_width()/2,200+text2.get_height()))
			
			pygame.display.update()
		self.player.is_dead = False
		self.clock.tick()
		self.player.restart()
		self.Food.restart()

	def run(self):
		while True :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
			self.screen.fill((0,0,0))

			dt = self.clock.tick()
			self.player.update(dt,self.screen)
			self.Food.update(dt,self.screen,self.player)

			if self.player.is_dead :
				self.game_over()
				self.player.point = 0

			point = self.font.render(str(self.player.point),True,(255,255,255))
			self.screen.blit(point,(0,0))
			pygame.display.update()


if __name__ == '__main__':
	app = Game_Window()
	app.run()

