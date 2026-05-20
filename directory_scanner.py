import os

path = input("Enter folder path: ")

for root, dirs, files in os.walk(path):

    print("\nCurrent Folder:", root)

    for file in files:
        print("File:", file)
