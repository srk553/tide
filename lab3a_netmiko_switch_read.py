from netmiko import ConnectHandler

# Define the switch details
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.10',       # Replace with actual switch IP
    'username': 'admin',
    'password': 'lab123'
}

# Connect to the switch
net_connect = ConnectHandler(**device)

# Send the command to get VLANs
output = net_connect.send_command("show vlan brief")

# Print the output
print("=== VLANs on the Switch ===")
print(output)

# Disconnect from the switch
net_connect.disconnect()
