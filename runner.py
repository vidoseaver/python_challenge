from text_parser import TextParser

def main():
    ips_file = open("list_of_ips.txt", "r")
    text_from_file = ips_file.read()
    text_parser = TextParser(raw_text=text_from_file)
    ips = text_parser.list_of_ip_adresses_contained_in_raw_text()

if __name__ == '__main__':
    main()
