import sys, pygame, random
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w)), (int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 27, 225)

fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image,(80,80))
fish_rect = fish_image.get_rect()

fish_rect.center = (width // 2, height // 2)

fish_speed = pygame.math.Vector2(0,10)
rotation = random.randint(0,360)
fish_speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180 - rotation)

def move_fish():
    global fish_image
    fish_rect.move_ip(fish_speed)

    if fish_rect.left < 0 or fish_rect > screen_info.current_w:
        fish_speed[0] *= -1
        fish_image = pygame.transform.flip(fish_image, True, False)
        fish_rect.move_ip(speed[0], 0)

    if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
        fish_speed[1] *= -1
        fish_image = pygame.transform.flip(fish_image, False, True)
        fish_rect.move_ip(0,speed[0])

def main(): 
    while True:
        clock.tick(60)

        move_fish()
        screen.blit(fish_image, fish_rect)
        screen.fill(color)
        pygame.display.flip()

if __name__ == '__main__':
    main()



