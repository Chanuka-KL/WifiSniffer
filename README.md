
# Wi-Fi Network Sniffer

## Description
Wi-Fi Network Sniffer is a Python-based tool that captures and analyzes packets from Wi-Fi networks. It allows users to monitor network traffic, which can help in identifying vulnerabilities and conducting security assessments.

## Features
- Captures Wi-Fi packets in real-time.
- Displays packet summaries for analysis.
- User-friendly interface for entering the network interface to sniff.

## Requirements
- Python 3.x
- Scapy library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Chanuka-KL/WI-FI-Network-Sniffer.git
   cd WI-FI-Network-Sniffer
   ```

2. Install the required library:
   ```bash
   pip install scapy
   ```

## Usage
1. Run the script with administrative privileges:
   ```bash
   sudo python WifiSniffer.py
   ```

2. Enter the Wi-Fi interface you want to sniff (e.g., `wlan0`).

3. Monitor the captured packets displayed in the terminal.

## Example Output
```
Enter the interface to sniff (e.g., wlan0): wlan0
Starting to sniff on wlan0...
Packet Captured: Dot11 / Radiotap
Packet Captured: Dot11 / Radiotap
...
```

## Important Note
- Sniffing network traffic without permission is illegal and unethical. Always ensure you have authorization to capture packets on the network.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- [Chanuka-KL](https://github.com/Chanuka-KL)

## Contact
For any questions or issues, feel free to reach out via GitHub or email.
```
