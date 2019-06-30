import requests

class GeoIpService():
    def __init__(self, key, url):
        self.api_key = key
        self.url = url
    
    def get_geo_ip_info_for_ip(self, ip_address, format):
        url = self.url.replace("{ip}", ip_address).replace("{format}", format).replace("{api_key}", self.api_key)
        response = requests.get(url=url)
        return response
