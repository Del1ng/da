#1.
# def main():
#     name = input("Введите ваше имя: ")
#     while True:
#         try:
#             age = int(input("Введите ваш возраст: "))
#             if age < 18 or age > 130:
#                 raise ValueError("Что вы ток что написали?")
#             print(f"Привет,{name}!")
#             print(f"Ваш возраст  {age}")
#             break
#         except ValueError as e:
#             print(f"Ошибка: {e}. Пожалуйста, введите корректный возраст.")
#
# if __name__ == "__main__":
#     main()

#3.
def main():
    numbers = []

    while True:
        try:
            num = int(input("Введите  число: "))
            if num < 0:
                raise ValueError("Введенное число не может быть отрицательным.")
            numbers.append(num)
        except ValueError as e:
            print(f"Ошибка: {e}")
            break

    if numbers:
        print(f"Сумма чисел: {sum(numbers)}")
    else:
        print("Список чисел пуст.")


if __name__ == "__main__":
    main()
