from netmiko import ConnectHandler 


cisco1 = { 
    "ip": "192.168.56.104", 
    "device_type": "cisco_ios",
    "username": "cisco", 
    "password": "cisco123!", 
} 

#command = "show ip interface brief"
#command = "show running-config"
command = "show version"


with ConnectHandler(**cisco1) as net_connect: 
    output = net_connect.send_command(command) 


print() 
print(output) 
print() 