# def add_two(x):
#     return x+2

# def calculate_two(eq: str):
#     first, sym, snd = eq.split()
#     try:
#         first, snd = int(first), int(snd)
#     except ValueError:
#         print('Формат ввода: VALUE1 <+-*/> VALUE2\n\
#             Пример: 1*2')
#     if sym == '+':
#         return first + snd
#     elif sym == '-':
#         return first - snd
#     elif sym == '*':
#         return first * snd
#     elif sym == '/':
#         return first / snd

# print(calculate_two('1 + 2'))
# print(calculate_two('3 / 2'))

# def heshteg(str):
#     str = str.split()
#     stroka = '#'
#     for n in range(len(str)):
#         stroka += str[n].capitalize()
#     return stroka
# print(heshteg('привет пока'))

# def map_move(mass):
#     subs = {'W':'E', 'E':'W', 'N':'S', 'S':'N'}
#     run = True
#     while run :
#         run= False
#         for i in range(1, len(mass)):
#             if subs[mass[i]] == mass[i-1]:
#                 mass.pop(i)
#                 mass.pop(i-1)
#                 run = True
#                 break
#     return mass
# print(map_move(['w', 'N', 'E', 'W', 'S']))

# def check_result(marks):
#     good = marks.count(1)
#     if good/len(marks)*100 >= 80:
#         return 'Пока ок'
#     else: return 'Отчислен'

# def return_from_list(index):
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     return nums[index]

# def division(a, b):
#     return a/b
# print(division(10, 5))

def file_1(name):
    with open(name, 'r') as file:
        list_1 = file.readlines()
    result = {}
    for line in list_1:
        k, v = line.split('=')
        v = int(v)
        result[k] = v
    return result


print(file_1('name.txt'))
