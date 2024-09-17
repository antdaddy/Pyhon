import socket

def send_email(email, message):
    # создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # подключаемся к серверу
    client_socket.connect(('localhost', 8000))
    # отправляем данные на сервер
    data = email + '|' + message
    client_socket.send(data.encode())
    # получаем ответ от сервера
    response = client_socket.recv(1024).decode()
    # закрываем сокет
    client_socket.close()
    return response



while True:
    email = input('Введите email: ')
    message = input('Введите сообщение: ')
    response = send_email(email, message)
    if response == 'OK':
        print('Сообщение отправлено')
        break
    else:
        print(response)

