import pygame


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
    
    
    def player_input(self):
        pass


    def update(self):
        pass


class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
    

    def update(self):
        pass



pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('DIO runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/Battle_Tendency_Opening.mp3')
bg_music.set_volume(0.1)
bg_music.play(loops = -1)


while True:
    pygame.display.update()
	clock.tick(60)
