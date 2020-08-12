import pygame
import  random
import math

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')

pygame.display.set_icon(icon)

# player
player_img = pygame.image.load('ship.png')
playerX = 336
playerY = 468
playerX_change = 0

# place image on screen
def player(x, y):
    screen.blit(player_img, (x, y))


# enemy

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enmy = 4

for i in range(num_of_enmy):

    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(10, 726))
    enemyY.append(10)
    enemyX_change.append(0.3)
    enemyY_change.append(80)

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Bullet
bullet_img = []
bulletX = []
bulletY = []
bulletY_change = []
#  ready - you cant see the bullet
#   fire - the bullet is moving
bullet_state = []
num_of_bullet = 6

for i in range(num_of_bullet):
    bullet_img.append(pygame.image.load('bullet.png'))
    bulletX.append(0)
    bulletY.append(468)
    bulletY_change.append(0.5)
    #  ready - you cant see the bullet
    #   fire - the bullet is moving
    bullet_state.append('ready')

def fire_bullet(x, y, i):
    #global bullet_state[i]
    bullet_state[i] = 'fire'
    screen.blit(bullet_img[i], (x + 48, y - 32))


def isCollusion(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 48:
        return True
    else: return False

#score
score = 0
font = pygame.font.Font('Notebook.ttf', 32)
def show_score():
    text = font.render("Score :"+ str(score), True, (0, 0, 255))
    screen.blit(text, (10, 10))

#Game Loop
running = True
while running:

    #RGB background
    screen.fill((255, 255, 0))

    k = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

        #if key is pressed check its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(num_of_bullet):
                if bullet_state[i] is 'ready':
                    bulletX[i] = playerX
                    fire_bullet(bulletX[i], bulletY[i], i)
                    k = True
                if k:
                    break


    playerX = playerX + playerX_change
    if playerX < 10: playerX = 10
    if playerX > 662: playerX = 662 
    player(playerX, playerY)


    for i in range(num_of_enmy):

        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i] < 10 or enemyX[i] > 726:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)

        # Game OVER
        if enemyY[i] > 450:
            over_font = pygame.font.Font('Notebook.ttf', 100)
            over = over_font.render("Game Over", True, (0, 0, 0))
            screen.blit(over, (50, 200))
            for j in range(num_of_enmy):
                enemyY[j] = 2000
            playerY = 2000
            for j in range(num_of_bullet):
                bulletY[j] = 2500

    for j in range(num_of_bullet):
        if bulletY[j] < 0:
            bulletY[j] = 468
            bullet_state[j] = 'ready'
        if bullet_state[j] is 'fire':
            fire_bullet(bulletX[j], bulletY[j], j)
            bulletY[j] -= bulletY_change[j]


    # collusion
    for i in range(num_of_enmy):
        for j in range(num_of_bullet):
            collusion = isCollusion(enemyX[i], enemyY[i], bulletX[j], bulletY[j])
            if collusion:
                bulletY[j] = 468
                bullet_state[j] = 'ready'
                score += 1
                enemyX[i] = random.randint(10, 726)
                enemyY[i] = 10

    show_score()
    pygame.display.update()

















