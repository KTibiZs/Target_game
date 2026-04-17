import pygame
import random


pygame.init()
clock = pygame.time.Clock()
player_pos = [200, 150]
target_pos = [400, 150]
text_yeahlup_size = 10
lup_is_growing = False
score = 0
number_of_levels = 1

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Target game")



running = True

while running:
    screen.fill((30, 30, 30))
    circle_1 = pygame.draw.circle(screen, "yellow", player_pos, 20)
    circle_2 = pygame.draw.circle(screen, "red", target_pos, 40)

    my_font = pygame.font.SysFont("Roboto", 40, bold = True)
    # 1. Sorok renderelése külön-külön
    title_img = my_font.render("Get in the circle!", True, (255, 200, 0))
    score_img = my_font.render(f"Score: {score}", True, (255, 200, 0))
    level_img = my_font.render(f"Level: {number_of_levels}", True, (255, 200, 0))

# 2. Kirajzolás egymás alá (Y koordináta növelésével)
    screen.blit(title_img, (10, 10))  # Első sor
    screen.blit(score_img, (10, 50))  # Második sor (40 pixellel lejjebb)
    screen.blit(level_img, (10, 90))  # Harmadik sor (még 40 pixellel lejjebb)

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




    if (target_pos[0] - 40 <= player_pos[0] <= target_pos[0] + 40) and (target_pos[1] - 40 <= player_pos[1] <= target_pos[1] + 40):
        score += 1        
        target_pos[0] = random.randint(40, 1160)
        target_pos[1] = random.randint(40, 560)

        if score % 10 == 0 and score != 0:
            number_of_levels += 1
            lup_is_growing = True
    
    if lup_is_growing:
        text_yeahlup_size += 2
        text_yeah_font = pygame.font.SysFont("Roboto", int(text_yeahlup_size), bold=True)
        growing_text_yeah = text_yeah_font.render("LEVEL UP!", True, "green")
        text_rect = growing_text_yeah.get_rect(center=(600, 300)) 
        screen.blit(growing_text_yeah, text_rect)
        if text_yeahlup_size > 120:
            lup_is_growing = False
            text_yeahlup_size = 10

    clock.tick(60)


    pygame.display.flip()
pygame.quit()