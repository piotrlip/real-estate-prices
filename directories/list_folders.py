import os
from os import walk

path = 'C:\\Users\\lipinsp3\\Desktop\\Projekt'


def ListFoldersInDirectories(path):
    f = []
    new = 'test'

    files = [f for f in os.listdir(path) if os.path.isdir(f)]

    files1 = [f for f in os.listdir(path)]

    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break


if __name__ == '__main__':
    ListFoldersInDirectories(path)
