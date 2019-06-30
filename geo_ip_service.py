import requests

class GeoIpService():
    def __init__(self):
        self.url = "http://ip-api.com/json/"
    
    def get_geo_ip_info_for_ip(self, ip_address):
        url = self.url + ip_address
        response = requests.get(url=url)
        return response