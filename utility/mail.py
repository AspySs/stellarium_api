import smtplib                                      # Импортируем библиотеку по работе с SMTP
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from log.logger import log_error

def send_mail(addr_to, code):
    addr_from = "stellarium.bot@gmail.com"                # Адресат
   # addr_to   = "to_address@gmail.com"                  # Получатель
    password  = "02tidivu"                                  # Пароль
    addr = "http://192.168.1.105:5000/confirm?code="

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'Подтверждение почты!'                   # Тема сообщения

    main = "Пожалуйста, не отвечайте на данное сообщение, оно отправлено автоматизированной системой, ответа не последует \r "
    link = "\nссылка для подтверждения регистрации: " + addr + code
    body = main+link
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
    server.starttls()
    server.set_debuglevel(False)
    try:
        server.login(addr_from, password)
    except Exception as e:
        log_error(str(e), "send_mail")
    #server.sendmail(msg)
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()

def send_mail_pas_rec(addr_to, code, mail, passw):
    addr_from = "stellarium.bot@gmail.com"                # Адресат
   # addr_to   = "to_address@gmail.com"                  # Получатель
    password  = "02tidivu"                                  # Пароль
    addr = "http://127.0.0.1:5000/passActivate/"
    req = "?mail=" + mail + "&code=" + code

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'Восстановление пароля!'                   # Тема сообщения

    main = "Пожалуйста, не отвечайте на данное сообщение, оно отправлено автоматизированной системой, ответа не последует \r "
    link = "\nссылка для активации временного пароля: "+passw+"\n перейдите для активации: " + addr + req
    body = main+link
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
    server.starttls()
    server.set_debuglevel(False)
    try:
        server.login(addr_from, password)
    except Exception as e:
        log_error(str(e), "send_mail_pas_rec")
    #server.sendmail(msg)
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()