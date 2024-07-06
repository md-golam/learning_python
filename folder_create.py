import os
def folder_frm_file(file_path,target_dir):
    with open(file_path, 'r') as file:
        folder_names= file.read().split(',') #read the file content
    for i in folder_names:
        os.makedirs(i)
file_path="D:\learning\learningpython\list_of_employee.txt"
target_dir="D:\learning\learningpython\test1"
folder_frm_file(file_path,target_dir)
