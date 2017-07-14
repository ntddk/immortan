#!/usr/bin/env python
#coding: utf-8

import urllib.request
import socket
import geoip2.database
import json

def main():
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

    amcharts_map_dict = {
        'type': 'map',
        'theme': 'dark',
        'projection': 'eckert5',

        'imagesSettings': {
            'rollOverColor': '#089282',
            'rollOverScale': 3,
            'selectedScale': 3,
            'selectedColor': '#089282',
            'color': '#13564e'
        },
        'areasSettings': {
            'unlistedAreasColor': '#15A892'
        },
        'dataProvider': {
            'map': 'worldLow',
            'images': []
        }
    }

    google_map_dict = {
        'Marker': []
    }

    with urllib.request.urlopen('http://mirror1.malwaredomains.com/files/immortal_domains.txt') as response:
        domains = response.readlines()

    for domain in domains:
        domain = domain.decode('utf-8').replace('\n', '')
        try:
            ip = socket.gethostbyname(domain)
            print(ip)
            record = reader.city(ip)
            amcharts_point = {
                'zoomlevel': 5,
                'scale': 0.5,
                'title': domain,
                'latitude': record.location.latitude,
                'longitude': record.location.longitude
            }
            google_point = {
                'lat': record.location.latitude,
                'lng': record.location.longitude,
                'content': domain
            }
            amcharts_map_dict['dataProvider']['images'].append(amcharts_point)
            google_map_dict['Marker'].append(google_point)
        except:
            pass
    
    amcharts_json = open('amcharts_map.json', 'w')
    google_json = open('google_map.json', 'w')
    json.dump(amcharts_map_dict, amcharts_json, indent = 4)
    json.dump(google_map_dict, google_json, indent = 4)

if __name__ == '__main__':
    main()

