#!/usr/bin/env python
#coding: utf-8

import urllib.request
import socket
import geoip2.database

def main():
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

    with urllib.request.urlopen('http://mirror1.malwaredomains.com/files/immortal_domains.txt') as response:
        domains = response.readlines()

    for domain in domains:
        domain = domain.decode('utf-8').replace('\n', '')
        try:
            ip = socket.gethostbyname(domain)
            print(ip)
            record = reader.city(ip)
            print(record.country.name)
            print(record.city.name)
            print(record.location.latitude)
            print(record.location.longitude)
        except:
            pass

