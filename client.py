# Simple ZeroRPC synchronous client example

import zerorpc
import logging
import argparse

parser = argparse.ArgumentParser(description='Simple RPC client')
parser.add_argument('--port', nargs='?', default=4242, type=int)
parser.add_argument('--method', nargs='?', default="all", type=str)

args = parser.parse_args()
logging.basicConfig(filename='client.log',level=logging.DEBUG)
c = zerorpc.Client()
addr="tcp://0.0.0.0:{}".format(args.port)
print("Connecting to {}".format(addr))
c.connect(addr)
method = args.method
print("Calling {}".format(method))

if method == "simple" or method == "all":
    #Call simple method
    print(c.hello("RPC"))

if method == "exception" or method == "all":
    #Call exception method
    try:
        c.bad()
    except Exception as e:
        print("An error occurred: %s" % e)

if method == "streaming" or method == "all":
    #call streaming method
    for item in c.streaming_range(10, 20, 2):
        print(item)
