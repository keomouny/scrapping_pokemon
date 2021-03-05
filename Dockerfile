FROM python:latest

WORKDIR /scrap_pokemontrash

EXPOSE 5000

ENV FLASK_APP=main.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_ENV=development

COPY . .

RUN pip3 install -r files/requirements.txt

CMD ["flask", "run"]

# CMD ["python3"]