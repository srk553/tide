import csv
from netmiko import ConnectHandler

# Define device details once outside the loop
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.10',  # Replace with actual router/switch IP
    'username': 'admin',
    'password': 'lab123'
}

# Establish SSH connection
net_connect = ConnectHandler(**device)

# Read and apply VLANs
with open("vlan.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        vlan_id = row['vlan_id']
        vlan_name = row['vlan_name']
        config_cmds = [
            f'vlan {vlan_id}',
            f'name {vlan_name}'
        ]
        output = net_connect.send_config_set(config_cmds)
        print(output)

# Disconnect after all VLANs are configured
net_connect.disconnect()
