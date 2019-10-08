import socket

def find_service_name():
	protocol_name = 'tcp'

	# pass the port numbers here
	for port in [80,25]:
		print ("Port : ",port," Service : ", socket.getservbyport(port,protocol_name))

if __name__ == "__main__":
	find_service_name()