import os
import sys

print('\n', "... FILE CLEANER ...")


check = input("Enter directory path: ")

print('\n')

if not os.path.exists(check) or not os.path.isdir(check):
    raise FileNotFoundError(f'Directory {check} does not exist')


empty_directories = []

for entry in os.scandir(check):
    if entry.is_dir() and not os.listdir(entry.path):
        empty_directories.append(entry.path)




if not empty_directories:
    print("No empty directories found.")



else:
    print("Empty directories:")
    for i, directory in enumerate(empty_directories, start=1):
        print(f"{i}. {directory}")


    check2 = input("Do you want to delete them all? [y/n] : ")
    if check2.lower() == 'y':
        for directory in empty_directories:
                os.rmdir(str(directory))
        print("Successfully Deleted!! ")
    else:
        print("Deletion Canceled")

    sys.exit(0)

try:
    choice = int(input("Enter the number of the directory you want to delete (0 to cancel): "))

    if 1 <= choice <= len(empty_directories):
        directory_to_delete = empty_directories[choice - 1]
        check3 = input(f"Are you sure you want to delete '{directory_to_delete}'? (y/n): ")
        if check3.lower() == "y":
            os.rmdir(directory_to_delete)
            print(f"'{directory_to_delete}' was successfully deleted.")
        else:
            print("Deletion canceled.")
    elif choice == 0:
        print("Deletion canceled.")
    else:
        print("Invalid choice. No directory will be deleted.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

restart = input("Do you want to restart? [y/n] : ")
if str(restart) == str('y'):
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else:
    print('\n', "Program will be closed...")
    sys.exit(0)