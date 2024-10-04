import scapy.all as scapy

# Function to capture packets
def sniff_packets(interface):
    scapy.sniff(iface=interface, prn=process_packet, store=False)

# Function to process captured packets
def process_packet(packet):
    if packet.haslayer(scapy.Dot11):
        print(f"Packet Captured: {packet.summary()}")

# Main function
def main():
    interface = input("Enter the interface to sniff (e.g., wlan0): ")
    print(f"Starting to sniff on {interface}...")
    sniff_packets(interface)

# Driver code
if __name__ == "__main__":
    main()