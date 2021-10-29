import os

folders = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in folders:
    dir_path = os.path.join('my_project', i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
