def tabla():
    for i in range(5):
        print(i+1, end=' ')
        for j in range(4):
            valor = (i+1)**j
            print(valor, end=' ')
        print()


if __name__ == '__main__':
    tabla()