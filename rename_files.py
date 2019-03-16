import os

def rename_files():
    #(1) get file names from a folder
    #Dynamically get location based on this file's location
    file_path = os.getcwd()


    
    #(2) for each file, rename filename
    #header of file with 4A464946 is JFIF in ascii (which is a jpg/png file)



    # translation_table = str.maketrans("0123456789", "          ", "0123456789")
    # for file_name in file_list:
    #     os.rename(file_name, file_name.translate(translation_table))
    # os.chdir(saved_path)

rename_files()
