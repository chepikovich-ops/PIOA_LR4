from itertools import product
from itertools import zip_longest
import random
def get_set(filename):
    return set(open(filename, encoding= 'utf-8' ).read().split())

def start_calc():
    while True:
        s1 = get_set('set1.txt')
        s2 = get_set('set2.txt')
        print("множества")
        print(s1)
        print(s2)
        print("1. объединение (+ или |)")
        print("2. пересечение (&)")
        print("3. разность (set1 - set2)")
        print("4. разность (set2 - set1) ")
        print("5. Декартово произведение")
        print("6. выборка: случайная разность")
        print("7. выборка: 3 случайных элемента из случайного множества")
        print("8. выборка: случайная с вероятностью")
        print("9. случайная выборка пары из пересечения")
        print("10. проекция")
        print("11. деление на третье множества")
        print("12. соединение")
        print("0 — выход")
        line = input(">").strip().lower()
        if line in ('0'):
            print("выход ")
            break

        if line in ('1', '+', '|'):
            res = s1 | s2
            result = "объединение"
        elif line in ('2', '&'):
            res = s1 & s2
            result = "пересечение"
        elif line in ('3'):
            res = s1 - s2
            result = "разность (1-2)"
        elif line in ('4'):
            res = s2 - s1
            result = "разность (2-1)"
        elif line in ('5'):
            res = set(product(s1, s2))
            result = "декартово произведение"
        elif line in ('6'):
            diff = list(s1 - s2)
            if diff:
                #выбор случайных элементов, которые есть в s1, но которых точно нет в s2
                res = random.choice(diff)
                result = ("случайная разность")
        elif line in ('7'):
            chosen_set = random.choice([s1, s2])
            # берем 3 случайных элемента из выбранного множества
            res = random.sample(list(chosen_set), min(3, len(chosen_set)))
            result = ("выборка 3 случайных элемента из случайного множества")
        elif line in ('8'):
            # oставляем элемент из объединения s1 и s2 с вероятностью 0.5
            res = {x for x in (s1 | s2) if random.random() > 0.5}
            result = ("случайная выборка")
        elif line in ('9'):
            # Находим общие, превращаем в список и берем 2 случайных символа
            common = list(s1 & s2)
            if len(common) >= 2:
                res = random.sample(common, 2)
                result = ("случайная выборка из пересечения")
        elif line in ('10'):
            table = list(zip_longest(s1, s2, fillvalue="None"))
            # удаляем дубликаты строк и получаем множество уникальных пар
            res = {(row[0], row[1]) for row in table}
            result=("проекция")
        elif line in ('11'):
            s3 = {'6', 'i', '8'}  #делитель
            #cоздаем таблицу пар (делимое)
            pairs = [(a, b) for a in s1 for b in s2]
            # находим такие a, для которых в парах есть все b из s3
            res = {a for a in s1 if all((a, b) in pairs for b in s3)}
            # в данном случае результатом будет тоже множество s1 (так как s3 подмножество s2)
            # если s3 не будет подмножеством будет выводить пустое множество
            # так как ни один элемент из s1
            # не сможет образовать пару с несуществующим элементом
            # имеем что имеем
            result = "деление на третье множества"
        elif line in ('12'):
            if not s1 or not s2:
                result = set()
                # если предположить что множество однородно проверяем по первому значению
            len_s1 = len(next(iter(s1)))
            len_s2 = len(next(iter(s2)))
            # если односимвольные
            if len_s1 == 1 and len_s2 == 1:
                res = s1 | s2
                result=("объединение изза односимвольности")
            # чтоюы работало соединение нужны пары или боллее длинные кортежи
            elif len_s1 >= 2 and len_s2 >= 2:
                res = {
                    a + b[1:]
                    for a in s1
                    for b in s2
                    if a[-1] == b[0]
                }
                result = "соединение"
        else:
            print("неизвестная команда")
            continue
        print(f"\nрезультат ({result}):")
        print(res if res else "пустое множество")
if __name__ == "__main__":
    start_calc()
