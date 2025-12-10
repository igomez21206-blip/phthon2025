import pygame
import sys

# Inicialització
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()

# Carregar imatges (posar al mateix directori)
ball_img = pygame.image.load("bola.png")
paddle_img = pygame.image.load("barra.png")
brick_img = pygame.image.load("maó.png")

# Colors
BLACK = (0, 0, 0)

# Classes
class Paddle:
    def __init__(self):
        self.image = paddle_img
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT-30))
        self.speed = 7

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class Ball:
    def __init__(self):
        self.image = ball_img
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-50))
        self.speed = [5, -5]
        self.moving = False

    def update(self, paddle, bricks):
        if not self.moving:
            self.rect.centerx = paddle.rect.centerx
            return

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Col·lisions amb parets
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom >= HEIGHT:
            self.moving = False
            self.rect.center = (WIDTH//2, HEIGHT-50)

        # Col·lisions amb paddle
        if self.rect.colliderect(paddle.rect):
            self.speed[1] = -abs(self.speed[1])
            # Ajustar velocitat segons on toca la barra
            offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width/2)
            self.speed[0] = 5 * offset

        # Col·lisions amb maons
        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                # Detectar direcció del rebote
                if abs(self.rect.bottom - brick.rect.top) < 10 and self.speed[1] > 0:
                    self.speed[1] = -self.speed[1]
                elif abs(self.rect.top - brick.rect.bottom) < 10 and self.speed[1] < 0:
                    self.speed[1] = -self.speed[1]
                else:
                    self.speed[0] = -self.speed[0]
                break

    def draw(self):
        screen.blit(self.image, self.rect)

class Brick:
    def __init__(self, x, y):
        self.image = brick_img
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        screen.blit(self.image, self.rect)

# Crear objectes
paddle = Paddle()
ball = Ball()
bricks = [Brick(80*c+5, 40*r+5) for r in range(5) for c in range(10)]

# Bucle principal
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.moving = True

    paddle.move()
    ball.update(paddle, bricks)

    paddle.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()