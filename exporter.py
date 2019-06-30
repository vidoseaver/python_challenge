import json

class Exporter():
    # def __init__(self):
    
    def export_as_csv(file_name, list_of_modeled_ips):
        #do a thing
        thing = 1

    @staticmethod
    def export_as_json(file_name, modeled_ips_dict):
        data = json.dumps(modeled_ips_dict, default=lambda x: x.__dict__)
        with open(file_name, "w") as outfile:
            outfile.write(data)
