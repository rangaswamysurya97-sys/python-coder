import os
import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def analyze_file(file_path):
    print("\n--- Sandbox Analysis Report ---")

    if not os.path.exists(file_path):
        print("File not found!")
        return

    size = os.path.getsize(file_path)
    file_hash = calculate_hash(file_path)

    print(f"File Name : {os.path.basename(file_path)}")
    print(f"File Size : {size} bytes")
    print(f"SHA256    : {file_hash}")

    suspicious_extensions = [".exe", ".bat", ".vbs"]

    ext = os.path.splitext(file_path)[1]

    if ext.lower() in suspicious_extensions:
        print("⚠ Suspicious executable detected")
    else:
        print("✓ File looks safe")

file = input("Enter file path: ")
analyze_file(file)
