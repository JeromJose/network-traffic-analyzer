# Network Traffic Analyzer

## Description
A Python-based tool to capture and analyze live network traffic using Scapy.

## Features
- Real-time packet capture
- Displays source and destination IPs
- Detects unusual protocols

## Technologies Used
- Python
- Scapy

## How to Run
```bash
pip install scapy
python traffic_analyzer.py

#Example Output

[+] 192.168.1.5 -> 142.250.183.14 | Protocol: TCP
[+] 192.168.1.5 -> 8.8.8.8 | Protocol: UDP