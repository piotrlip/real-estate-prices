import os

from folder_download_websites.check_folder_present import CheckFolderPresent


RAW_WEBSITES_MAIN_FOLDER_NAME = 'raw_websites'


def GetMainDirPath():
    directory = os.getcwd()
    extrac_main_dir = directory.split("\\real-estate-prices")

    return extrac_main_dir[0]


MAIN_DIR_PATH = GetMainDirPath()

def MaintainDownloadFolderController():
    print('112 MaintainDownloadFolderController()')
    CheckFolderPresent()


if __name__ == '__main__':
    CheckFolderPresent()