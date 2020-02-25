# zerorpc-test
Simple starter project for zerorpc clients/servers

using https://www.zerorpc.io/

## setup

### Create a virtualenv to run each python process

`python3 -m venv zerorpc-env
. zerorpc-env/bin/activate
pip install zerorpc`


## run simple synchronous examples
`. zerorpc-env/bin/activate
python server.py`

`. zerorpc-env/bin/activate
python client.py`

logs are written to client.log and server.log

## run asynchronous examples

`. zerorpc-env/bin/activate
python async_server.py`


`. zerorpc-env/bin/activate
python async_client.py`

logs are written to async_client.log and async_server.log

## HA

Use HAProxy toproxy requests to multiple backends and connect via HAProxy

### Start proxy

`haproxy -f haproxy.cfg`

### Start backends

`. zerorpc-env/bin/activate
python server.py --port=4242`

`. zerorpc-env/bin/activate
python server.py --port=4243`

### run some clients

`. zerorpc-env/bin/activate
./load_test_client.sh 10`

## Limitations

No security: bind 0mq to localhost and use stunnel with client certificates
Not convinced streaming or hearbeats work with HA

