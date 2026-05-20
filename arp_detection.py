from scapy.all import ARP, sniff

known_ips = {}

def detect(packet):

    if packet.haslayer(ARP):

        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in known_ips:

            if known_ips[ip] != mac:

                print(
                    "Possible ARP Spoof Detected"
                )

        else:

            known_ips[ip] = mac

sniff(filter="arp", prn=detect)
