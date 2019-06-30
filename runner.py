from text_parser import TextParser
from geo_ip_service import GeoIpService
from ip_model import IpModel
def main():
    ips_file = open("list_of_ips.txt", "r")
    text_from_file = ips_file.read()
    text_parser = TextParser(raw_text=text_from_file)
    raw_ips = text_parser.list_of_ip_adresses_contained_in_raw_text()
    
    geo_ip_service = GeoIpService()
    modeled_ips = []

    for ip in raw_ips:
        geo_ip_resonse = geo_ip_service.get_geo_ip_info_for_ip(ip)
        modeled_ip = IpModel(ip_address=ip, data=geo_ip_resonse.json())
        import pdb; pdb.set_trace()
if __name__ == '__main__':
    main()
