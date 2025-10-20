import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Моя первая игра")
clock = pygame.time.Clock()
x, y = 200, 150
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()