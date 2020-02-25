docker network create zerorpc-net

docker create --name my-zerorpc-server \
  --network zerorpc-net \
  --publish 4242:4242 \
  zerorpc-server:latest

  