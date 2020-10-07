# 네트워크로 메시지를 수신하여 메시지 송신자에게 수신한 메시지를 그대로 돌려보내는 서버 프로그램을 작성해보면서 소켓 프로그래밍에 대해 이해합니다.

import socket           # 소켓 모듈을 임포트합니다.

HOST = ''               # 서버의 ip와 사용할 포트번호 9009를 각각 지정합니다.host 와 port 는 생성한 소켓을 bind() 함수로 ip와 포트번호를 바인딩할 때 사용됩니다.
PORT = 9009             # host 값으로 빈 문자열을 지정하면 bind() 는 서버가 구동되는 컴퓨터의 ip 를 자동적으로 할당합니다.

def runServer():        # 네트워크 소켓은 네트워크 통신에 있어서 시작점이자 종점으로, 클라이언트나 서버 프로그램을 구현하기 위한 가장 핵심적인 모듈입니다. 서버와 클라이언트는 각자 네트워크 소켓을 가지고 있다.
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:   # tcp 소켓을 생성하고 socket 객체를 리턴합니다.생성된 socket 객체를 sock으로 둡니다.
        sock.bind((HOST,PORT))      # bind는 소켓을 지정된 ip와 포트번호로 바인딩하는 함수.생성한 소켓을 프로그램이 구동되는 컴퓨터의 ip와 포트번호 9009번으로 바인딩
        sock.listen(1)          # 서버가 한 번에 처리 가능한 연결 수를 1로 설정하고 기다리게 합니다. 5까지 가능
        print('클라이언트 연결을 기다리는 중..')
        conn,addr = sock.accept()   #accpet는 클라이언트로부터 연결 요청이 올 때까지 기다립니다.연결 요청이 오면 accept()는 클라리언트와 연결된 tcp소켓과 클라이언트주소 리턴
        with conn:
            print('[%s]와 연결됨'%addr[0])  #클라이언트가 연결되었다는 메시지를 클라이언트의 ip주소와 함께 화면에 출력
            while True:
                data = conn.recv(1024)     #conn.recv(1024)는 클라이언트로부터 1024바이트를 수신하고 수신한 데이터를 변수 data로 둡니다.
                if not data:               # 수신한 데이터가 없으면 while 루프를 빠져나온다.
                    break
                print('메시지 수신[%s]'%data.decode()) # 네트워크 소켓인 conn을 통해 수신한 데이터는 이진 바이트 스트림이다.data.decode()를 통해 사람이 알아볼 수 있는
                conn.sendall(data)                   # 문자열로 변환하여 화면에 출력함.수신한 데이터는 소켓의 sendall()을 이용해 클라이언트로 다시 전달.

runServer()