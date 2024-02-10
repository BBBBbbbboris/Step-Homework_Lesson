# while True:
#     try:
#         a = int(input('Введите число A: '))
#         b = 10
#         c = b / a
#         print(f"Результат C = {c}")
#     except ValueError:
#         a, b = 1, 10
#         c = b / a
#         print("Вы ввели не число", c)
#     except ZeroDivisionError:
#         print("Вы ввели 0")
#         break
#     else:
#         print("Else")
#     finally:
#         print("Finaly")
# import datetime
#
# def write_logo(error):
#     with open("Logo.txt", "a") as file:
#         file.write(f"Error: {error} {datetime.datetime.now()}\n")
#
# while True:
#     try:
#         a = int(input("Введите число A: "))
#         b = 100
#         c = b / a
#         print(f"Результат C = {c}")
#     except ValueError as va:
#         write_logo(va)
#         a, b = 1, 10
#         c = b / a
#         print("Вы ввели не число!")
#     except ZeroDivisionError as zd:
#         write_logo(zd)
#         print("На ноль делить нельзя!")
#         break
#     else:
#         print("ELSE")
#     finally:
#         print("FINALLY")
class BuildingError(Exception):
    def __str__(self):
        return "Мала кількість матеріалів"

def checker_materials(material, limit):
    if material > limit:
        return "Починаємо будувати"
    else:
        raise BuildingError()

material = 1000
limit = 300

