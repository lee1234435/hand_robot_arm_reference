# import bluetooth

# server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# port = 1
# server_sock.bind(("", port))
# server_sock.listen(1)

# client_sock, address = server_sock.accept()
# print("Accepted connection from", address)

# data = client_sock.recv(1024)
# print("Received:", data)

# client_sock.close()
# server_sock.close()


import bluetooth
def bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    server_socket.bind(("", port))
    server_socket.listen(1)
    bluetooth.advertise_service(server_socket, "SampleServer",
                                service_classes=[bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])
    print("블루투스 서버가 시작되었습니다. 연결을 기다립니다...")
    client_socket, address = server_socket.accept()
    print(f"연결된 주소: {address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"받은 데이터: {data.decode()}")
            if data.decode() == "아포가토":
                # 아포가토 작업 시작
                print("아포가토 작업을 시작합니다.")
    except OSError:
        pass
    print("연결 종료")
    client_socket.close()
    server_socket.close()

bluetooth_server()