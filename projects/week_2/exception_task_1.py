"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
        while True:
            try:
                hello_text = input('Как дела? \n')
                if hello_text== 'Пока':
                    print('Ну пока')
                    break
                else:
                    print('Сам ты {}'.format(hello_text))
            except KeyboardInterrupt:
                print("\n Пока! ")
                break

if __name__ == "__main__":
    hello_user()

