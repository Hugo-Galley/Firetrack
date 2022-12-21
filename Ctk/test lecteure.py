import database

playlist = database.DataBase.recup_song()

for fichier in range(len(playlist)):
    playlist[fichier].lstrip('../Song/')