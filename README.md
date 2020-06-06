# Espionage - A Network Traffic Interceptor For Linux
<p align="center">
  <img src="https://github.com/josh0xA/Espionage/blob/master/imgs/espionage_logo.png?raw=true">
</p>

## About Espionage
Espionage is network packet sniffer that intercepts large amounts data being passed through an interface. The tool allows users to to run normal and verbose traffic analysis that shows a live feed of traffic, revealing packet direction, protocols, flags, etc. Espionage supports IPv4, TCP/UDP, ICMP, and HTTP. Scapy support is also available so users can run in-depth sniffs using the Scapy library. Espionage was written in Python 3.8 but it also supports version 3.6. This is the first version of the tool so please contact the developer if you want to help contribute and add more to Espionage.

## Installation
1: ```git clone https://www.github.com/josh0xA/Espionage.git```<br/>
2: ```cd Espionage```<br/>
3: ```sudo python3 -m pip install -r requirments.txt```<br/>
4: ```sudo python3 espionage.py --help```<br/>

## Usage
1. ```sudo python3 espionage.py --normal --iface wlan0 -f capture_output.pcap```<br/>
Command 1 will execute a clean packet sniff and save the output to the pcap file provided. Replace ``wlan0`` with whatever your network interface is.<br/>
2. ```sudo python3 espionage.py --verbose --iface wlan0 -f capture_output.pcap```<br/>
Command 2 will execute a more detailed (verbose) packet sniff and save the output to the pcap file provided.<br/>
3. ```sudo python3 espionage.py --normal --iface wlan0```<br/>
Command 3 will still execute a clean packet sniff however, it will not save the data to a pcap file. Saving the sniff is recommended. <br/>
4. ```sudo python3 espionage.py --verbose --httpraw --iface wlan0```<br/>
Command 4 wille execute a verbose packet sniff and will also show raw http/tcp packet data in bytes. <br/>

## Menu
```
usage: espionage.py [-h] [--version] [-n] [-v] [-hr] [-s] [-f FILENAME] [-i IFACE]

optional arguments:
  -h, --help            show this help message and exit
  --version             returns the packet sniffers version.
  -n, --normal          executes a cleaner interception, less sophisticated.
  -v, --verbose         (recommended) executes a more in-depth packet interception/sniff.
  -hr, --httpraw        displays raw packet data (byte order) recieved or sent on port 80.
  -s, --scapy           uses scapy to intercept data sent to urls.

(Recommended) arguments for data output (.pcap):
  -f FILENAME, --filename FILENAME
                        name of file to store the output (make extension '.pcap').

(Required) arguments required for execution:
  -i IFACE, --iface IFACE
                        specify network interface (ie. wlan0, eth0, wlan1, etc.)
```

## Discord Server
https://discord.gg/jtZeWek

## Ethical Notice
The developer of this program, Josh Schiavone, written the following code for educational and ethical purposes only. The data sniffed/intercepted is not to be used for malicous intent. Josh Schiavone is not responsible or liable for misuse of this penetration testing tool. May God bless you all.

### License
MIT License<br/>
Copyright (c) 2020 Josh Schiavone
