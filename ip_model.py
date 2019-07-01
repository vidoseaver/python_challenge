from pprint import pformat


class IpModel():

    def set_geo_ip_data_to_attributes(self, data):
            # Data can get overwritten and therefore not accurately reflect the model
            # would need to be changed if more data was being added to model at another time via
            self.set_attributes_from_dict(data)

    def set_attributes_from_dict(self, data):
        for attribute_name, attribute_value in data.items():            
            #  setting values to string type for easy comparison on filtering
            attribute_value_as_string = str(attribute_value)
            setattr(self, attribute_name,
                    attribute_value_as_string)

