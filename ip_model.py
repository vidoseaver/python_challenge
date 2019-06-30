from helper_methods import *

class IpModel():
    def __init__(self, ip_address):
        self.ip_address = ip_address # string of an ip adress

    def set_geo_ip_data_to_attributes(self, data):
        if data["status"] == "fail":
            self.set_as_failed_geo_ip(data)
        else: 
            set_attributes_for_success_full_geo_ip(data)
            import pdb; pdb.set_trace()

    def set_as_failed_geo_ip(self):
        setattr(self, "status", self.raw_data["status"])
        setattr(self, "message", self.raw_data["message"])
        
    def set_attributes_for_successfull_geo_ip(self, data):
        for attribute_name, attribute_value in data.items():
            #  the json body that comes back has camel cased response attributes,
            #  to keep the class "Pythonic" I'm converting the attribute name to snake case
            attribute_name_as_snake_case = to_snake_case(attribute_name)
            setattr(self, attribute_name_as_snake_case, attribute_value)

