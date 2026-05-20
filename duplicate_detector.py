import hashlib
import os

folder = input("Enter folder path: ")

hashes = {}

for filename in os.listdir(folder):

    filepath = os.path.join(folder, filename)

    if os.path.isfile(filepath):

        with open(filepath, "rb") as file:

            file_hash = hashlib.md5(file.read()).hexdigest()

        if file_hash in hashes:
            print("Duplicate Found:")
            print(filepath)
            print(hashes[file_hash])

        else:
            hashes[file_hash] = filepath
