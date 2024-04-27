import os

class open_dire():

    sentence = "open the folder Contacts from disc c"  # the spoken voice converted into a sentence and passed in this variable

    def open_folder(sentence):
        # Disc name keywords
        disc_keywords = ["disc", "disk"]
        
        # Extracting disc name and folder name
        disc_name = None
        folder_name = None
        words = sentence.split()
        for i in range(len(words)):
            if words[i] in disc_keywords and i+1 < len(words):
                disc_name = words[i+1]
            elif words[i] == "folder" and i+1 < len(words):
                folder_name = words[i+1]
        return [disc_name,folder_name]


    def search_directory_in_disk(directory_path, target_directory):
        for root, dirs, files in os.walk(directory_path):
            if target_directory in dirs:
                target_directory_path = os.path.join(root, target_directory)
                print(f"The directory '{target_directory}' is found at '{target_directory_path}'.")
                os.startfile(target_directory_path)
                return True
        return False




    disk_path = open_folder(sentence)[0]+':/'  # Specify the disk path you want to traverse
    target_directory = open_folder(sentence)[1]   # Specify the directory name to search and open

    if os.path.isdir(disk_path):
        if not search_directory_in_disk(disk_path, target_directory):
            print(f"The directory '{target_directory}' is not found in the disk '{disk_path}'.")
    else:
        print(f"The disk path '{disk_path}' is not valid.")


