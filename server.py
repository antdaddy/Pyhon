import smtplib
import socket

# функция отправки email @mail.ru

#def send_email(to_email, message):
 #   try:
        # создаем объект SMTP
  #      smtp_server = smtplib.SMTP('smtp.mail.ru', 587)
        # запускаем процесс авторизации
  #      smtp_server.starttls()
  #      smtp_server.login('d_d_a_37@mail.ru', 'm0dbgu1S3xep9aAEQd3h')
        # отправляем email
   #     smtp_server.sendmail('d_d_a_37@mail.ru', to_email, message)
        # закрываем соединение
   #     smtp_server.quit()
   #     return 'OK'
   # except Exception as e:
    #    return str(e)

# функция отправки email @gmail.com
def send_email(to_email, message):
    try:
        # создаем объект SMTP
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        # запускаем процесс авторизации
        smtp_server.starttls()
        smtp_server.login('antdaddyprod@gmail.com', 'pxui trhi zctf lkyx')
        # отправляем email
        smtp_server.sendmail('antdaddyprod@gmail.com', to_email, message)
        # закрываем соединение
        smtp_server.quit()
        return 'OK'
    except Exception as e:
        return str(e)


# создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем сокет с адресом и портом
server_socket.bind(('localhost', 8000))
# слушаем входящие соединения
server_socket.listen(1)

while True:
    # принимаем входящее соединение
    connection, address = server_socket.accept()
    # получаем данные от клиента
    data = connection.recv(1024).decode().split('|')
    email = data[0]
    message = data[1]
    # отправляем email
    response = send_email(email, message)
    # отправляем ответ клиенту
    connection.send(response.encode())
    # закрываем соединение
    connection.close()