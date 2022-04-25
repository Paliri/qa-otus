# 1. создать произвольный список из 8 элементов, проверить что длина списка равна 8 элементам.
# 2. сложить две строки, проверить что полученный результат соответствует ожидаемому.#
# 3. вывести максимальное простое число
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.
# 10.


import pytest
import random



def test_list():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    assert len(l) == 8

def test_two():
    cat1 = "Charlie"
    cat2 = "Olaf"
    cats = cat1 + cat2
    print (cats)
    assert cats == "CharlieOlaf"

def test_colors():
    i = 1
    for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
        print('#', i, ' color of rainbow is ', color, sep='|')
        i += 1

def test_prostye():
    MAX = 100
    p = 0
    for n in range(1,MAX):
        for i in range(2,n):
            if n % i == 0:
                break
            if i == n-1:
                p = n
    print(p)
                # print("n =", n, "i =", i, "rem =", n % i)

# def test_string():
#     str1 = input("enter something: ")
#     str2 = input("enter something else: ")
#     length = len(str1) + len(str2)
#     print("total length of input is", length)
#     print("found", str1.count("в"), "letters 'в' in", str1)
#
# def test_numbers():
#     lst = []
#     lst.append([1, 4, 7, 436457])
#     lst[0] = 10
#     lst.extend([786, "e46", 363])
#     lst[1] = 3
#     print(lst)
#     lst_final = input("Enter smth \n")
#     lst.append(lst_final)
#     for i in lst:
#         print(i)
#     assert lst[len(lst) - 1].isnumeric(), "expected number"


def test_apozh():
    peremenn = list("ЖОПА")
    peremenn.reverse()
    print(peremenn)
    assert peremenn == ['А', 'П', 'О', 'Ж']


def test_apozh2():
    peremenn = [4, 6, 9, 3, 9, 3]
    peremenn2 = reversed(peremenn)
    print(peremenn, peremenn2)
    print(peremenn, list(peremenn2))

def test_tuple_count():
    abc = ('a', 'b', 'c', 'd', 'e', 'f', 'j')
    findB = abc.count('b')
    assert findB == 1

def test_tuple_index():
    abc = ('a', 'b', 'c', 'd', 'e', 'f', 'j')
    indexB = abc.index('b')
    assert indexB == 1
    assert abc[indexB] == 'b'
    assert abc[abc.index('b')] == 'b'

def test_tuple_index_exception():
    abc = ('a', 'b', 'c', 'd', 'e', 'f', 'j')
    with pytest.raises(Exception):
        abc.index('q')

def test_set_intersection():
    "функция сравнивает пересечения в 2 списках и проходит если их 3"
    first_set = {1, 2, 4, 7, 8,}
    second_set = {1, 7, 9, 2, 3}
    intersect = first_set.intersection(second_set)
    len_intersect = len(intersect)
    assert len_intersect == 3
    help(test_set_intersection)

def test_dict():
    list_num = [1, 2, 3, 4, 5]
    list_name = ['masha', 'lesha', 'olaf', 'charley', 'edgar']

    users = {}
    users[0] = "Admin"
    i = 0
    while i < len(list_name):
        users[list_num[i]] = list_name[i]
        i = i + 1
    print(users)
    print(users.keys())
    print(users.values())
    assert len(users.values()) == len(users.keys())

@pytest.fixture()
def fixture_random_number ():
    return random.randint(1, 100)



def test_login(fixture_random_number):
    rnd = fixture_random_number
    if rnd != 2:
        print ("you are winner with", rnd)
    if rnd == 2:
        print ("looser")
    assert rnd != 2

def test_sum_four(fixture_random_number):
    num1 = fixture_random_number
    num2 = fixture_random_number
    print("sum", num1, '&', num2, "equals", num2 + num1)
    
