import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Cars")

car_img = pygame.image.load('car.png')
carX = 10
carY = 10
carX_change = 0
carY_change = 0
theta = 0
angle = 0
speed = .5
v = 0
a = 0
dir = 'nullf'

def car(x,y):
    screen.blit(car_img, (x, y))

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dir = 'front'
                a = .0001
            if event.key == pygame.K_s:
                dir = 'back'
                a = .0001
            if event.key == pygame.K_d and dir is 'front': theta = -.1
            if event.key == pygame.K_d and dir is 'back': theta = .1
            if event.key == pygame.K_a and dir is 'front': theta = .1
            if event.key == pygame.K_a and dir is 'back': theta = -.1
            if event.key == pygame.K_d and dir is 'nullf' or dir is 'nullb': theta = -.1
            if event.key == pygame.K_a and dir is 'nullf' or dir is 'nullb': theta = .1


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                dir = 'nullf'
                a = -.0001
            if event.key == pygame.K_s:
                dir = 'nullb'
                a = -.0001
            if event.key == pygame.K_a or event.key == pygame.K_d: theta = 0


    angle = angle + theta
    if angle < 0: angle = 359
    if angle > 360: angle = 1
    rotated = pygame.transform.rotate(car_img, angle)


    v = v + a
    print(v)
    if v > speed: v = speed
    if v < 0: v = 0

    carX_change = abs(v * math.cos(math.pi / 180 * angle))
    carY_change = abs(v * math.sin(math.pi / 180 * angle))

    if dir is 'front' or dir is 'nullf':
        if angle >=0 and angle <= 90:
            carX = carX + carX_change
            carY = carY - carY_change
        elif angle >= 90 and angle <= 180:
            carX = carX - carX_change
            carY = carY - carY_change
        elif angle >= 180 and angle <= 270:
            carX = carX - carX_change
            carY = carY + carY_change
        elif angle >= 270 and angle <= 360:
            carX = carX + carX_change
            carY = carY + carY_change

    elif dir is 'back' or dir is 'nullb':
        if angle >= 0 and angle <= 90:
            carX = carX - carX_change
            carY = carY + carY_change
        elif angle >= 90 and angle <= 180:
            carX = carX + carX_change
            carY = carY + carY_change
        elif angle >= 180 and angle <= 270:
            carX = carX + carX_change
            carY = carY - carY_change
        elif angle >= 270 and angle <= 360:
            carX = carX - carX_change
            carY = carY - carY_change

    if carX < 10: carX = 10
    if carX > 852: carX = 852
    if carY < 10 : carY = 10
    if carY > 562: carY = 562

    screen.blit(rotated, (carX, carY))

    pygame.display.update()




















