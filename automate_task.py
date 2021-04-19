import os
import fnmatch
import shutil
from datetime import *


def copy_files_to_another_folder(filename_pattern, sourcefolder=None, targetfolder=None, fromdate=None, todate=None):
    if fromdate and todate:
        delta = datetime.strptime(todate, '%Y-%m-%d') - datetime.strptime(fromdate, '%Y-%m-%d')
        for i in range(delta.days + 1):
            day = datetime.strftime(datetime.strptime(fromdate, '%Y-%m-%d') + timedelta(days=i), '%Y-%m-%d')
            for root, dirs, files in os.walk(sourcefolder):
                for file in files:
                    if fnmatch.fnmatch(os.path.basename(file), '*' + filename_pattern + '*') and fnmatch.fnmatch(
                            os.path.basename(file), '*' + str(day) + '*'):
                        shutil.copy(str(root).replace("\\", '/') + '/' + file, targetfolder)
    else:
        for root, dirs, files in os.walk(sourcefolder):
            for file in files:
                if fnmatch.fnmatch(os.path.basename(file), '*' + filename_pattern + '*'):
                    shutil.copy(str(root).replace("\\", '/') + '/' + file, targetfolder)


def move_files(from_folder, to_folder, filename_pattern):
    for items in os.listdir(from_folder):
        for criteria in filename_pattern:
            if fnmatch.fnmatch(os.path.basename(items), '*{}*'.format(criteria)):
                shutil.move(os.path.join(from_folder, os.path.basename(items)), to_folder)


def rename_file(from_folder, filename_pattern, replace_to_name, ):
    for root, dirs, files in os.walk(from_folder):
        for file in files:
            if fnmatch.fnmatch(os.path.basename(file), '*{}*'.format(filename_pattern)):
                filename = str(root).replace("\\", '/') + '/' + file
                try:
                    os.rename(filename, filename.replace(filename_pattern, replace_to_name))
                except Exception as e:
                    print(e)
