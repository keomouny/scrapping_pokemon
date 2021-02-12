FROM python:3.9
WORKDIR /scrap
RUN pip install -e files/requirements.txt
COPY main.py .
CMD ["python", "main.py"]
