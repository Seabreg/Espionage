'''
Copyright (C) 2020 Josh Schiavone - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license, which unfortunately won't be
written for another century.

You should have received a copy of the MIT license with
this file. If not, visit : https://opensource.org/licenses/MIT
'''

import struct
import socket
import textwrap

import httpcap

from core.config import *

class HTTP(object):
    def __init__(self, raw_data):
        try:
            self.data = raw_data.decode('utf-8')
        except:
            self.data = raw_data

class Packet(object):

    def transform_ip_4_address(self, dest_src_address):
        return '.'.join(map(str, dest_src_address))

    def unpack_packet(self, bytes_string, packet_data, array_value):
        cfg = Config()
        return struct.unpack(
            str(bytes_string), packet_data[:int(array_value)]
        )

    def handle_ipv4_packet(self, packet_data):
        pk = Packet()
        cfg = Config()

        __v_header_length__ = packet_data[0]
        __v_version__ = __v_header_length__ >> cfg.__version_header_shifter_length__
        __header_len__ = (__v_header_length__ & 15) * cfg.__version_header_shifter_length__

        ttl, proto, src, target = pk.unpack_packet(cfg.ESPI_IPV4_BYTES_STR, packet_data, 20)

        return __v_version__, __header_len__, ttl, proto, pk.transform_ip_4_address(src), pk.transform_ip_4_address(target), packet_data[__header_len__:]

    def handle_icmp_packet(self, packet_data):
        cfg = Config()
        pk = Packet()

        icmp_checksum, icmp_type, icmp_code = pk.unpack_packet(cfg.ESPI_ICMP_BYTES_STR, packet_data, 4)
        return icmp_checksum, icmp_type, icmp_code, packet_data[4:]

    def handle_raw_http_packet(self, packet_data):
        cfg = Config()
        pk = Packet()

        esp = Espionage()
        esp.print_espionage_noprefix("\t\tRaw HTTP Packet: ")
        try:
            raw_http_byteorder = HTTP(packet_data)
            byteorder_information = str(raw_http_byteorder.data).split('\n')
            for order in byteorder_information:
                esp.print_espionage_noprefix('\t\t\t' + str(order))

        except:
            print(espionage_textwrapper('\t\t\t', packet_data))
    
    def process_http_packet(self, http_packet):
        if http_packet.haslayer(HTTPRequest):
            packet_url = http_packet[HTTPRequest].Host.decode() + http_packet(HTTPRequest).Path.decode()
            packet_ip_address = http_packet[IP].src
            # Fetch the HTTP request method (GET or POST)
            http_method = http_packet[HTTPRequest].Method.decode()
            print(f"[+] {packet_ip_address} Requested {packet_url} with {http_method}")

    def sniff_http_packet(self, interface):
        cfg = Config()
        esp = Espionage()
        pk = Packet()

        if Interface(interface).is_interface_up():
            sniff(filter="port 443", prn=pk.process_http_packet, iface=interface, store=True)
        else: sniff(filter="port 443", prn=pk.process_http_packet, store=True)

   





    

