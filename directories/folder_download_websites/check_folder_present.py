import os, re

RAW_WEBSITES_FOLDER_NAME = 'test'
ROOT_DIR = os.path.dirname(os.path.abspath('real-estate-prices'))

ROOT_DIR1 = os.path.dirname(os.path.abspath("top_level_file.txt"))


def CheckFolderPresent(main_dir_path):

    directory = os.getcwd()
    extrac_main_dir = directory.split("\\real-estate-prices")
    print(extrac_main_dir[0])

if __name__ == '__main__':
    CheckFolderPresent()
