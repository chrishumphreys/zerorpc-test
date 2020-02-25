docker network create zerorpc-net

echo "If you get an error reporting existing container, use docker rm <container hash>"

docker create --name my-zerorpc-server \
  --network zerorpc-net \
  --publish 4242:4242 \
  zerorpc-server:latest

    echo "when ready, start with docker start <container hash>"