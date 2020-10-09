# 에코 서버에 접속하여 메시지를 송신하고, 동일한 메시지를 수신하는 에코 클라이언트입니다. 네트워크로 메시지를 서버로 송신하고 서버로부터 메시지를 그대로 수신하는 클라이언트
# 프로그램을 작성해보면서 소켓 프로그래밍에 대해 이해

import socket

HOST = 'localhost'      # 에코 클라이언트가 서버와 동일한 컴퓨터에서 실행되면 HOST 의 값으로 localhost를 설정하고 서버와 다른 컴퓨터에서 실행시 서버가 실행되는 컴퓨터ip 설정
PORT = 9009

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:   # tcp 소켓을 생성하고 sock으로 둡니다.
    sock.connect((HOST,PORT))               # (host,port)에 해당하는 원격 호스트로 연결을 시도, 클라이언트에서 이 부분을 실행하여 서버의 accept()에서 연결을 수락하게되면 클라이언트와 서버는 연결된 상태
    msg = input('메시지 입력:')
    sock.sendall(msg.encode())              # 메시지를 바이트 스트림으로 인코딩하고 소켓의 sendall()을 이용해 서버로 전송합니다
    data = sock.recv(1024)                  # 서버가 전송하는 데이터를 수신합니다.

print('에코 서버로부터 받은 데이터[%s]'%data.decode())  # 수신한 데이터를 화면에 출력,네트워크 소켓을 통해 수신받은 데이터는 이진 바이트 스트림이므로 디코딩해야 제대로 된 글자가보임
