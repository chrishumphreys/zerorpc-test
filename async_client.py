# Simple ZeroRPC asynchronous client example
import zerorpc
import logging

logging.basicConfig(filename='async_client.log',level=logging.DEBUG)
client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4444")

result1 = client.long_running_task(async=True)
result2 = client.other_task(async=True)
result3 = client.other_task_with_Error(async=True)

zerorpc.gevent.joinall([result1, result2, result3])

print(result1.value)
print(result2.value)
print("processing result of other_task_with_Error")
try:
    if result3.exception:
        raise result3.exception
except Exception as e:
    print(e)

client.close()