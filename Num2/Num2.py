import os
import yaml
import re

with open('config.yaml', 'r') as f:
    my_dict = yaml.load(f, Loader=yaml.FullLoader)


def creat_dir(data, paths, root):
    folder = list(data.keys())[0]
    structure = data[folder]
    dir_name = os.path.join(root, folder)
    if structure:
        for i in structure:
            if isinstance(i, dict):
                creat_dir(i, paths, dir_name)
            else:
                filepath = os.path.join(dir_name, i)
                paths.append(filepath)
    else:
        paths.append(f'{dir_name}\\')
    return paths


for i in creat_dir(my_dict, list(), os.getcwd()):
    if not os.path.exists(os.path.dirname(i)):
        os.makedirs(os.path.dirname(i))
    with open(i, "w") as file:
        pass
