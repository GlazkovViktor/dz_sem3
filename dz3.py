# Домашнее задание 4


from random import randint
import itertools


# # def create_equation():
# #     equation = {}
# #     k = int(input("Введите ммксимальную степень: "))
# #     for i in range(k, -1, -1):
# #         if i == k:
# #             koef = randint(1, 100)
# #             equation[i] = koef
# #         else:
# #             equation[i]=randint(0,100)
# #     return equation
# # print(create_equation())


# k = int(input('Задайте натуральную степень многочлена k: '))


# def get_ratios(k):
#     ratios = [randint(0, 100) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios



# def get_polynomial(k, ratios):
#     var = ['*x^'] * (k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
#         ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x', ' x')

# ratios = get_ratios(k)
# print(ratios)
# polynom = get_polynomial(k, ratios)
# print(polynom)


from random import randint
import itertools

k = int(input('Задайте натуральную степень многочлена k: '))

def get_ratios(k):
    ratios = [randint(0, 100) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^'] * (k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratios = get_ratios(k)
polynom = get_polynomial(k, ratios)
print(polynom)

m = int(input('Задайте натуральную степень второго многочлена m: '))

second_polynom = get_polynomial(m, ratios)
print(second_polynom)
