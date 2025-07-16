import pygame

class Player:
    def __init__(self, x=400, y=500):
        # Car position on screen
        self.x = x
        self.y = y
        # Car speed (pixels per frame)
        self.speed = 0
        # Car direction (-1: left, 0: straight, 1: right)
        self.direction = 0
        # Car sprite
        self.image = pygame.Surface((40, 80))
        self.image.fill((255, 0, 0))

    def accelerate(self, amount=1):
        self.speed += amount
        self.speed = min(self.speed, 20)

    def brake(self, amount=1):
        self.speed -= amount
        self.speed = max(self.speed, 0)

    def steer(self, direction):
        # direction: -1 (left), 0 (straight), 1 (right)
        self.direction = direction

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.accelerate()
        if keys[pygame.K_DOWN]:
            self.brake()
        if keys[pygame.K_LEFT]:
            self.steer(-1)
        elif keys[pygame.K_RIGHT]:
            self.steer(1)
        else:
            self.steer(0)

    def update(self):
        # Update horizontal position based on direction
        self.x += self.direction * 5
        self.x = max(0, min(self.x, 760))  # Keep car within screen bounds
        # Update vertical position based on speed
        self.y -= self.speed
        self.y = max(0, min(self.y, 520))  # Keep car within screen bounds

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
