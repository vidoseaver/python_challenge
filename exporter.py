import json

class Exporter():
    
    @staticmethod 
    def export_as_csv(file_path, list_of_modeled_ips):
        #do a thing
        thing = 1

    @staticmethod
    def export_as_json(file_path, modeled_ips_dict):
        data = json.dumps(modeled_ips_dict, default=lambda x: x.__dict__)
        with open(file_path, "w") as outfile:
            outfile.write(data)
