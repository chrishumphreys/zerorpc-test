FROM python:3.8-slim-buster
LABEL description="ZeroRPC client"

RUN apt-get update
RUN apt-get -y install build-essential

RUN pip install zerorpc
ADD ./client.py /
ENV clientport 4242
ENV host 127.0.0.1

CMD [ "sh", "-c", "python ./client.py --port=$clientport --method=simple --host=$host --stdout" ]