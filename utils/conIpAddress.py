import socket

def convert_to_diff_format():
	for ip_addr in ['127.0.0.1','192.168.0.1']:
		packed_ip_addr = socket.inet_aton (ip_addr)
		unpacked_ip_addr = socket.inet_ntoa (packed_ip_addr)

		# print the packed and unpacked ip address
		print ("Packed : ", packed_ip_addr)
		print ("Unpacked : ", unpacked_ip_addr)

if __name__ == "__main__":
	convert_to_diff_format()