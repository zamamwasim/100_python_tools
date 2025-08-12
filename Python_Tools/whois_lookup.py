import whois

domain = input('Please Enter the Domain(e.g: google.com): ').strip()

try:
    w = whois.whois(domain)
    print(f'\n[+]  Whois lookup for domain: {domain}')
    print(f'-' * 40)
    for key, value in w.items():
        print(f'{key}: {value}')

except Exception as e:
    print(f'Error: {e}')
