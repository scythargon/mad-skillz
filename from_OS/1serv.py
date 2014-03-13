import Pyro4
Pyro4.config.HMAC_KEY='123'
class Server(object):
    def evaluate(self, hand, args):
        pass
        #return hand.handle(args)

def main():
    server = Server()
    Pyro4.Daemon.serveSimple(
            {
                server: "server"
            },
            ns=True)

if __name__ == '__main__':
    main()
