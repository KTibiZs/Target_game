import pygame


pygame.init()
clock = pygame.time.Clock()
player_pos = [200, 150]
target_pos = [400, 150]

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Target_game")

running = True
my_font = pygame.font.SysFont("Roboto", 40, bold = True)

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 20:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < 1180:
        player_pos[0] += 5
    circle_1 = pygame.draw.circle(screen, "yellow", player_pos, 20)
    circle_2 = pygame.draw.circle(screen, "yellow", target_pos, 40)
    if target_pos[0] - 40 <= player_pos[0] <= target_pos[0] + 40:
        circle_2 = pygame.draw.circle(screen, "green", target_pos, 40)
    else:
        circle_2 = pygame.draw.circle(screen, "red", target_pos, 40)
    clock.tick(60)

    text_image = my_font.render("Get in the circle!", True, (255, 200, 0))
    screen.blit(text_image,(10, 10))
    pygame.display.flip()
pygame.quit()