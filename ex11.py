def main():
    def conversor(value):
        return value / 5.30

    valor_reais = float(input('Digite um valor em reais.\n'))
    valor_convertido = round(conversor(valor_reais), 2)

    if not valor_reais <= 0:
        print(f'Você pode comprar ${valor_convertido} por {valor_reais}R$')
    else:
        print('Você não consegue comprar doláres com esse valor!')

if __name__ == "__main__":
    main()