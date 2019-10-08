# RFC retrival via `socket` module

```python
import socket
import sys

try:
    rfc_number = int (sys.argv[1])
except:
    print("Please enter an RFC number")
    sys.exit(2)

# defining basic parameters
host = 'www.rfc-editor.org'
port = 80
sock = socket.create_connection ((host, port))

req = (
    'GET /rfc/rfc{rfcNum}.txt HTTP/1.1\r\n'
    'HOST: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: closer\r\n'
    '\r\n'
)

template = req.format (rfcNum=rfc_number, host=host, port=port, version=sys.version_info[0])

# send the frame via TCP connection
sock.sendall (template.encode('ascii'))

# we now get the reply, so create a bytearray container
rfc_bytes = bytearray()

while True:
    buf = sock.recv(1024)

    if not len(buf):
        break

    rfc_bytes = rfc_bytes + buf

rfc = rfc_bytes.decode('utf-8')
print (rfc)
```