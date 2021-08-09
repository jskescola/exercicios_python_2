def main():
    preco = float(input('Digite o preço do produto: '))
    preco = preco - (preco * 5 / 100)

    print(f'O seu preço com desconto é {preco}.')

if __name__ == '__main__':
    main()
