
FROM python

WORKDIR /main

COPY . .

RUN pip3 install kafka-python pymongo[srv] python-dotenv

CMD ["python","consumer.py"]