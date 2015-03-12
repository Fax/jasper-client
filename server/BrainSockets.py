__author__ = 'fabrizio'

"""
     this is the standalone implementation of the brain.
     This will make easier the development of different clients on different machines/platform.
     Every single device could dialogate with the brain asking for data and giving updates in a natural way.


     The question is: Why a natural way?

     An asterisk plugin could be a client.
     An irc client could be a client.
     A twitter client could be a Brain client.
     A Facebook client could be a Brain client.

     Modules are made to allow the user to interact with something else through the brain.
     Clients are made to allow Something to interact with something else through the brain.

     The user could be another bot.

     Using sockets more users are allowed to connect at the same time.

"""

import socket
import threading
import SocketServer


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """
        This is the server itself
        It handles messages from clients

    """

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)

        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()


class BrainSocketServer():

    def __init__(self):
        """
        Start the SocketServer
        :return:
        """
        self.host = "localhost"
        self.port = 2220
        self.server = ThreadedTCPServer((self.host, self.port), ThreadedTCPRequestHandler)
        self.ip, self.port = self.server.server_address
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print "Server loop running in thread:", server_thread.name

    def turnoff(self):
        self.server.shutdown()



#Testing the client and the server instance
if __name__ == "__main__":
    bs = BrainSocketServer()
    client(bs.ip, bs.port, "lol" )
    client(bs.ip, bs.port, "lol3234")
    client(bs.ip, bs.port, "lolzzzzz")
    client(bs.ip, bs.port, "exit")
    bs.turnoff()

