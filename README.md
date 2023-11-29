from email.message import EmailMessage
import ssl
import smtplib

my_email = 'snapcut3@gmail.com'
senha_gerada = 'gkjh fabf smfq tics'
destinatario = 'mauricio.batista@estudante.ifms.edu.br'
assunto = 'test'
body = 'testzinho'

en = EmailMessage()

en['From'] = my_email
en['To'] = destinatario
en['Subject'] = assunto
en.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(my_email, senha_gerada)
    smtp.sendmail(my_email, destinatario, en.as_string())

