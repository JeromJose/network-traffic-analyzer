from scapy.all import sniff, IP

def analyze_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"[+] {src} -> {dst} | Protocol: {proto}")

        # Simple anomaly detection
        if proto not in [6, 17]:  # TCP = 6, UDP = 17
            print(f"[ALERT] Unusual protocol detected: {proto}")

print("🔍 Starting Network Traffic Analyzer...\n")

sniff(prn=analyze_packet, store=False)