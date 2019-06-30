from pprint import pformat
from helper_methods import *


class IpModel():
    def __init__(self):
        self.data = {}

    def set_geo_ip_data_to_attributes(self, data):
            # Merge new data into stored data
            # could pose a risk if there were dupes of keys
            self.data.update(data)
            self.set_attributes_from_dict(data)

    def set_attributes_from_dict(self, data):
        for attribute_name, attribute_value in data.items():
            #  the json body that comes back has camel cased response attributes,
            #  to keep the class "Pythonic" I'm converting the attribute name to snake case
            attribute_name_as_snake_case = to_snake_case(attribute_name)
            setattr(self, attribute_name_as_snake_case, attribute_value)

    def __repr__(self):
        # prints the data of the object in console when called. useful for debugging
        return pformat(self.data)
