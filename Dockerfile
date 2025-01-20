FROM python:3.11.9

  

COPY football.py /

COPY main_script.py /

COPY time_func.py /

COPY twitter.py /

COPY .env /

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

  

WORKDIR /

CMD ["python3", "main_script.py"]