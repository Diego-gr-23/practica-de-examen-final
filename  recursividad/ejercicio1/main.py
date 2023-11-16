def finonacci(num: int):
    if num == 0 or num == 1:
        return num
    elif num > 1:
        return finonacci(num - 1) + finonacci(num - 2)


def main():
    n = int(input('Ingrese un numero'))
    print(finonacci(n))


main()
