import os
import binascii
import re

def rename_files():
    #(1) get file names from a folder
    #Dynamically get location based on this file's location
    file_path = os.getcwd()


    
    #(2) for each file, rename filename

    for filename in os.listdir(file_path):
        print(filename)
        ext = ""
        with open(filename, 'rb') as f:
            content = re.search(b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x02\x00\x00\x01', f.read()[0:48])
            #if this is a jpg
            if content is not None:
                ext = ".jpg"
        with open(filename, 'rb') as f:
            content = re.search(b'\x89\x50\x4E\x47', f.read()[0:48])
            #if this is a png
            if content is not None:
                ext = ".png"
        with open(filename, 'rb') as f:
            content = re.search(b'\x47\x49\x46', f.read()[0:48])
            #if this is a gif
            if content is not None:
                ext = ".gif"
        with open(filename, 'rb') as f:
            content = re.search(b'\x69\x73\x6F\x6D', f.read()[0:48])
            #if this is an mp4
            if content is not None:
                ext = ".mp4"
        with open(filename, 'rb') as f:
            content = re.search(b'\x25\x50\x44\x46', f.read()[0:48])
            #if this is a PDF
            if content is not None:
                ext = ".pdf"
            
            f.close()
            print(ext)
            os.rename(filename,filename + ext)
                
    
    

rename_files()
