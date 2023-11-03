import os
import fnmatch
import subprocess
import sys

print('\n', "... FILE MANAGER ...")

path = input("Enter Directory Path: ")

if not os.path.exists(path) or not os.path.isdir(path):
    raise NotADirectoryError(f'Directory {path} does not exist')

file_type = input("Enter file extension: ")
count = len(fnmatch.filter(os.listdir(path), f'*{file_type}*'))
count_all_files = len(os.listdir(path))
count_all_folders = len(next(os.walk(path))[1])
name = (fnmatch.filter(os.listdir(path), f'*{file_type}*'))

if count > 1:
    print(f'There are {count} files')
elif count == 1:
    print(f'There is {count} file')

else:
    raise FileExistsError('There are no files', f'with ({file_type}) extension')

print("Total Files: ", count_all_files)
print("Total Folders: ", count_all_folders)

print('\n')
for i, file in enumerate(name, start=1):
    print(f"{i}. {file}")

print('\n')

new_folder_ask = input("Do you want to create a new folder [y/n]: ")
if new_folder_ask == 'y':
    new_folder_name = input("Enter new folder name: ")
    folder_path = os.path.join(path, new_folder_name)
    os.mkdir(folder_path)
    print(f'Folder: ({new_folder_name}) successfully  created in the directory: ({path})')
    if os.path.exists(new_folder_name):
        raise IsADirectoryError(f'The folder: {new_folder_name}, already exists')
else:
    print("New folder will not be created")

print('\n')

new_file_ask = input("Do you want to create a new file [y/n]: ")
if new_file_ask == 'y':

    new_file_name = input("Enter new file name: ")
    with open(os.path.join(path, new_file_name), 'x') as nf:
        pass
    print(f'File: ({new_file_name}) successfully  created in the directory: ({path})')

    if os.path.exists(new_file_name):
        raise FileExistsError(f'The file: {new_file_name}, already exists')

else:
    print("New file will not be created")

print('\n')
file_ask = input("Would you like to open a file [y/n]: ")
if file_ask == 'y':
    try:
        for i, file in enumerate(name, start=1):
            print(f"{i}. {file}")
        choice = int(input('Enter the number of the file you want to open [0 to cancel]: '))
        if 1 <= choice <= len(name):
            selected_file = name[choice - 1]
            file_path = os.path.join(path, selected_file)
            if selected_file.endswith('.mp4'):
                subprocess.call(['vlc', file_path])
            else:
                subprocess.call(['gnome-text-editor', file_path])
        elif choice == 0:
            sys.exit(0)

        else:
            print("Invalid number. Please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    print("No file will be opened.")

restart = input("Do you want to restart? [y/n] : ")
if str(restart) == str('y'):
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else:
    print('\n', "Program will be closed...")
    sys.exit(0)
