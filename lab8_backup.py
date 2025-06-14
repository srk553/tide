from netmiko import ConnectHandler

device_info = {
    'ios': ['192.168.1.1'],
    'junos': ['192.168.1.2']
}

for os_type, devices in device_info.items():
    for ip in devices:
        if os_type == 'ios':
            device_params = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': 'admin',
                'password': 'lab123',
            }
            cmd = 'show running-config'
        elif os_type == 'junos':
            device_params = {
                'device_type': 'juniper',
                'host': ip,
                'username': 'admin',
                'password': 'lab123',
            }
            cmd = 'show configuration | display set'
        else:
            print(f"Unsupported OS: {os_type}")
            continue
        
        net_connect = ConnectHandler(**device_params)
        output = net_connect.send_command(cmd)
        with open(f'{ip}_running.txt', 'w') as file:
            file.write(output)
        net_connect.disconnect()
