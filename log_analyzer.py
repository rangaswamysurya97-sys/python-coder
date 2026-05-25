# Simple Log File Analyzer
# Python 3.13 Compatible

from collections import Counter

def analyze_log_file(file_path):
    try:
        # Open log file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Total lines
        total_lines = len(lines)

        # Count log levels
        error_count = 0
        warning_count = 0
        info_count = 0

        # Store IP addresses
        ip_addresses = []

        for line in lines:

            # Convert to uppercase for matching
            upper_line = line.upper()

            if "ERROR" in upper_line:
                error_count += 1

            if "WARNING" in upper_line:
                warning_count += 1

            if "INFO" in upper_line:
                info_count += 1

            # Extract possible IP addresses
            words = line.split()

            for word in words:
                if word.count(".") == 3:
                    ip_addresses.append(word)

        # Count repeated IPs
        ip_counter = Counter(ip_addresses)

        # Display results
        print("\n===== LOG FILE ANALYSIS REPORT =====\n")

        print(f"Total Log Entries : {total_lines}")
        print(f"INFO Messages     : {info_count}")
        print(f"WARNING Messages  : {warning_count}")
        print(f"ERROR Messages    : {error_count}")

        print("\n===== TOP IP ADDRESSES =====\n")

        for ip, count in ip_counter.most_common(5):
            print(f"{ip} --> {count} times")

    except FileNotFoundError:
        print("Error: Log file not found.")

    except Exception as e:
        print("Error:", e)

# Get log file path from user
log_file = input("Enter log file path: ")

# Run analyzer
analyze_log_file(log_file)
