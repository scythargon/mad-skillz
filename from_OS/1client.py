import Pyro4
Pyro4.config.HMAC_KEY='123'
remoteServer = Pyro4.Proxy('PYRONAME:server')

class square:
    def handle(self,x): 
        return x**2
#print square().handle(5)
print remoteServer.evaluate(square(), 4)
