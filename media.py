import pygame
import os

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)

title_page_music = pygame.mixer.Sound("assets/media/title_page_music.mp3")
good_ending = pygame.mixer.Sound("assets/media/good_ending.mp3")
bad_ending = pygame.mixer.Sound("assets/media/bad_ending.mp3")