FROM python:alpine3.7
COPY ./app /app
WORKDIR /app/
RUN pwd
RUN ls /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./flapp.py
