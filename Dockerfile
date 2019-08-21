FROM python:2

ADD insert.py /

RUN pip install mysql-connector

ENTRYPOINT ["python"]
CMD [ "insert.py", "-i", "naved", "-o" , "shah"]