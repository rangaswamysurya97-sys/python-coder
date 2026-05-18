# Dictionary to store failed login attempts
failed_attempts = {}

# Maximum allowed failed attempts
MAX_ATTEMPTS = 3

def detect_brute_force(ip_address, success):
    
    # If login successful
    if success:
        print(f"[SUCCESS] Login successful from {ip_address}")

        # Reset failed attempts after success
        if ip_address in failed_attempts:
            failed_attempts[ip_address] = 0

    else:
        # Increase failed attempts
        if ip_address in failed_attempts:
            failed_attempts[ip_address] += 1
        else:
            failed_attempts[ip_address] = 1

        print(f"[FAILED] Login failed from {ip_address}")

        # Detect brute force attack
        if failed_attempts[ip_address] >= MAX_ATTEMPTS:
            print(f"[ALERT] Possible brute force attack detected from {ip_address}")

# Simulated login attempts
detect_brute_force("192.168.1.10", False)
detect_brute_force("192.168.1.10", False)
detect_brute_force("192.168.1.10", False)
detect_brute_force("192.168.1.20", False)
detect_brute_force("192.168.1.20", True)
