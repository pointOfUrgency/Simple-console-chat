import socket
import threading


def send(sock):
    while True:
        try:
            data = input("Type your message here:\n").encode('utf-8')
            if data == 'exit':
                break
            sock.send(data)
        except:
            print("Something went wrong...")


def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except:
            print("Something went wrong...")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9999))

    send_thread = threading.Thread(target=send, args=[sock])
    recv_thread = threading.Thread(target=receive, args=[sock])
    send_thread.start()
    recv_thread.start()


if __name__ == "__main__":
    main()
