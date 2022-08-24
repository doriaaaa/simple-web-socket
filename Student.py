import socket
import time
import random

def s1(s, host, port):
    s.connect((host, port))
    s.sendall(b'1155126139')
    new_port = s.recv(5)
    return new_port, s #return the socket

def s2(s2_port): #server
    listenPort = int(s2_port)
    localhost = ''
    print("Creating TCP socket...")
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.bind((localhost, listenPort))
    listenSocket.listen(5)
    print("Done")

    print("\nTCP socket created, ready for listening and accepting connection...")
    print("Waiting for connection on port", listenPort)

    # accept connections from outside, a new socket is constructed
    s2_socket, address = listenSocket.accept()
    print("\nClient from %s at port %d connected" % (address[0], address[1]))
    data = s2_socket.recv(12).decode('utf-8')
    ###########################Step 7#######################################
    bufsize = s2_socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("buffer size: ")
    print(bufsize)  # s2 buffer size
    ###########################Step 7#######################################
    return data, bufsize, s2_socket # str

def s3(host, fffff, eeeee, bufsize, s2_socket, s1_socket):
    size = random.randint(6, 9)
    byte_message = bytes(str(size), "utf-8")
    s3_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("", int(eeeee))
    s3_socket.bind(addr)
    s3_socket.sendto(byte_message, (host, fffff))
    ###########################Step 7#######################################
    byte_size = bytes(str(bufsize), "utf-8")
    s1_socket.sendall(byte_size) # step 7: send bufsize to s1

    print("\nreceiving large amount of data...")

    currentbufsize = [10, 25, 50] # change bufsize here
    for buffer in currentbufsize:
        s2_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffer)
        buffsize = s2_socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        list_data = []
        received_byte_size = 0
        max_time = 1
        start_time = time.time()
        while (time.time() - start_time) < max_time:
            large_data = s2_socket.recv(int(buffsize)).decode('utf-8') # string
            received_byte_size += len(large_data)
            list_data.append(large_data)
        print(f"Test: buffer size = {buffer} "
              f"[STUDENT] Number of received messages: {len(list_data)} total received bytes: {received_byte_size} "
              f"Throughput = {received_byte_size / 1}")
    s2_socket.close()
    ###########################Step 7#######################################
    print("\nReceiving UDP packet:")
    while True:  # remove potentially duplicate msg
        data, addr = s3_socket.recvfrom(int(size) * 10)
        print(data) # data = string
        if int(data) != int(size):
            break
    for i in range(0, 5):
        print("sending UDP packets")
        time.sleep(1)
        s3_socket.sendto(data, (host, fffff))

def main():
    # create tcp/ip socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    # host = 'set robot IP' #set robot ip
    port = 3310
    s2_port, s1_socket = s1(s, host, port)
    s3_data, bufsize, s2_socket = s2(s2_port)
    fffff = int(s3_data[0:5])
    eeeee = int(s3_data[6:11])
    s3(host, fffff, eeeee, bufsize, s2_socket, s1_socket)

if __name__ == "__main__":
    main()