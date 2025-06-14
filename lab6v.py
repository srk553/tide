from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'lab123',
    'secret': 'lab123'
}

net_connect = ConnectHandler(**device)
net_connect.enable()

output = net_connect.send_command("show runnig-configuration | include hostname")
print(output)

net_connect.disconnect()
