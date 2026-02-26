import socket


def server():
    HOST="192.168.2.96" # host
    PYNQ="192.168.2.99"
    PORT=12345

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            pynqsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pynqsock.connect((PYNQ, PORT))
            with conn:
                while True:
                    if not conn.recv(1024):
                        break
                    pynqsock.send(b"beep")
                pynqsock.close()

                
server()
