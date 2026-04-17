import pygame
import random
from player import Player

pygame.init()

my_font = pygame.font.SysFont("Roboto", 40, bold = True)

clock = pygame.time.Clock()
text_yeahlup_size = 10
lup_is_growing = False
score = 0
number_of_levels = 1

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Target game")

stage = "input" 
player_name = ""


running = True
# --- A CIKLUS ELŐTT (csak egyszer fut le) ---
player = Player(200, 200, 20, "yellow", "")
target = Player(300, 300, 40, "red", "")

running = True
while running:
    # --- 1. ESEMÉNYKEZELÉS (Csak egy legyen!) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if stage == "input":
            if event.type == pygame.TEXTINPUT:
                player_name += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                if event.key == pygame.K_RETURN and player_name != "":
                    player.name = player_name # Itt adjuk át a nevet
                    stage = "game"

    if stage == "game":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.pos[0] > 20:
            player.pos[0] -= 5
        if keys[pygame.K_RIGHT] and player.pos[0] < 1180:
            player.pos[0] += 5
        if keys[pygame.K_DOWN] and player.pos[1] < 580:
            player.pos[1] += 5
        if keys[pygame.K_UP] and player.pos[1] > 20:
            player.pos[1] -= 5

        # Ütközésvizsgálat is csak játék közben kell
        if (target.pos[0] - 40 <= player.pos[0] <= target.pos[0] + 40) and \
           (target.pos[1] - 40 <= player.pos[1] <= target.pos[1] + 40):
            score += 1        
            target.pos[0] = random.randint(40, 1160)
            target.pos[1] = random.randint(40, 560)
            if score % 10 == 0 and score != 0:
                number_of_levels += 1
                lup_is_growing = True

    # --- 3. RAJZOLÁS ---
    screen.fill((30, 30, 30))
    
    if stage == "input":
        prompt_img = my_font.render("Írd be a neved és nyomj ENTER-t:", True, (255, 200, 0))
        name_img = my_font.render(player_name, True, (255, 255, 255))
        screen.blit(prompt_img, (600 - prompt_img.get_width()//2, 250))
        screen.blit(name_img, (600 - name_img.get_width()//2, 320))
    
    elif stage == "game":
        player.draw(screen)
        target.draw(screen)
        
        # UI elemek (csak játék közben)
        title_img = my_font.render("CATCH IT!", True, (255, 200, 0))
        score_img = my_font.render(f"Score: {score}", True, (255, 200, 0))
        level_img = my_font.render(f"Level: {number_of_levels}", True, (255, 200, 0))
        name_display = my_font.render(f"Player: {player.name}", True, (255, 200, 0))

        screen.blit(title_img, (10, 10))  
        screen.blit(score_img, (10, 50)) 
        screen.blit(level_img, (10, 90))
        screen.blit(name_display, (1190 - name_display.get_width(), 10))

        # Animáció
        if lup_is_growing:
            text_yeahlup_size += 2
            text_yeah_font = pygame.font.SysFont("Roboto", int(text_yeahlup_size), bold=True)
            growing_text_yeah = text_yeah_font.render("LEVEL UP!", True, "green")
            text_rect = growing_text_yeah.get_rect(center=(600, 300)) 
            screen.blit(growing_text_yeah, text_rect)
            if text_yeahlup_size > 120:
                lup_is_growing = False
                text_yeahlup_size = 10
        

    pygame.display.flip()
    clock.tick(60)


    pygame.display.flip()
pygame.quit()