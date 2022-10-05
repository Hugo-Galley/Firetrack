import pygame

import init_music
import  download_music

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Firetracker")
screen = pygame.display.set_mode((500, 300))

background = pygame.image.load("assets/background.jpg")

play_button = pygame.image.load("assets/play_button.png")
play_button_rect = play_button.get_rect()
play_button_rect.x = 200
play_button_rect.y = 110

pause_button = pygame.image.load("assets/pause_buton.png")
pause_button_rect = pause_button.get_rect()
pause_button_rect.x = 300
pause_button_rect.y = 110

next_button = pygame.image.load("assets/next_button.png")
next_button_rect = next_button.get_rect()
next_button_rect.x = 400
next_button_rect.y = 110

precedent_button = pygame.image.load('assets/precedent_button.png')
precedent_button_rect = precedent_button.get_rect()
precedent_button_rect.x = 100
precedent_button_rect.y = 110

like_button = pygame.image.load('assets/like.png')
like_button_rect = like_button.get_rect()
like_button_rect.x = 50
like_button_rect.y = 190

dislike_button = pygame.image.load('assets/dislike.png')
dislike_button_rect = dislike_button.get_rect()
dislike_button_rect.x = 450
dislike_button_rect.y = 200


artist = input("ajouter le nom de l'artiste (remplacer les espace par des _)")
music = input("ajouter le nom de la musique (remplacer les espace par des _)")
download_music.add_video(artist,music)

running = True
action = False
start = False
playlist = list()
for i in init_music.recup():
    playlist.append(i)

while running:

    screen.blit(background,(0,0))
    screen.blit(precedent_button,precedent_button_rect)
    screen.blit(play_button,play_button_rect)
    screen.blit(pause_button,pause_button_rect)
    screen.blit(next_button,next_button_rect)
    screen.blit(like_button,like_button_rect)
    screen.blit(dislike_button,dislike_button_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_rect.collidepoint(event.pos):
                pygame.mixer.music.unpause()
                action = False
                print("play")

            elif pause_button_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
                action = True
                print("pause")
            elif next_button_rect.collidepoint(event.pos) :
                if i < len(playlist)-1 :
                    i+=1
                else:
                    i = 0
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                pygame.mixer.music.queue(playlist[song - 1])
                print(playlist[i])

            elif precedent_button_rect.collidepoint(event.pos):
                if i > 0:
                    i-=1
                else :
                    i = len(playlist)-1

                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                pygame.mixer.music.queue(playlist[song - 1])
                print(playlist[i])
            elif like_button_rect.collidepoint(event.pos):
                like+=1
                print(like)

            elif dislike_button_rect.collidepoint(event.pos):
                dislike+=1
                print(dislike)

            elif input_box.collidepoint(event.pos):

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RETURN:
                        print(texte)
                        texte = ''
                    elif event.key == pygame.K_BACKSPACE:
                        texte = texte[:-1]
                    else :
                        texte += event.unicode

                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                print(playlist[i])


        else :

            if not action and not start:
                for song in range(len(playlist)):
                    i = 0
                    pygame.mixer.music.load(playlist[song])
                    pygame.mixer.music.play()
                    pygame.mixer.music.queue(playlist[song - 1])
                    print("Loading song ...")
                    start = True
                    like = 0
                    dislike = 0
                print("Votre playlist contient : ", len(playlist), " morceaux")
