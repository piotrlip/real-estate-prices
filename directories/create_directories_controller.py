import os


DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME = 'downloaded_websites'
ELASTIC_SEARCH_DIR = 'elastic'
POSTGRES_DIR = 'postgres'


def GetMainDirPath():
    directory = os.getcwd()
    extrac_main_dir = directory.split("\\real-estate-prices")

    return extrac_main_dir[0]


def CheckFolderPresent(main_dir_path, dir_name):

    dir_list = []
    for file in os.listdir(os.path.normpath(main_dir_path)):
        check_dir = os.path.isdir(main_dir_path + '\\' + file)
        if check_dir is True:
            dir_list.append(file)

    if dir_name in dir_list:
        return True
    else:
        return False


def ListAllDirInFolder(main_dir_path):
    extrac_main_dir = main_dir_path.split("\\real-estate-prices")
    dir_list = []
    for file in os.listdir(os.path.normpath(extrac_main_dir[0])):
        check_dir = os.path.isdir(extrac_main_dir[0] + '\\' + file)
        if check_dir is True:
            dir_list.append(file)

    return dir_list

def CreateDir(dir_name, main_path):

    if dir_name == DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME:
        os.mkdir(main_path + '\\' + dir_name)
        os.mkdir(main_path + '\\' + dir_name + '\\raw')
        os.mkdir(main_path + '\\' + dir_name + '\\clean')

    elif dir_name == ELASTIC_SEARCH_DIR:
        os.mkdir(main_path + '\\' + dir_name)

    elif dir_name == POSTGRES_DIR:
        os.mkdir(main_path + '\\' + dir_name)


def MaintainDownloadFolderController():
    main_dir_path = GetMainDirPath()
    required_dirs = [DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME, ELASTIC_SEARCH_DIR, POSTGRES_DIR]

    for dir_name in required_dirs:
        if CheckFolderPresent(main_dir_path, dir_name) is False:
            CreateDir(dir_name, main_dir_path)


