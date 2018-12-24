#!/usr/bin/python3
import os
import shutil

folder_dirname = input("Please input the path:\n(e.g. ~/[YOUR_DIRNAME])\n\n")

dir_names = os.listdir(os.path.expanduser(folder_dirname))

dir_names.remove(".DS_Store")

def mkdir(path):
    
    folder = os.path.exists(path)
    if not folder:                   
        os.makedirs(path)            
        print("---  Made New Dir  ---")
    else:
        print("---  Alredy Exsits  ---")

for dir_name in dir_names:
    
    dir_name_former = dir_name.split(" 2018-")[0]
    print(dir_name_former) 
    dir_name_latter = dir_name.split(" 2018-")[1]
    print(dir_name_latter)
    new_dir_name = "2018-" + dir_name_latter + " " + dir_name_former
    print(new_dir_name + "\n")

    dir_path = os.path.join(os.path.expanduser(folder_dirname), dir_name)
    new_dir_path = os.path.join(os.path.expanduser(folder_dirname), new_dir_name)
    #mkdir(os.path.expanduser(new_dir_path))
    shutil.copytree(dir_path, new_dir_path)



        
