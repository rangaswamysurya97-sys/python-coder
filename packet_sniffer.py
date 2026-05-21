from scapy.all import sniff

def packet_callback(packet):

    print(packet.summary())

sniff(count=5, prn=packet_callback)
