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
        # self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        # y_cord = self.pos.y + self.image.get_height() // 2
        self.pos = pygame.Vector2(screen.get_width() // 2, 0)
        self.rect = self.image.get_rect(center=self.pos)
        # rect1 = self.rect

    def update(self):
        self.rect.y += 1
        # if collide:
        #    enemy_sprite_group.remove()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        # rect2 = self.rect

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
            for each_bullet in bullet_group:
                for enemy in enemy_sprite_group:
                    collide = each_bullet.rect.colliderect(enemy.rect)
                    if collide:
                        enemy_sprite_group.remove(enemy)
                        bullet_group.remove(each_bullet)

    # fill the screen with a color to wipe away anything from last frame


    # pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    screen.fill("black")
    character.Draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and character.pos.y > 0:
        character.pos.y -= 300 * character.dt
    if keys[pygame.K_s] and character.pos.y < 720 - character.char.get_height():
        character.pos.y += 300 * character.dt
    if keys[pygame.K_a] and character.pos.x > 0:
        character.pos.x -= 300 * character.dt
    if keys[pygame.K_d] and character.pos.x < 1280- character.char.get_width():
        character.pos.x += 300 * character.dt
    # flip() the display to put your work on screen
    #pygame.draw.rect(screen, color, pygame.Rect(5,5,5,5), 2)
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    character.dt = clock.tick(60) / 1000
