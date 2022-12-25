# Домашнее задание 3 семинар

# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# summ=0
# my_list = [1, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 33, 35]
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         summ = summ + my_list[i]
# print(summ)

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# my_list = [2,3,5,6]
# mult = 0
# my_mult = []
# leng = len(my_list)
# if leng%2 == 0:
#     for i in range(int(leng/2)):
#         mult = my_list[i]*my_list[((len(my_list))-1-i)]
#         my_mult.append(mult)
# else:
#     for i in range(int(leng/2)+1):
#         mult = my_list[i]*my_list[((len(my_list))-1-i)]
#         my_mult.append(mult)
# print(my_mult)

# 3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# N = int(input('Введите размер списка: '))
# my_list = []
# my_list2 = []
# ostatok = 0
# for i in range(N):
#     my_list.append(
#         float(input('Введите вещественные элементы массива через Enter: ')))
# for i in range(len(my_list)):
#     ostatok = round((my_list[i]-int(my_list[i])), 5)
#     if ostatok != 0:
#         my_list2.append(ostatok)
# print(my_list)
# print(my_list2)
# max_num = max(my_list2)
# min_num = min(my_list2)
# diff = max_num-min_num
# print(diff)

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное
# N = int(input('Введите число которое требуется перевести: ' ))
# A = ''
# while N > 0:
#     A = str(N % 2) + A
#     N = N // 2
 
# print(A)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  P.S. ЗАДАЧУ ЧЕСТНО СПИСАЛ, САМ НЕ ДОДУМАЛСЯ КАК ДЕЛАТЬ
def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input("Введите целое число: "))
my_list = [findFib(i) for i in range(1, n+2)]
print(my_list)
my_list = my_list[::-1] + my_list[1:]
print(my_list, '\n')  
