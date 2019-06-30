This readme assumes you have python 3 installed on your machine with the path set and that you are familiar with virtual enviornments and have pip installed.

The basic premise of this program is to read in text files, parse out all of the ip addresses out of the file, perform a geolocation call on that ip address then store the returned object in memory so and be query able. 

It is geo location service agnostic. That is to say you should be able for plug and play different geo location api's as you wish. It accomplishes this my dynamically assigning the attributes returned by said api to an ip model. It then stores that model in memmory and provides a repl inferface to query the data. The query parameters are also dyanmically generated as the file is read in.

Due to the limits imposed by most of these api's purchased a month subscription for 150,000 calls. In order to save calls I've written in the functionality where the program will save the information to a json for the ips provided after the first run. This persists the geo-location data allows the program to be run much faster the second time, while avoiding making duplictive calls.

To program uses several third party libraries listed in the requirements.txt file.

The first order of business to run this program is first activate a virtual environment.

Then you'll want to install the requirements using pip. 
```pip install -r requirements.txt --upgrade``

Once pip is installed you can run the program via the runner file.

Your command will look something like this:
```python3 runner.py list_of_ips.txt```
The final argument is the file you want to be parsed for ips.

When that command is entered the program will grab that file path and generate an instance of the ip_populator. 


The ip populator is responsible for reading in the path, determinng if its been run against this file before and whether a json file exists for that path. And then generating and storing IpModel from either the json file for that path or the responses it gets from the GeoIpService.

Once this is done a a repl object is kicked on that allows you to query the data. The repl is relatively simple and uses a IpFilter class to query the data. You can return items with a specific attribute for a specific value.