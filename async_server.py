# Simple ZeroRPC asynchronous server example

import zerorpc
import logging

class API():

    def long_running_task(self):
        logging.info('long_running_task call received')
        logging.info('1 - started long_running_task')
        #for instance a long running SQL query
        zerorpc.gevent.sleep(3)
        logging.info('2 - finished long_running_task')
        return "result from long_running_task"

    def other_task(self):
        logging.info('other_task call received')
        logging.info('1 - started other_task')
        pass
        logging.info('2 - finished other_task')
        return "result from other_task"

    def other_task_with_Error(self):
        logging.info('other_task_with_Error call received')
        zerorpc.gevent.sleep(1)
        raise Exception("A simulated exception from the server")

logging.basicConfig(filename='async_server.log',level=logging.DEBUG)
s = zerorpc.Server(API())
s.bind("tcp://0.0.0.0:4444")
zerorpc.gevent.spawn(s.run)
while True:
    zerorpc.gevent.sleep(10)