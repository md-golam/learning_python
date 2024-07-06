import os

def create_folders_from_file(file_path, target_directory):
    # Read the file content
    with open(file_path, 'r') as file:
        folder_names = file.read().strip().split(',')
    
    # Create the folders
    for folder_name in folder_names:
        folder_path = os.path.join(target_directory, folder_name.strip())
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder created: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

# Specify the path to the text file and the target directory
file_path = 'D:\ learning\ learningpython\ list_of_employee.txt'
target_directory = 'D:\ learning\ learningpython\ test1'

create_folders_from_file(file_path, target_directory)
