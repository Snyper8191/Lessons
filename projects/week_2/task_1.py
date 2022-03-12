import sys


def hello_user():
    while True:
        try:
            user_say = input('Скажи что-нибудь: ')
            if user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print('Сам ты {}'.format(user_say))
        except KeyboardInterrupt:
            print("\n Пока! ")
            break


hello_user()