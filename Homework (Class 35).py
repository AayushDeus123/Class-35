import pygame

pygame.init()

screen_width = 500
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controlled Sprite")

white = (255, 255, 255)
red = (255, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(white, 20, 30, 100, 200)
sp2 = Sprite(red, 40, 60, 300, 150)

all_sprites_list.add(sp1)
all_sprites_list.add(sp2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sp1.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                sp1.speed_x = 5
            elif event.key == pygame.K_UP:
                sp1.speed_y = -5
            elif event.key == pygame.K_DOWN:
                sp1.speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sp1.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                sp1.speed_y = 0

    all_sprites_list.update()
    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()