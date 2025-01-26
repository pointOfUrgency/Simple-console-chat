import socket
import threading

clients = []

def broadcast(data, socket):
    ip, port = socket.getsockname()
    try:
        for client in clients:
            if client != socket:
                client.send(data.encode("utf-8"))
    except:
        print("[ERROR] hey Something went wrong...")
        clients.remove(client)


def handle_client(socket, address):
    print(f"[NOTIFICATION] The user: {address[0]}:{address[1]} has connected...")

    while True:
        try:
            data = socket.recv(1024).decode("utf-8")
            if data:
                print(f"Message from {address[0]}:{address[1]}:\n{data}")
                broadcast(data, socket)
            else:
                break
        except:
            break
    clients.remove(socket)
    socket.close()
    print(f"[DISCONNECT] The user {address[0]}:{address[1]} has disconnected...")

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9999))
    sock.listen(5)
    print("[LISTENING]")
    try:
        while True:
            s, addr = sock.accept()
            clients.append(s)
            thread = threading.Thread(target=handle_client, args=[s, addr])
            thread.start()
    except:
        print("[ERROR] Something went wrong...")


if __name__ == "__main__":
    server()