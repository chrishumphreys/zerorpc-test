FROM python:3.8-slim-buster
LABEL description="ZeroRPC server"

RUN apt-get update
RUN apt-get -y install build-essential

RUN pip install zerorpc
ADD ./server.py /
ENV port 4242
ENV host 0.0.0.0

CMD [ "sh", "-c", "python ./server.py --port=$port --host=$host --stdout" ]