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

        Feature ready

    """

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if data == 0:
                break
            print "something incoming"
            print data
            cur_thread = threading.current_thread()
            response = "{}: {}".format(cur_thread.name, data)
            self.request.send(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


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
    while True:
        pass
    bs.turnoff()

