import time
import sys
from ip_filter import IpFilter

class REPL():
    def __init__(self):
        self.ip_filter = IpFilter()
        self.ip_populator = None
        self.response_map = {
            "exit":self.exit,
            "help":self.print_help,
            "parse_response_and_answer":self.parse_response_and_answer
        }
        self.queryable_options = None
    @staticmethod
    def greet():
        print("\n\n")
        print("Thank you for running the ip_geo_query_machine_thing ")
        print("Please hold while data is populated")
        print("Also, note you can ask for help by entering 'help' or exit by typeing 'exit'")
        time.sleep(5)
    
    def intro(self):
        print("\n\n")
        print("Whew! Sorry about that, you can now query my data. There are three arguments used for querying the data")
        time.sleep(5)
        print("the first can consist of one from the following list['all', 'any' or 'first']")
        print("\n\n")
        time.sleep(5)
        print("The second can consist of: " + str(self.queryable_options)) 
        print("\n\n")
        print("The last should consist of the value you want to look for in the second parameter")
        print("\n\n")
        time.sleep(5)
        print("Here I'll give you an example lets say you want to know if there") 
        print("are any ip's with the value Spain for country_name")
        print("\n")
        print("You would enter 'any country_name Spain'")
        print("\n")
        print("I would then return your answer of True Or False")
        print("\n\n")
        self.print_help()

    
    def print_help(self):
        
        print("Here is a key of to how to work this:")
        print("any: returns a True or False if any of the ")
        print("all: returns an array of ip's with the value for the specified attribute")
        print("first: returns an the first ip that matches the value entered to the specified attribute")
        print("\n")
        print("Next comes a space then you choose an attribute from this list "+ str(self.queryable_options))
        print("finally another space with the value you want to search for for that option")
        self.prompt()
    
    def prompt(self):
        user_input = input("So what do you want to do?\n")
        self.handle_response(user_input)

    def handle_response(self, user_input):
        if user_input == "help" or user_input == "exit":
            self.response_map[user_input]()
        else:
            self.response_map["parse_response_and_answer"](user_input)

    def exit(self):
        print("Thank you! Have nice day!")
        sys.exit()
    
    def parse_response_and_answer(self, user_input):
        split_user_input = user_input.split(" ")
        if len(split_user_input) < 3:
            print("Sorry there needs to be three commands")
            self.print_help()
        last_value = " ".join(split_user_input[2:])
        corrected_split_user_input = [
            split_user_input[0], split_user_input[1], last_value]
        self.validate_user_input(corrected_split_user_input)
        self.query_and_return_data(corrected_split_user_input)

    # with more time i would objectify the response messages and have
    # this pass those back, right now it builds a stack and thats not great. 
    # it could use a refactor to keep it flat.
    def validate_user_input(self, split_user_input):
        if split_user_input[0] not in ["any", "all", "first"]:
            print("Sorry first command: " + 
                  split_user_input[0] + " was not in ['any, 'all', 'first]")
            self.print_help()
        elif split_user_input[1] not in self.queryable_options:
            print("Sorry second command: " +
                  split_user_input[1] + " was not in " + str(self.queryable_options))
            self.print_help()
    
    def query_and_return_data(self, split_user_input):
        list_of_ips = self.ip_populator.list_of_ip_objects
        user_verb = split_user_input[0]
        attribute = split_user_input[1]
        value = split_user_input[2]


        if user_verb == "any":
            if self.ip_filter.do_any_ips_with_query_data_exist(ip_list=list_of_ips, query=split_user_input):
                print("True,  There are ips in with the attribute " +
                       attribute + "that have a value that matches" + value)
                print("\n")
                self.prompt()

            else:
                print("False,  There are no ips in with the attribute " +
                         attribute + "that have a value that matches " + value)
                print("\n")
                self.prompt()

        elif user_verb == "all":
            ips_with_with_query_value = self.ip_filter.return_all_ips_with_value(ip_list=list_of_ips, query=split_user_input)
            if ips_with_with_query_value:
                print("There are " + str(len(ips_with_with_query_value)) + "ips with the attribute " +
                     attribute + " that have a value that matches " + value) 
                print("They are: \n" + str(ips_with_with_query_value))
                print("\n")
                self.prompt()
            else:
                print("There are no ips with the attribute " +
                     attribute + " that have a value that matches " + value)
                print("\n")
                self.prompt()
        elif user_verb == "first":
            first_ip_with_attribute_matching_value = self.ip_filter.return_first_ip_with_matching_value_for_attribute(
                ip_list=list_of_ips, query=split_user_input)
            if first_ip_with_attribute_matching_value:
                print("The first ip with the attribute of " +  attribute + "and value of " + value )
                print("Is: " + str(first_ip_with_attribute_matching_value))
                print("\n")
                self.prompt()
            else:
                print("There is no ip with the attribute " +
                      attribute + " that have a value that matches " + value)
                print("\n")

                self.prompt()
