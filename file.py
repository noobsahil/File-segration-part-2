import os
import shutil

from_dir = "C:/Users/sahil/Downloads"
to_dir = "C:/Users/sahil/OneDrive/Desktop/Home"

allowed_exts = [".txt", ".doc", ".docx", ".pdf"]

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    file_ext = os.path.splitext(file_name)[1]
    
    if file_ext == "":
        continue
    
    if file_ext in allowed_exts:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files/" + file_ext[1:].upper()
        path3 = to_dir + "/" + "Document_Files/" + file_ext[1:].upper() + "/" + file_name
        
        if not os.path.exists(path2):
            os.makedirs(path2)
            print("Created directory:", path2)
        
        print("Moving file:", file_name)
        shutil.move(path1, path3)

print("All files have been moved to the appropriate destination folders.")
