import os


DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME = 'downloaded_websites'


def GetMainDirPath():
    directory = os.getcwd()
    extrac_main_dir = directory.split("\\real-estate-prices")

    return extrac_main_dir[0]


def CheckFolderPresent(main_dir_path, dir_name):

    extrac_main_dir = main_dir_path.split("\\real-estate-prices")
    dir_list = []
    for file in os.listdir(os.path.normpath(extrac_main_dir[0])):
        check_dir = os.path.isdir(extrac_main_dir[0] + '\\' + file)
        if check_dir is True:
            dir_list.append(file)

    if dir_name not in dir_list:
        os.mkdir(extrac_main_dir[0] + '\\' + dir_name)



def MaintainDownloadFolderController():
    main_dir_path = GetMainDirPath()

    CheckFolderPresent(main_dir_path, DOWNLOADED_WEBSITES_MAIN_FOLDER_NAME)


if __name__ == '__main__':
    MaintainDownloadFolderController()