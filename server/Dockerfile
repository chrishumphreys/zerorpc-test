FROM python:3
LABEL description="ZeroRPC server"

RUN pip install zerorpc
ADD ./server.py /
ENV port 4242
ENV host 0.0.0.0

CMD [ "sh", "-c", "python ./server.py --port=$port --host=$host --stdout" ]