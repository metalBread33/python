import os

def move_file(destination_folder):
    os.rename(
            os.path.join(og_folder, file.name),
            os.path.join(destination_folder, file.name))

og_folder = 'demos/fileCleanupDemo'
archived_folder = 'demos/fileCleanupDemo/CleanedUp/archived'
document_folder = 'demos/fileCleanupDemo/CleanedUp/docs'
picture_folder = 'demos/fileCleanupDemo/CleanedUp/pics'

if not os.path.exists(archived_folder):
    os.mkdir(archived_folder)

if not os.path.exists(document_folder):
    os.mkdir(document_folder)

if not os.path.exists(picture_folder):
    os.mkdir(picture_folder)

for file in os.scandir(og_folder):
    if os.path.splitext(file.name)[1] == '.txt':
        print("Moving file", file.name)
        move_file(document_folder)
        
    if os.path.splitext(file.name)[1] == '.zip':
        print("Moving file", file.name)
        move_file(archived_folder)

    if os.path.splitext(file.name)[1] == '.png':
        print("Moving file", file.name)
        move_file(picture_folder)