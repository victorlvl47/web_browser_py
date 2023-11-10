import socket
from urllib.parse import urlparse

# url
url = input("Enter URL: ")
if not url:
    url = "http://data.pr4e.org/romeo.txt"


# get domain
parsed_url = urlparse(url)
domain = parsed_url.netloc


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(515)
    if (len(data) < 1):
        break

    print(data.decode())

mysock.close()
