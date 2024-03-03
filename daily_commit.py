from git import Repo
from datetime import datetime
import os
import time

# Lokasi direktori repo Anda
repo_dir = "C:/Users/crimson_net/Documents/kodingan/python/git-automa"
repo = Repo(repo_dir)

file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

for i in range(4):
    # Membuat file dengan timestamp
    file_name = os.path.join(repo_dir, file_names[i])
    with open(file_name, 'w') as fp:
        fp.write(str(datetime.now()))

    # Menambahkan semua perubahan
    repo.git.add('--all')

    # Melakukan commit
    repo.index.commit("Daily commit " + str(i+1))

    # Melakukan push
    origin = repo.remote(name='origin')
    origin.push()

    # Tunggu selama 5 detik sebelum commit berikutnya
    time.sleep(5)
