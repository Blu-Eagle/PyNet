# import the necessary libraries
import socket

def get_remote_machine_ip():
	host_name = "www.google.com"
	ip_address = socket.gethostbyname(host_name)
	print ("IP : ", ip_address)

if __name__ == "__main__":
	get_remote_machine_ip()