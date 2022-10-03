import os
import shutil

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


#
# def ListAllDirInFolder(main_dir_path):
#     extrac_main_dir = main_dir_path.split("\\real-estate-prices")
#     dir_list = []
#     for file in os.listdir(os.path.normpath(extrac_main_dir[0])):
#         check_dir = os.path.isdir(extrac_main_dir[0] + '\\' + file)
#         if check_dir is True:
#             dir_list.append(file)
#
#     return dir_list


def CreateMainDirs(dir_name, main_path):
    if dir_name == DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME:
        os.mkdir(main_path + '\\' + dir_name)
        os.mkdir(main_path + '\\' + dir_name + '\\raw')
        os.mkdir(main_path + '\\' + dir_name + '\\clean')

    elif dir_name == ELASTIC_SEARCH_DIR:
        os.mkdir(main_path + '\\' + dir_name)

    elif dir_name == POSTGRES_DIR:
        os.mkdir(main_path + '\\' + dir_name)


def CreateNewDir(path):
    os.mkdir(path)
    print("Created directory: " + path)


def CreateDownloadedFolders(folder_name, year, month):
    main_dir_path = GetMainDirPath()

    str_year = str(year)
    str_month = str(month)
    # print(str_month, ',', str_year)

    if folder_name == 'raw':

        try:
            main_path_to_raw_dir = main_dir_path + '\\' + DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME + '\\raw'

            full_path_to_raw_dir = main_path_to_raw_dir + '\\' + str_year + str_month

            CreateNewDir(full_path_to_raw_dir)
            print(f"Directory Created: {full_path_to_raw_dir}")
            return full_path_to_raw_dir
        except FileExistsError:

            print(f"Directory Exits: {full_path_to_raw_dir}")
            return full_path_to_raw_dir

    elif folder_name == 'clean':

        try:
            main_path_to_clean_dir = main_dir_path + '\\' + DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME + '\\clean'
            full_path_to_raw_dir = main_path_to_clean_dir + '\\' + str_year + str_month

        except FileExistsError:
            print(f"Directory Exits {full_path_to_raw_dir}")


def CleanDownloadDirectories(path, website, unnecessary_file_names):

    print('CleanDownloadDirectories')
    dir_list = []
    clean_website_name = website.replace('https://', '').replace('/', '')
    #test = os.listdir(os.path.normpath(path + '\\' + clean_website_name))
    #print()
    for file in os.listdir(os.path.normpath(path + '\\' + clean_website_name)):
        #print(path + '\\' +  clean_website_name + '\\' + file)
        check_dir = os.path.isdir(path + '\\' +  clean_website_name + '\\' + file)
        if check_dir is True:
            dir_list.append(path + '\\' +  clean_website_name + '\\' + file)

    for dir in dir_list:
        # print('\n\n\n\n')
        # print(dir)
        # print(path + '\\' +  clean_website_name + '\\' + dir)
        shutil.rmtree( dir )
        # os.remove(path + '\\' + dir)

    for element in unnecessary_file_names:
        #print(path + '\\' + element)
        os.remove(path + '\\' +  clean_website_name + '\\' + element)
        #os.remove(path + '\\' + element)


def MaintainMainFoldersController():
    main_dir_path = GetMainDirPath()
    required_main_dirs = [DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME, ELASTIC_SEARCH_DIR, POSTGRES_DIR]

    for dir_name in required_main_dirs:
        if CheckFolderPresent(main_dir_path, dir_name) is False:
            CreateMainDirs(dir_name, main_dir_path)
