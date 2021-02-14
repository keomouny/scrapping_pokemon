FROM python:latest
# WORKDIR /.
WORKDIR /scrap
# COPY . .
# COPY *.py .
# COPY main.py .
COPY . /scrap
RUN pip3 install -r files/requirements.txt
# RUN pip3 install requests bs4 mysql-connector-python
# CMD ["python3", "./main.py"]
