# Simple ZeroRPC synchronous server example

import zerorpc
import logging
import argparse

class HelloRPC(object):
    def hello(self, name):
        logging.info('hello call received')
        return "Hello, %s" % name


    @zerorpc.stream   
    def streaming_range(self, fr, to, step):
        logging.info('streaming_range call received')
        return range(fr, to, step)


    def bad(self):
        logging.info('bad call received')
        raise Exception("A simulated exception from the server")


parser = argparse.ArgumentParser(description='Simple RPC server')
parser.add_argument('--port', nargs='?', default=4242, type=int)
parser.add_argument('--host', nargs='?', default="0.0.0.0", type=str)
args = parser.parse_args()

logging.basicConfig(filename='server.log',level=logging.DEBUG)
s = zerorpc.Server(HelloRPC())
bind_addr = "tcp://{}:{}".format(args.host, args.port)
print("binding server to {}".format(bind_addr))
s.bind(bind_addr)
s.run()
