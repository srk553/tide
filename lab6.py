from netmiko import ConnectHandler

# Device information
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'lab123',
}

# List of configuration commands
commands = [
    'hostname NewR1',
    'interface e0/0',
    'description Connection to the Core',
]


print(f"Connecting to {device['ip']}...")
net_connect = ConnectHandler(**device)

print("Sending configuration...")
output = net_connect.send_config_set(commands)
print(output)

print("Disconnecting...")
net_connect.disconnect()
print("Configuration complete!")

