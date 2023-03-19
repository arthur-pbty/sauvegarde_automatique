import shutil
import time

source = r'C:\Users\Arthur\Desktop\1'       # chemin vers le dossier a sauvegarder
destination = r'C:\Users\Arthur\Desktop\2'  # chemin vers le dossier de destination

while True:
    backup_name = 'backup_' + time.strftime('%Y-%m-%d-%H-%M-%S')
    shutil.make_archive(destination + '/' + backup_name, 'zip', source)
    time.sleep(3600)  # sauvegarde toutes les heures
