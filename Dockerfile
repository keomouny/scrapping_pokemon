FROM python:latest

WORKDIR /scrap

COPY . .

RUN pip3 install -r files/requirements.txt

# CMD ["python3", "./main.py"]
