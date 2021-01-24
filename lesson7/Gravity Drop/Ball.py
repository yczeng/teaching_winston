class Ball:
    def __init__(self, img, target_posn, gravity):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)     # Start ball at top of its column
        self.y_velocity = 0    #    with zero initial velocity
        self.gravity = gravity

    def update(self):
        self.y_velocity += self.gravity       # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity  # Velocity moves the ball
        self.posn = (x, new_y_pos)       #   to this new position.              # Do nothing for the moment.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)