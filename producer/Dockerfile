
FROM python

WORKDIR /main

COPY . .

RUN pip3 install kafka-python

CMD ["python","producer.py"]