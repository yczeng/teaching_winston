class Trooper:
	def __init__(self, image, target_pos, gravity):
		self.image = image
		self.target_pos = target_pos
		(x, y) = target_pos
		self.pos = (x, y)
		self.x_velocity = 0
		self.gravity = gravity
		self.rect = self.image.get_rect()


	def get_pos(self):
		return self.pos

	def update(self):
		self.x_velocity += self.gravity
		(x, y) = self.pos
		new_pos = x + self.x_velocity
		self.pos = (new_pos, y)


	def draw(self, target):
		target.blit(self.image, self.pos)
