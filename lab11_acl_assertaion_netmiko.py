from netmiko import ConnectHandler

# Device connection details
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'lab123',
    'secret': '',  # enable password if needed
}

# Connect to device
net_connect = ConnectHandler(**device)

# Optional: enter enable mode if you need privileged commands
# net_connect.enable()

# Run command to get ACL info (you can use "show access-lists" or "show ip access-lists")
output = net_connect.send_command('show ip access-lists')

# Check if the ACL rule exists in the output
if 'deny tcp any any eq 23' in output:
    print("ACL rule found!")
else:
    print("ACL rule not found.")

# Disconnect from device
net_connect.disconnect()
