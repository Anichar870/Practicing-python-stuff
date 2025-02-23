import os
folders = input("Please provide list of folder names: ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)
    
    except FileNotFoundError:
        print("Nai deh bro")
        break 
    
    print("listing files for the folder- " + folder)
    
    
    for file in files:
        print(file)