#read_config_file.py

from configparser import ConfigParser
'''
obj = ConfigParser()

obj["user"] ={
    "name": "admin",
    "pass" : "admin123",
    "user" : "root"
}

obj["services"] = {
    "server": "google.com",
    "host": "google"
}

with open("demo.ini","w") as f:
    obj.write(f)
print("data saved successfully")
f.close()
'''
obj1 = ConfigParser()
obj1.read("demo.ini")

print("Sections=",obj1.sections())
print("user name=",obj1.get('user','name'))
print("user pass=",obj1.get('user','pass'))

print("services server=",obj1.get('services','server'))          

'''
output:
Sections= ['user', 'services']
user name= admin
user pass= admin123
services server= google.com
'''