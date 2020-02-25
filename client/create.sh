echo "If you get an error reporting existing container, use docker rm <container hash>"

docker create --name my-zerorpc-client \
  --network zerorpc-net \
  -e host=my-zerorpc-server \
  zerorpc-client:latest

  echo "when ready, start with docker start <container hash>"