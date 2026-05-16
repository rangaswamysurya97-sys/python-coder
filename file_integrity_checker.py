import hashlib
import os

def calculate_hash(file_path, algorithm="sha256"):
    try:
        # Create hash object
        hash_function = hashlib.new(algorithm)

        # Open file in binary mode
        with open(file_path, "rb") as file:
            # Read file in chunks
            while chunk := file.read(4096):
                hash_function.update(chunk)

        return hash_function.hexdigest()

    except FileNotFoundError:
        return "File not found."

    except Exception as error:
        return f"Error: {error}"


def verify_integrity(file_path, original_hash, algorithm="sha256"):
    current_hash = calculate_hash(file_path, algorithm)

    print("\n===== File Integrity Report =====\n")

    print("Original Hash : ", original_hash)
    print("Current Hash  : ", current_hash)

    if current_hash == original_hash:
        print("\n[SAFE] File integrity verified.")
    else:
        print("\n[WARNING] File has been modified!")


# Main Program
print("===== File Integrity Checker =====")

file_path = input("Enter file path: ")

# Check if file exists
if not os.path.exists(file_path):
    print("File does not exist.")
else:
    # Generate original hash
    original_hash = calculate_hash(file_path)

    print("\nGenerated SHA-256 Hash:")
    print(original_hash)

    input("\nPress Enter after modifying the file (or leave unchanged)...")

    # Verify integrity
    verify_integrity(file_path, original_hash)
