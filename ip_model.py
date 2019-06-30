class IpModel():
    def __init__(self, ip_address, data):
        self.ip_address = ip_address
        self.raw_data = data
        self.set_data_to_attributes()

    def set_data_to_attributes(self):
        if self.raw_data["status"] == "fail":
            self.set_as_failed_geo_ip()
        else: 
            import pdb; pdb.set_trace()

    def set_as_failed_geo_ip(self):
        setattr(self, "status", self.raw_data["status"])
        setattr(self, "message", self.raw_data["message"])
        
