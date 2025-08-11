import socket
import ipaddress
import time

ip = input('Please Enter Your IP Address: ')

try:
    ipaddress.ip_address(ip)
except ValueError:
    print('IP Address is not valid! ')
    exit()

startport = int(input('Enter the Start Port: '))
endport = int(input('Enter the End Port: '))

if startport < 1 or endport >  65536 or startport > endport:
    print('Invalid Port')
    exit()

print (f'\n[+]  Scanning {ip} from port {startport} to {endport}...\n')
socket.setdefaulttimeout(0.5)

open_ports = []
start_time = time.time()

for port in range(startport, endport + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f'[OPEN] Port {port}')
        open_ports.append(port)
    sock.close()

end_time = time.time()

print(f'[+]  Scan Completed!')
print(f'[+]  Open Ports: {open_ports if open_ports else 'None Found'}')
print(f'[+]  Time Taken: {round(end_time - start_time, 2)} seconds')
