from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',  # Change to your router's IP
    'username': 'admin',
    'password': 'lab123',
}

net_connect = ConnectHandler(**device)

# Get hostname from running config
output = net_connect.send_command("show running-config | include hostname")
print("Current hostname line:", output)

# Change hostname if needed
new_hostname = "BRANCH1"
config_commands = [f"hostname {new_hostname}"]
output = net_connect.send_config_set(config_commands)
print("Config change output:")
print(output)

net_connect.disconnect()
