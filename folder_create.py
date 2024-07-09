import os
def folder_frm_file(file_path):
    with open(file_path, 'r') as file:
        folder_names= file.read().split('\t') #read the file content
    for i in folder_names:
        os.makedirs(i)
file_path="F:\python learning\list_of_employee.txt"
folder_frm_file(file_path)

