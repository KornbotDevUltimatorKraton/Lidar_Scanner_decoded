from bluetooth import* 
from pprint import pprint 
devices = discover_devices() 
print(devices) 
service = find_service(address="'"+devices[0]+"'") 
pprint(service)



