import pygame
import os

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)

title_page_music = pygame.mixer.Sound("assets/media/title_page_music.mp3")
scene_4_music = pygame.mixer.Sound("assets/media/scene_4_music.mp3")
good_ending_music = pygame.mixer.Sound("assets/media/good_ending_music.mp3") # Doki Doki Literature Club! OST - My Feelings (composed by Dan Salvato)
bad_ending_music = pygame.mixer.Sound("assets/media/bad_ending_music.mp3") # Doki Doki Literature Club! OST - Sayo-nara (composed by Dan Salvato)

caught_sound = pygame.mixer.Sound("assets/media/caught_sound.wav") # Startled, gasping for breath 1 (created by AtoMediaDesign from Freesound)
kill_sound = pygame.mixer.Sound("assets/media/kill_sound.wav") # Slash1 (created by wesleyextreme_gamer)