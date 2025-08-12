import socket

PROTOCOL_REQUESTS = {
    80: b'HEAD / HTTP/1.1\r\nHost: example.com \r\n\r\n',
    443: b'',
    21: b'',
    25: b'',
    110: b'',
    143: b'',
}

def banner_grbber(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip, port))

            if port in PROTOCOL_REQUESTS and PROTOCOL_REQUESTS[port]:
                request = PROTOCOL_REQUESTS[port]
                if b'Host: example.com' in request:
                    host_line = f'Host: {ip}'.encode()
                    request = request.replace(b'Host: example.com', host_line)
                s.sendall(request)

            banner = s.recv(1024)
            print(f'[+]  Banner from {ip}:{port}:\n{banner.decode(errors='ignore')}')

    except socket.timeout:
        print(f'[!]  Connection to {ip}:{port} timed out.')
    except ConnectionRefusedError:
        print(f'[!]  Connection to {ip}:{port} refused.')
    except Exception as e:
        print(f'[!]  Error Connecting to {ip}:{port} - {e}')

if __name__ == '__main__':
    ip = input('Enter Ip Address: ')
    port = int(input('Enter the port: ').strip())
    banner_grbber(ip, port)
