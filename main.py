from os import walk
from shutil import move
import time
from schedule import every, run_pending

'''
STEPS:
======
1. Get files
2. Move files
3. PUT 1, 2 in a schedular
'''


def get_source_sink():
    source = "./dummy_data/source"
    sink = "./dummy_data/sink"
    # source = input("Enter Source Directory: ").strip()
    # sink = input("Enter Sink Directory: ").strip()
    return source, sink


def get_list_of_files(directory="."):
    try:
        for root, dirs, files in walk(directory):
            pass
        return files
    except:
        return False


def move_file(file_name="", source_dir="", dest_dir=""):
    try:
        source_file_path = source_dir + '/' + file_name
        dest_file_path = dest_dir + '/' + file_name
        move(source_file_path, dest_file_path)
        return True
    except:
        print("ERROR")
        return False


def operation():
    source, sink = get_source_sink()
    list_of_files = get_list_of_files(source)
    counter = 0
    if list_of_files:
        for file in list_of_files:
            if not move_file(file, source, sink):
                print("ERROR: File Cannot be moved!")
            else:
                counter += 1
        if counter:
            print("Successfully Moved {} files".format(counter))
        else:
            print("NO FILES MOVED")
    elif list_of_files == []:
        print("INFO: No New File Found!")
    else:
        print("ERROR: Source NOT FOUND!")


def operate():
    every(10).seconds.do(operation)
    while 1:
        try:
            run_pending()
        except:
            print("INTERNAL ERROR")


operate()
