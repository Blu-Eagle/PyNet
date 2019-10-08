# import the necessrary library
import socket

def print_machine_info():
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	print ("Host name : ",host_name)
	print ("IPV4 address : ",ip_address)

if __name__ == "__main__":
	# invoke the function
	print_machine_info()