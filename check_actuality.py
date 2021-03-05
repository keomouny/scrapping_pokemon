import os
import db
import pokemon
import smtplib
import ssl
from setup_logger import logger, pwd_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class CheckActuality:
    def __init__(self):
        logger.info('instanciation checkActuality class')
        self.result_query = self.check_db()
        self.result_scrap = self.check_scrap()

    def check_db(self):
        connect_db = db.DB()
        mycursor = connect_db.myconn.cursor(dictionary=True)
        query_specify = 'SELECT id, title, author FROM all_news;'
        mycursor.execute(query_specify)
        result = mycursor.fetchall()
        connect_db.myconn.commit()
        connect_db.myconn.close()
        return result

    def check_scrap(self):
        get_pokemon = pokemon.pokemon()
        data = get_pokemon.soup.find_all('li', {
            'class': 'post'})
        list_result_scrap = get_pokemon.get_all_news(data)
        return [i for i in list_result_scrap]

    def campare_scrap_and_db(self):
        all_news = self.get_diff_list(self.result_query, self.result_scrap)
        db = db.DB()
        if len(all_news) > 0:
            db.insert_data(all_news, pokemon().scrap_data(all_news))
            db.__disconnect__()
            self.send_mail()

    def get_diff_list(self, list_query, list_scrap):
        # get all title from query database
        list_title_news_query = [i['title'] for i in list_query]
        # compare each title from scrapping to title's list from query database
        return [i for i in list_scrap if i[0] not in list_title_news_query]

    def send_mail(self):
        sender_email = "mouny.keo@hetic.net"
        receiver_email = "keomouny02@gmail.com"
        password = pwd_mail

        message = MIMEMultipart("alternative")
        message["Subject"] = "nouvelle actualité sur pokémon"
        message["From"] = "scrapper_pokemontrash.com"
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Bonjour,
        voici l'actualité pokémon"""
        html = """\
        <html>
        <body>
            <p>Bonjour,<br>
            Voici l'actualité pokémon?<br>
            <a href="https://www.pokemontrash.com/">pokémon</a> 
            has many others news.
            </p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )


test_check = CheckActuality()
test_check.compare_scrap_and_db()
