import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
dt = 0 
player_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
nave = pygame.image.load('nave.png').convert()
nave = pygame.transform.scale(nave, (50,50))

while running:

    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 *dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 *dt
    if keys[pygame.K_d]:
        player_pos.x += 300 *dt

    nave_rect = nave.get_rect() 
    nave_rect.center = player_pos

    if nave_rect.left <0:
        nave_rect.left = 0 
    if nave_rect.top <0:
        nave_rect.top = 0
    if nave_rect.right > screen.get_width():
        nave_rect.right = screen.get_width()  
    if nave_rect.bottom > screen.get_height():
        nave_rect.bottom = screen.get_height()  

    player_pos = pygame.Vector2(nave_rect.center)
    nave_rect.center = player_pos
    screen.blit(nave, nave_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
