def main():
    quant_dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
    quant_km = float(input('Digite a quantidade de KMs percorridos: '))

    preco = (quant_dias * 60) + (quant_km * 0.15)

    print(f'O preço a pagar é: {preco}')

if __name__ == '__main__':
    main()