FROM python:slim-buster

EXPOSE 5000

COPY . .

RUN pip3 install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 5000