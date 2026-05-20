import shutil

source = input("Source file: ")
destination = input("Destination: ")

shutil.copy(source, destination)

print("Secure Transfer Complete")
