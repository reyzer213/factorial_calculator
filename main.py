"""def factorial(n):

    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():

    try:
        num = int(input("Введіть ціле число: "))
        if num < 0:
            print("Факторіал визначений тільки для невід'ємних цілих чисел.")
        else:
            result = factorial(num)
            print("Факторіал числа", num, "дорівнює", result)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
"""
def factorial(n):

    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


number = 7
result = factorial(number)
print(f"Факторіал числа {number} дорівнює {result}")
