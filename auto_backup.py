import os
import shutil
from datetime import datetime

# Source folder
SOURCE_FOLDER = r"C:\Users\ELCOT\Documents"

# Backup folder
BACKUP_FOLDER = r"C:\Backup"

# Folders to skip
SKIP_FOLDERS = [
    "My Music",
    "My Pictures",
    "My Videos"
]

def ignore_folders(directory, contents):
    ignored = []

    for item in contents:
        if item in SKIP_FOLDERS:
            ignored.append(item)

    return ignored

def create_backup():

    # Create backup folder
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Backup path
    backup_path = os.path.join(
        BACKUP_FOLDER,
        f"backup_{timestamp}"
    )

    try:
        # Copy files while ignoring protected folders
        shutil.copytree(
            SOURCE_FOLDER,
            backup_path,
            ignore=ignore_folders
        )

        print("\nBackup Created Successfully")
        print("Backup saved at:")
        print(backup_path)

    except Exception as e:
        print("Error:", e)

# Run program
create_backup()
