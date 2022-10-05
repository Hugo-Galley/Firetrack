import os
import sqlite3
def recup():
    file_list=os.listdir("Song")
    f=len(file_list)
    print(f, "fichiers trouvés dans le dossier")

    connexion = sqlite3.connect("Data Base/donné_musique.db")

    curseur = connexion.cursor()

    curseur.executescript("""
    
        CREATE TABLE IF NOT EXISTS playlist(
        id_titre INTEGER PRIMARY KEY,
        titre TEXT,
        integer vote);
    
       """)
    i=0
    donnees_liste = []
    playlist = []
    for fichier in range(len(file_list)):
        print("musique :", fichier)
        i=i+1
        file_list[fichier] = 'Song/' + file_list[fichier]
        playlist.append(file_list[fichier])

    print(i, "fichiers préparés pour la base")

    curseur.executemany("INSERT INTO playlist (titre,vote) VALUES (?, ?)", donnees_liste)

    connexion.commit()


    connexion.close()
    return playlist
recup()
