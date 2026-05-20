import os
import time

filename = input("Enter file name: ")

last_modified = os.path.getmtime(filename)

print("Monitoring file changes...")

while True:

    current_modified = os.path.getmtime(filename)

    if current_modified != last_modified:

        print("File Changed!")

        last_modified = current_modified

    time.sleep(2)
