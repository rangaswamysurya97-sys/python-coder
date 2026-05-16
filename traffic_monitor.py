import psutil
import time

def get_size(bytes_value):

    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024

def monitor_traffic():

    print("===== Network Traffic Monitor =====\n")

    old_data = psutil.net_io_counters()

    while True:

        time.sleep(1)

        new_data = psutil.net_io_counters()

        bytes_sent = new_data.bytes_sent - old_data.bytes_sent
        bytes_recv = new_data.bytes_recv - old_data.bytes_recv

        print(f"Upload Speed   : {get_size(bytes_sent)}/s")
        print(f"Download Speed : {get_size(bytes_recv)}/s")

        print("-" * 40)

        old_data = new_data

monitor_traffic()
