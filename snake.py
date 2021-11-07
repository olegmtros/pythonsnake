import pygame
from random import randrange

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (200,200)
pygame.init()
pygame.display.set_mode(WINDOW_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)


OBJECT_SIZE = 10
x = randrange(0, WINDOW_WIDTH-2, OBJECT_SIZE) 
y = randrange(0, WINDOW_HEIGHT-2, OBJECT_SIZE)
body_snake = [(x, y)]
length_snake = 1
dx, dy = 0, 0
fps = 10
traffic_dict = {"W": (0, -1), "S": (0,1), "A": (-1,0), "D": (1,0)}

apple = randrange(0, WINDOW_WIDTH, OBJECT_SIZE), randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)


while True:
# Условие закрытия программы
    screen.fill(pygame.Color('black'))
    for i, j in body_snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
#    if x < 0 or x > WINDOW_WIDTH or y < 0 or y > WINDOW_HEIGHT:
    if x < 0 : x = WINDOW_WIDTH
    if x > WINDOW_WIDTH : x = 0
    if y < 0 : y = WINDOW_HEIGHT
    if y > WINDOW_HEIGHT : y = 0

#        break
    if len(body_snake) != len(set(body_snake)):
        break
    
    key = pygame.key.get_pressed()
    x += dx * OBJECT_SIZE
    y += dy * OBJECT_SIZE
    body_snake.append((x, y))
    body_snake = body_snake[-length_snake:]
    if key[pygame.K_w] and (dx, dy) != traffic_dict["S"]:
        dx, dy = traffic_dict["W"]
    if key[pygame.K_s] and (dx, dy) != traffic_dict["W"]:
        dx, dy = traffic_dict["S"]
    if key[pygame.K_a] and (dx, dy) != traffic_dict["D"]:
        dx, dy = traffic_dict["A"]
    if key[pygame.K_d] and (dx, dy) != traffic_dict["A"]:
        dx, dy = traffic_dict["D"]
    
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, OBJECT_SIZE, OBJECT_SIZE)) 
    if body_snake[-1] == apple:
        apple = randrange(0, WINDOW_WIDTH, OBJECT_SIZE), randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
        length_snake += 1
#        fps += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(fps)
    

