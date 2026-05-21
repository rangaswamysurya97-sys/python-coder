from scapy.all import sniff

def analyze(packet):

    print(packet.summary())

sniff(count=10, prn=analyze)
