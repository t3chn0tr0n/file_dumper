import os
import shutil

'''
STEPS:
======
1. Get files
2. Move files
3. PUT 1, 2 in a schedular
'''


def get_list_of_files(directory="."):
    try:
        for root, dirs, files in os.walk(directory):
            pass
        return files
    except:
        return False


def move_file(file_name="", source_dir="", dest_dir=""):
    try:
        source_file_path = source_dir + '/' + file_name
        dest_file_path = dest_dir + '/' + file_name
        shutil.move(source_file_path, dest_file_path)
        return True
    except:
        print("ERROR")
        return False


def get_source_sink():
    source = "D:/DOCUMENTS/Programs/Python/source"
    sink = "D:/DOCUMENTS/Programs/Python/sink"
    # source = input("Enter Source Directory: ").strip()
    # sink = input("Enter Sink Directory: ").strip()
    return source, sink


source, sink = get_source_sink()
list_of_files = get_list_of_files(source)
if list_of_files:
    for file in list_of_files:
        if not move_file(file, source, sink):
            print("ERROR: File Cannot be moved!")
elif list_of_files == []:
    print("INFO: No New File Found!")
else:
    print("ERROR: Source NOT FOUND!")
