import sys
from ip_populator import IpPopulator
from repl import REPL
from exporter import Exporter

def main():

    # Grab file_path argument from initial run
    file_path = sys.argv[1]

    #Instatiate repl that interacts with the user


    # Instantiate ip populator that generates all the ips
    ip_populator = IpPopulator(file_path=file_path)
    
    exporter = Exporter()
    json_file_path = file_path.replace("txt", "json")
    exporter.export_as_json(file_path=json_file_path,
                            modeled_ips_dict=ip_populator.dict_of_ip_objects)

    




    #iterate over the subsection of ip addresses for testing purposes

    
    # write json file of ips
    
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
