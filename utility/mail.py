import smtplib                                      # Импортируем библиотеку по работе с SMTP
from smtplib import SMTPHeloError, SMTPAuthenticationError, SMTPNotSupportedError
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML

def send_mail(addr_to, code):
    addr_from = "stellarium.bot@gmail.com"                # Адресат
   # addr_to   = "to_address@gmail.com"                  # Получатель
    password  = "02tidivu"                                  # Пароль

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'Подтверждение почты!'                   # Тема сообщения

    main = "Пожалуйста, не отвечайте на данное сообщение, оно отправлено автоматизированной системой, ответа не последует \r "
    link = "\nссылка для подтверждения регистрации: http://127.0.0.1:5000/confirm?code="+code
    body = main+link
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
    server.starttls()
    server.set_debuglevel(False)
    try:
        server.login(addr_from, password)
    except SMTPNotSupportedError:
        print("1")
    except SMTPAuthenticationError:
        print("2")
    except SMTPHeloError:
        print("3")
    #server.sendmail(msg)
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()