import sys
from os import path
from ip_populator import IpPopulator
from repl import REPL
from exporter import Exporter

def main():

    # Grab file_path argument from initial run
    file_path = sys.argv[1]

    #Instatiate repl that interacts with the user
    repl =  REPL()
    repl.greet()

    # Instantiate ip populator that generates all the ips
    ip_populator = IpPopulator(file_path=file_path)
    
    # Save file to json if it doesnt already exist
    json_file_path = file_path.replace("txt", "json")
    if path.exists(json_file_path) is False:
        exporter = Exporter()
        exporter.export_as_json(file_path=json_file_path, modeled_ips_dict=ip_populator.dict_of_ip_objects)

    # Set queryable_options for repl 
    repl.queryable_options = ip_populator.list_of_ip_geo_attributes
    repl.ip_populator = ip_populator

    # Get into query mode
    response = repl.intro()
    repl.handle_response(response)

    #iterate over the subsection of ip addresses for testing purposes

    
    # write json file of ips
    
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
