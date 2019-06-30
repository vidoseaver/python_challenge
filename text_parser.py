import re

class TextParser():
    def __init__(self, raw_text):
        self.raw_text = raw_text
    
    def list_of_ip_adresses_contained_in_raw_text(self):
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', self.raw_text)
