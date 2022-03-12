"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():

    list_1 = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}]

    sum_product = 0
    count_product = 0
    for Product in list_1:
        sum_product = sum_product + sum(Product["items_sold"])
        count_product = count_product + len(Product["items_sold"])
        av_count = int(sum(Product["items_sold"])/len(Product["items_sold"]))
        print(f'Суммарное колличество продаж телефона {Product["product"]} составляет {sum_product}')
        print(f'Среднее колличество продаж телефона {Product["product"]} составляет {av_count}')

    print(f'Сумма всех проданных телефонов {sum_product}')
    print(f'Среднее количество продаж {int(sum_product/count_product)}')



if __name__ == "__main__":
    main()