import os
import sys
from datetime import date, datetime, timedelta

from directories.create_main_directories_controller import CreateDownloadedFolders, CleanDownloadDirectories

FOLDER_STEP_NAME = 'raw'
DOCKER_MAIN_COMMAND = 'docker run -i --rm -v'
# DOCKER_MAIN_COMMAND = 'docker run --rm -it -v'
WEBSITE_ADDRESS = 'https://otodom.pl/'
UNNECESSARY_FILE_NAMES = ['index']

def get_first_date_of_month(year, month):
    first_date = datetime(year, month, 1)
    return first_date.strftime("%Y%m%d")


def get_last_date_of_month(year, month):
    if month == 12:
        last_date = datetime(year, month, 31)
    else:
        last_date = datetime(year, month + 1, 1) + timedelta(days=-1)

    return last_date.strftime("%Y%m%d")

def RunDockerCommand(docker_main_command,path_to_file, website_address ,first_day, last_day):
    'docker run --rm -it -v $PWD/websites:/websites hartator/wayback-machine-downloader http://example.com --from 20060716231334 --to 20100916231334 --concurrency 2'
    #os.system("docker pull hartator/wayback-machine-downloader")
    docker_command = f"{docker_main_command} {path_to_file}:/websites hartator/wayback-machine-downloader {website_address} --from {first_day} --to {last_day} --concurrency 2"
    print(docker_command)

    # docker_command = f"{docker_main_command} $PWD/websites:{path_to_file} hartator/wayback-machine-downloader {website_address} --from{first_day} --to{last_day} --concurrency 2"
    os.system(docker_command)

#####


user_input = sys.argv

# os.system("docker pull hartator/wayback-machine-downloader")

month_list = [3]

for month in month_list:
    year = 2015  # int(user_input[1])
    #month = 7  # int(user_input[2])

    first_day = get_first_date_of_month(year, month)
    last_day = get_last_date_of_month(year, month)

    path_to_raw_dir = CreateDownloadedFolders(FOLDER_STEP_NAME, year, month)


    #RunDockerCommand(DOCKER_MAIN_COMMAND, path_to_raw_dir, WEBSITE_ADDRESS, first_day, last_day)

    # docker_command1 = 'docker run --rm -it -v $PWD/websites:/websites hartator/wayback-machine-downloader http://example.com --from 20060716231334 --to 20100916231334 --concurrency 2'

    # print(path_to_raw_dir)
    CleanDownloadDirectories(path_to_raw_dir, WEBSITE_ADDRESS ,UNNECESSARY_FILE_NAMES)

#
#
# wayback_machine_downloader http://example.com --directory downloaded-backup/ --from 20060716231334 --to 20100916231334 --only my_directory --concurrency NUMBER
#
# wayback_machine_downloader http://example.com --only "/\.(gif|jpg|jpeg)$/i"
#
#
# docker run --rm -it -v $PWD/websites:/websites hartator/wayback-machine-downloader http://example.com --from 20060716231334 --to 20100916231334 --only my_directory --concurrency 2
