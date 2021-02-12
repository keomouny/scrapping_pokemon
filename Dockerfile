FROM python:latest
WORKDIR /.
# WORKDIR /scrap
COPY . .
# COPY *.py .
RUN pip install -r /files/requirements.txt
#RUN pip3 install requests bs4 mysql-connector-python
CMD ["python", "main.py"]
