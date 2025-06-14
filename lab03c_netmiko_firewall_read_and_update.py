from netmiko import ConnectHandler

device = {
    'device_type': 'juniper',
    'host': '192.168.1.2',
    'username': 'admin',
    'password': 'lab123',
}

net_connect = ConnectHandler(**device)

# Enter configuration mode
net_connect.config_mode()

# Read the hostname
output = net_connect.send_command("show configuration system host-name")
print(output)

# Set the hostname
net_connect.send_config_set(['set system host-name juniper-r1'])

# Commit the changes
net_connect.commit()

# Exit configuration mode (optional, automatically exits after commit)
net_connect.exit_config_mode()

# Verify the hostname (optional)
output = net_connect.send_command("show configuration system host-name")
print(output)

# Disconnect session
net_connect.disconnect()
