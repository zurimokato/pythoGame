import pygame

class Knight(pygame.sprite.Sprite):
	
	def __init__(self, position):
		self.sheet = pygame.image.load('knight.png')
		self.sheet.set_clip(pygame.Rect(0,0,30,46))
		self.image = self.sheet.subsurface(self.sheet.get_clip())
		self.rect = self.image.get_rect()
		self.rect.topleft = position
		self.frame = 0
		self.left_states={0:(0,0,30,45)}
		self.right_states={0:(0,0,30,45),1:(30,0,36,45),2:(66,0,36,45),
						   3:(102,0,38,45),4:(140,0,25,45),5:(165,0,25,45),
						   6:(190,0,30,45),7:(221,0,36,45),8:(259,0,33,45)}
		
		self.up_states={0:(0,0,30,45),1:(46,95,45,45),2:(92,95,35,45),
						3:(128,95,40,45),4:(170,95,34,45),5:(206,95,37,45)}
		self.run_states={0:(0,46,38,45),1:(39,46,39,45),2:(79,46,43,45),
						 3:(121,46,32,45),4:(154,46,38,45),5:(194,46,45,45),
						 6:(240,46,38,45),7:(278,46,37,45)}


	def get_frame(self, frame_set):
		self.frame +=1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]

	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.sheet.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect

	def handle_event(self, event):
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pygame.transform.flip(self.sheet, False, True)
				self.update('left')
			if event.key == pygame.K_RIGHT:
				self.update('right')
			if event.key == pygame.K_UP:
				self.update('up')
			if event.key == pygame.K_x:
				self.update('runing')

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.update('stand_left')
			if event.key == pygame.K_RIGHT:
				self.update('stand_right')
			if event.key == pygame.K_UP:
				self.update('stand_up')
			
					
			

	def update(self, direction):
		if direction == 'left':
			self.clip(self.left_states)
			self.rect.x -= 5
		if direction == 'right':
			self.clip(self.right_states)
			self.rect.x += 5
		if direction == 'up':
			self.clip(self.up_states)
			self.rect.x +=10
		if direction == 'runing':
			self.clip(self.run_states)
			self.rect.x +=10
		
		
		if direction == 'stand_left':
			self.clip(self.left_states[0])
		if direction == 'stand_right':
			self.clip(self.right_states[0])
		if direction == 'stand_up':		
			self.clip(self.up_states[0])
		
			

		self.image = self.sheet.subsurface(self.sheet.get_clip())