import socket

domain = input('Enter the domain: ').strip()

wordlist = input('Enter the path of the wordlist file: ').strip()

try:
    with open(wordlist, 'r') as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print (f'[-]  File not found!')
    exit()

print(f'[+]  Starting subdomain enumeration for: {domain}\n' + '-'*50)
for sub in subdomains:
    subdomain = f'{sub}.{domain}'
    try:
        ip = socket.gethostbyname(subdomain)
        print(f'[+]  Found: {subdomain} --> {ip}')
    except socket.gaierror:
        pass

print('\n[+]  Scan Complete!')
