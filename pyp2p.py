import json
from uuid import uuid4
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

generate_nodeid = lambda: str(uuid4())


class PyP2P_Protocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.state = "PyP2P"
        self.remote_nodeid = None
        self.nodeid = generate_nodeid()

    def connectionMade(self):
        print('connection from', self.transport.getPeer())


class PyP2P_Factory(Factory):
    def startFactory(self):
        self.peers = {}
        self.nodeid = generate_nodeid()

    def buildProtocol(self, addr):
        return NCProtocol(self)


if if __name__ == "__main__":
    endpoint = TCP4ServerEndpoint(reactor, 5999)
    endpoint.listen(PyP2P_Factory())

