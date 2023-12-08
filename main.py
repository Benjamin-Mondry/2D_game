import time

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
dead = False
COLOR = (255, 0, 0)
clock = pygame.time.Clock()
running = True


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dt = 0
        self.char = pygame.image.load('Hero_Standing.png').convert_alpha()
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def Draw(self):
        screen.blit(self.char, self.pos)

    def CreateBullet(self):
        center_x = self.pos.x + self.char.get_width() // 2  # gets centre of x
        center_y = self.pos.y + self.char.get_height() // 2  # gets centre of y
        return Bullet(center_x, center_y)


class Enemy_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill("white")
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        # y_cord = self.pos.y + self.image.get_height() // 2
        self.rect = self.image.get_rect(center=self.pos)
        #rect1 = self.rect
    def update(self):
        self.rect.y += 2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        #rect2 = self.rect
    def update(self):
        self.rect.y -= 5


character = Character()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(character.CreateBullet())
        if running:
            enemy_sprite_group.add(Enemy_Sprite())
            collide = bullet.rect.colliderect(enemy_sprite.rect)

            if collide:
                enemy_sprite_group.remove(Enemy_Sprite())

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    character.Draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character.pos.y -= 200 * character.dt
    if keys[pygame.K_s]:
        character.pos.y += 200 * character.dt
    if keys[pygame.K_a]:
        character.pos.x -= 200 * character.dt
    if keys[pygame.K_d]:
        character.pos.x += 200 * character.dt
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    character.dt = clock.tick(60) / 1000
