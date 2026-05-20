from scapy.all import ARP, sniff

known_devices = {}

def detect(packet):

    if packet.haslayer(ARP):

        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in known_devices:

            if known_devices[ip] != mac:

                print(
                    "Possible ARP Spoof:",
                    ip
                )

        else:

            known_devices[ip] = mac

sniff(filter="arp", prn=detect)
