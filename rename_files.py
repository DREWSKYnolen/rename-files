import os
import binascii
import re

def rename_files():
    #(1) get file names from a folder
    #Dynamically get location based on this file's location
    file_path = os.getcwd()


    
    #(2) for each file, rename filename

    #filename = 'f_019916'
   

    for filename in os.listdir(file_path):
        with open(filename, 'rb') as f:
            content = re.search(b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x02\x00\x00\x01', f.read())
            if content is not "None":
                os.rename(filename,filename + ".jpg")
    
    

rename_files()
