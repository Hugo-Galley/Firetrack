# Créé par Magnesium, le 17/10/2020 en Python 3.7

# Créé par MGJ (MohammedGrimeJ, le 17/10/2020 tard le soir en Python 3.4
import sqlite3
import os
import random

#importer fichiers depuis le dossiers
#def fn():       # 1.Get file names from directory
def recup():
    file_list=os.listdir("Song")
    f=len(file_list)
    print(f, "fichiers trouvés dans le dossier")

        #print (file_list)

     #2.To rename files
    #fn()

    #Connexion
    connexion = sqlite3.connect("Data Base/donné_musique.db")

    #Récupération d'un curseur
    curseur = connexion.cursor()

    #Activation clés étrangères
    #curseur.execute("PRAGMA foreign_keys = ON")

    #Création table joueur puis score si elles n'existent pas encore
    #Puis suppression des données dans joueurs (et dans scores aussi par cascade)
    #afin d'éviter les répétitions d'enregistrements avec des exécutions multiples
    curseur.executescript("""
    
        CREATE TABLE IF NOT EXISTS playlist(
        id_titre INTEGER PRIMARY KEY,
        titre TEXT,
        vote integer);
    
       """)
    i=0
    donnees_liste = []
    #Préparation des données
    for fichier in file_list:
        print("musique :", fichier)
        i=i+1
        j=random.randint(1,100)
        donnees_liste.append(fichier)

    print(i, "fichiers préparés pour la base")
    print (donnees_liste)


    #Insertion des données dans table joueur puis score
    curseur.executemany("INSERT INTO playlist (titre, vote) VALUES (?, ?)", donnees_liste)
    #curseur.executemany("INSERT INTO scores (fk_joueur, valeur) VALUES (?, ?)", donnees_score)

    #Validation des ajouts
    connexion.commit()

    #Affichage des données
    #for playlist in curseur.execute("SELECT titre FROM playlist order by vote"):
        #print("musique triée:", playlist)


    #Déconnexion
    connexion.close()

recup()