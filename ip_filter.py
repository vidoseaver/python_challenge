class IpFilter():
    
    @staticmethod
    def do_any_ips_with_query_data_exist(ip_list, query):
        attribute_name = query[1]
        query_value = query[2]
        for ip in ip_list:
            if hasattr(ip, attribute_name):
                attribute = getattr(ip, attribute_name)
                if attribute == query_value:
                    return True
                
    def return_all_ips_with_value(self, ip_list, query):
        attribute_name = query[1]
        query_value = query[2]
        return [ip.__dict__ for ip in ip_list if hasattr(ip, attribute_name) and getattr(ip, attribute_name) == query_value]

    def return_first_ip_with_matching_value_for_attribute(self, ip_list, query):
        attribute_name = query[1]
        query_value = query[2]
        return next((ip.__dict__ for ip in ip_list if hasattr(ip, attribute_name) and getattr(ip, attribute_name) == query_value), None)
