import socket
import time
import signal
import sys

HOST="192.168.0.196"
PORT=12345

def run_program():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_l:
		sock_l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock_l.bind((HOST, PORT))
		sock_l.listen()
		print('Waiting for connection')
		conn, addr = sock_l.accept()
		print('Connected')
		with conn:
			data = conn.recv(1024)
		print(data.decode())


if __name__ == '__main__':
	original_sigint = signal.getsignal(signal.SIGINT)
	signal.signal(signal.SIGINT, exit)
	run_program()

