#socketserver를 이용하여 기능이 향상된 에코 서버를 만들어 보자
# socketserver 모듈은 네트워크 서버를 간단하고 편리하게 만들게 해주는 다양한 방법을 제공해주는 서버 구현을 위한 프레임워크.

import socketserver

HOST = ''
PORT = 9009

class MyTcpHandler(socketserver.BaseRequestHandler):    # MyTcpHandler는 socketserver.BaseRequestHandler 클래스를 상속받은 클래스,TCPServer 객체를 생성할떼 인자로 사용
    # 이 클래스는 서버 하나당 단 한 번 초기화됩니다. TCPServer 가 객체활 될 때.이 클래스는 client의 요청에 대한 처리 담당
    # handle() 메소드에 클라이언트 연결 처리를 위한 로직을 구현합니다.
    def handle(self) -> None:       # 클라이언트의 연결과 요청 작업을 처리함
        print('[%s] 연결됨'%self.client_address[0])    

        try:
            while True:
                self.data = self.request.recv(1024)#socketserver.BaseRequestHandler 클래스의 클래스 멤버인 request는 클라이언트 소켓과 연결된 서버의 tcp소켓
                if self.data.decode() == '/quit':
                    print('[%s] 사용자에 의해 중단 '%self.client_address[0])
                    return
                print('[%s]'%self.data.decode())
                self.request.sendall(self.data) # 클라이언트로 재전송

        except Exception as e:
            print(e)

def runSerer():
    print('+++에코 서버를 시작합니다.')
    print('+++에코 서버를 끝내려면 ctrl+c를 누르세요.')

    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)   # PORT 번호로 HOST와 바인딩하녀 socketserver.TCPServer 객체를 생성하고 server로 둡니다.
        server.serve_forever()                      # 생성된 TCPServer 객체에 연결되는 요청 처리는 MyTcpHandler가 담당.
    except KeyboardInterrupt:           # server.serve_forever()는 server.shutdown()호출이나 사용자가 ctrl+c를 눌러 강제로 종료하기 전끼지 클라이언트 연결을 기다림
        print('---에코 서버를 종료합니다.')


runSerer()