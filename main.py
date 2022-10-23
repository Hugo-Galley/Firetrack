import pygame
import  playlist_fonction
import tkinter as tk

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

add_button = pygame.image.load('assets/add.png')
add_button_rect = add_button.get_rect()
add_button_rect.x = 20
add_button_rect.y = 10

premium_button = pygame.image.load('assets/premium_icon.png')
premium_button_rect = premium_button.get_rect()
premium_button_rect.x = 430
premium_button_rect.y = 10



running = True
action = False
start = False
premium = False
playlist = list()
for i in playlist_fonction.recup():
    playlist.append(i)


while running:

    screen.blit(background,(0,0))
    screen.blit(precedent_button,precedent_button_rect)
    screen.blit(play_button,play_button_rect)
    screen.blit(pause_button,pause_button_rect)
    screen.blit(next_button,next_button_rect)
    screen.blit(like_button,like_button_rect)
    screen.blit(dislike_button,dislike_button_rect)
    screen.blit(add_button,add_button_rect)
    screen.blit(premium_button,premium_button_rect)
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
                if i == 5 and not premium:
                    win = tk.Tk()
                    win.geometry('200x100')
                    TEXTE = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                    label = tk.Label(win, text=TEXTE,
                                     wraplength=(100),
                                     justify=tk.CENTER)
                    label.pack()
                    win.mainloop()
                elif i < len(playlist)-1 :
                    i+=1
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                    print(playlist[i])

                else:
                    i = 0
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                    print(playlist[i])


            elif precedent_button_rect.collidepoint(event.pos):
                if i == 5 and not premium:
                    win = tk.Tk()
                    win.geometry('200x100')
                    TEXTE = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                    label = tk.Label(win, text=TEXTE,
                                     wraplength=(100),
                                     justify=tk.CENTER)
                    label.pack()
                    win.mainloop()
                elif i > 0:
                    i-=1
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                    print(playlist[i])
                else :
                    i = len(playlist[i])-1
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play()
                    print(playlist[i])

            elif like_button_rect.collidepoint(event.pos):
                playlist_fonction.add_vote(playlist[i],True)
                playlist = playlist_fonction.recup_vote_and_song()



            elif dislike_button_rect.collidepoint(event.pos):
                playlist_fonction.add_vote(playlist[i],False)
                playlist = playlist_fonction.recup_vote_and_song()


            elif add_button_rect.collidepoint(event.pos):
                win = tk.Tk()
                TEXTE = "Fonction en phase de test, bientôt disponible"
                label = tk.Label(win, text=TEXTE,
                                 wraplength=(100),
                                 justify=tk.CENTER)
                label.pack()
                win.mainloop()

                playlist_fonction.add_video(playlist_fonction.choix_artiste(), playlist_fonction.choix_music())



                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()

            elif premium_button_rect.collidepoint(event.pos):
                premium = True
                win = tk.Tk()
                win.geometry('200x100')
                TEXTE = "Merci d'avoir souscris à notre offre premium"
                label = tk.Label(win, text=TEXTE,
                                 wraplength=(70),
                                 justify=tk.CENTER)
                label.pack()
                win.mainloop()



        else :

            if not action and not start:
                for song in range(len(playlist)):
                    i = 0
                    pygame.mixer.music.load(playlist[song])
                    pygame.mixer.music.play()
                    print("Loading song ...")
                    start = True

                print("Votre playlist contient : ", len(playlist), " morceaux")