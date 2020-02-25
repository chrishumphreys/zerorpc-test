docker create --name my-zerorpc-client \
  --network zerorpc-net \
  -e host=my-zerorpc-server \
  zerorpc-client:latest