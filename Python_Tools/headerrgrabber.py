import requests
import sys
import urllib
from urllib.parse import urlparse

url = str(input('Please Enter the URL(google.com): ')).strip()

if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

parsed_url = urlparse(url)
if not parsed_url.netloc:
    print('Invalid Url Format! ')
    exit()

try:
    response = requests.get(url, timeout=5)
    print(f'\n[+]  HTTP Headers for: {url}\n' + '-'*40)
    for header, value in response.headers.items():
        print(f'{header}: {value}')
except requests.exceptions.RequestException as e:
    print(f'[-]  Error Fetching Headers: {e} ')
