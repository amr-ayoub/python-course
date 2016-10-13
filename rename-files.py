# renaming files names in a folder

import os

def rename_files():
    # get files names
    file_list = os.listdir(r"C:\Users\Amr\Google Drive\Work\Udacity\Python\Resources\prank")
    print(file_list)

    #change diretory
    saved_dir = os.getcwd()
    os.chdir(r"C:\Users\Amr\Google Drive\Work\Udacity\Python\Resources\prank")

    # rename files names
    for file_name in file_list:
        os.rename(file_name , file_name.translate(None,"0123456789"))


    #return to original directory
    os.chdir(saved_dir)

rename_files()
