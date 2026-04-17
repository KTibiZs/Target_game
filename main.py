import pygame
import random


pygame.init()
clock = pygame.time.Clock()
player_pos = [200, 150]
target_pos = [400, 150]
score = 0

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
    if keys[pygame.K_LEFT] and player_pos[0] > 20 :
        player_pos[0] -= 5
    elif keys[pygame.K_RIGHT] and player_pos[0] < 1180:
        player_pos[0] += 5
    elif keys[pygame.K_DOWN] and player_pos[1] < 580:
        player_pos[1] += 5
    elif keys[pygame.K_UP] and player_pos[1] >20:
        player_pos[1] -= 5


    circle_1 = pygame.draw.circle(screen, "yellow", player_pos, 20)
    circle_2 = pygame.draw.circle(screen, "yellow", target_pos, 40)
    if (target_pos[0] - 40 <= player_pos[0] <= target_pos[0] + 40) and (target_pos[1] - 40 <= player_pos[1] <= target_pos[1] + 40):
        score += 1
        target_pos[0] = random.randint(40, 1160)
        target_pos[1] = random.randint(40, 560)
    else:
        circle_2 = pygame.draw.circle(screen, "red", target_pos, 40)
    clock.tick(60)

    text_image = my_font.render("Get in the circle!", True, (255, 200, 0))
    score_image = my_font.render(str(score), True, (255, 200,0))
    screen.blit(text_image,(10, 10))
    screen.blit(score_image, (10, 50))
    pygame.display.flip()
pygame.quit()