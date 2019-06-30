from os import path
import json
from env_variable_getter import EnvVariableGetter
from geo_ip_service import GeoIpService
from ip_model import IpModel
from text_parser import TextParser


class IpPopulator():
    def __init__(self, file_path):
        self.file_path = file_path
        self.list_of_ip_objects = []
        self.dict_of_ip_objects = {}
        self.list_of_ip_geo_attributes = []
        self.populate_ips()
        
    
    def populate_ips(self):
        json_version_of_path = self.file_path.replace("txt", "json")
        if path.exists(json_version_of_path):
            self.populate_ips_from_json(file_path=json_version_of_path)
        else:
            self.populate_ips_from_text_file()
    
    def populate_ips_from_json(self, file_path):
        file_content = self.get_text_from_file(file_path=file_path)
        file_content_as_dict = json.loads(file_content)
        for ip, ip_data in file_content_as_dict.items():
            self.generate_and_store_ip_model(ip=ip, data=ip_data)

    def get_text_from_file(self, file_path):
        if path.exists(file_path):
            file = open(file_path, "r")
            return file.read()
        else:
            raise Exception(file_path + " is not a none file. Please try again")

    def populate_ips_from_text_file(self):

        # Loading the initial file
        file_content =  self.get_text_from_file(file_path=self.file_path)
    
        # Instantiating the text parser that grabs the ips
        text_parser = TextParser(raw_text=file_content)
        raw_ips = text_parser.list_of_ip_adresses_contained_in_raw_text()

        # Get env variables for the GeoIpService
        env_variable_getter = EnvVariableGetter()
        api_key = env_variable_getter.get_variable("api_key")
        api_url = env_variable_getter.get_variable("api_url")
        
        # Instantiate GeoIp service which is responsible for going out and getting ip geolocation
        geo_ip_service = GeoIpService(key=api_key, url=api_url)
        
        # Get the Geo Ip info using the geo_ip_service, generate ip_models from
        # the response date and store them in the list and the dict for further filtering
        for ip in raw_ips:
            geo_ip_resonse = geo_ip_service.get_geo_ip_info_for_ip(
                ip_address=ip, format="json")
            self.generate_and_store_ip_model(ip=ip, data=geo_ip_resonse.json())

    def generate_and_store_ip_model(self,ip, data):
        modeled_ip = IpModel()
        modeled_ip.set_geo_ip_data_to_attributes(
            data=data)
        self.list_of_ip_objects.append(modeled_ip)
        self.dict_of_ip_objects[ip] = modeled_ip
        self.add_attributes_to_list_of_geo_ip_attributes(modeled_ip=modeled_ip)
        print(modeled_ip.ip + " fetched, modeled and stored")

    def add_attributes_to_list_of_geo_ip_attributes(self, modeled_ip):
        ip_keys = [k for k in modeled_ip.data]
        comined_with_other_possible_keys = ip_keys + self.list_of_ip_geo_attributes
        self.list_of_ip_geo_attributes = list(
            set(comined_with_other_possible_keys))
