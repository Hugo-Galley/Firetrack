import pygame

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



running = True
action = False
start = False
playlist = list()
playlist.append("Song/2055.mp3")
playlist.append("Song/All Star.mp3")
playlist.append("Song/Doja.mp3")
playlist.append("Song/Au DD.mp3")
playlist.append("Song/Diva.mp3")
playlist.append("Song/Blueberry Faygo .mp3")
playlist.append("Song/Gasolina.mp3")
playlist.append("Song/Goosebumps.mp3")
playlist.append("Song/La vie quon mène.mp3")
playlist.append("Song/LE ZEN ET LES SEINS.mp3")
playlist.append("Song/Lemonade.mp3")
playlist.append("Song/Love me.mp3")
playlist.append("Song/Macarena.mp3")
playlist.append("Song/Mood.mp3")
playlist.append("Song/Papiers.mp3")
playlist.append("Song/Parfum.mp3")
playlist.append("Song/Problèmes.mp3")
playlist.append("Song/Roxanne.mp3")
playlist.append("Song/Si j savais.mp3")
playlist.append("Song/Train de vie.mp3")
playlist.append("Song/Tricheur.mp3")


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
            elif next_button_rect.collidepoint(event.pos):
                if i < len(playlist)-1:
                    i+=1
                else:
                    i = 0
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                print(i)

            elif precedent_button_rect.collidepoint(event.pos):
                if i > 0:
                    i-=1
                else :
                    i = len(playlist)-1

                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                print(i)
            elif like_button_rect.collidepoint(event.pos):
                like+=1
                print(like)

            elif dislike_button_rect.collidepoint(event.pos):
                dislike+=1
                print(dislike)


        else :

            if not action and not start:
                for song in playlist:
                    i = 0
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    print("Loading song ...")
                    start = True
                    like = 0
                    dislike = 0
                print("Votre playlist contient : ", len(playlist), " morceaux")
