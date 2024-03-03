from git import Repo
from datetime import datetime
import os

# Lokasi direktori repo Anda
repo_dir = "C:/Users/crimson_net/Documents/kodingan/python/git-automa"
repo = Repo(repo_dir)

# Membuat file dengan timestamp
file_name = os.path.join(repo_dir, 'commit.txt')
with open(file_name, 'w') as fp:
    fp.write(str(datetime.now()))

# Menambahkan semua perubahan
repo.git.add('--all')

# Melakukan commit
repo.index.commit("Daily commit")

# Melakukan push
origin = repo.remote(name='origin')
origin.push()
