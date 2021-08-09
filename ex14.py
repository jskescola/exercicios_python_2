def main():
    salario = float(input('Digite o seu salário: '))
    salario = salario + (salario * 15 / 100)

    print(f'O seu novo salário é {salario}.')

if __name__ == '__main__':
    main()
