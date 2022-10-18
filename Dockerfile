FROM python

WORKDIR /main

COPY ./requirements.txt /main/requirements.txt  

RUN pip install --no-cache-dir --upgrade -r /main/requirements.txt 

COPY ./application /main/application

EXPOSE 8000

CMD ["uvicorn","application.main:app","--proxy-headers", "--host","0.0.0.0", "--port","8000"]