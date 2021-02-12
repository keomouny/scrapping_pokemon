FROM python:3.9
WORKDIR /.
COPY . .
RUN pip install -r /files/requirements.txt
CMD ["python", "main.py"]
