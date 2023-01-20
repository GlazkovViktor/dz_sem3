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


# from random import randint
# import itertools

# k = int(input('Задайте натуральную степень многочлена k: '))

# def get_ratios(k):
#     ratios = [randint(0, 100) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^'] * (k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')

# ratios = get_ratios(k)
# polynom = get_polynomial(k, ratios)
# print(polynom)

# m = int(input('Задайте натуральную степень второго многочлена m: '))

# second_polynom = get_polynomial(m, ratios)
# print(second_polynom)

# Крестики нолики

# board = [1,2,3,4,5,6,7,8,9]

# def frame(board):
#     print ("-------------")
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-------------")

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         frame(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     frame(board)

# main(board)

# кодирование
# s = 'EEEEAFFFBBCCCCCCD'
# def encode(s):
 
#     coding = ''
 
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         coding += str(count) + s[i]
#         i = i + 1
 
#     return coding

# print(encode(s))
#дЕКОДИРОВАНИЕ
# s = '4E1A3F2B6C1D'
# def coding(s):
#     number = ''
#     res = ''
#     for i in range(len(s)):
#         if not s[i].isalpha():
#             number += s[i]
#             print(number)
#         else:
#             res = res + s[i] * int(number)
#             number = ''
#     return res
# print(coding(s))