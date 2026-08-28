import pygame
from config import Animal

pygame.mixer.init()


def play_sound_video(name):
    if name in Animal.keys():#dict的key的查找，看看有没有这个“key”
        print(Animal[name]["sound_content"])
        sound = pygame.mixer.Sound(Animal[name]["sound_path"])
        sound.play()
        # pygame.time.wait(1500)
    else:
        print("sorry,find an unknown item")
        # pygame.time.wait(1500)


def play_sound_pic(name):
    if name in Animal.keys():#dict的key的查找，看看有没有这个“key”
        print(Animal[name]["sound_content"])
        sound = pygame.mixer.Sound(Animal[name]["sound_path"])
        sound.play()
        pygame.time.wait(1500)
    else:
        print("sorry,find an unknown item")
        pygame.time.wait(1500)