def main():
    largura = float(input('(EM METROS)\nDigite o valor da largura: '))
    altura = float(input('(EM METROS)\nDigite o valor da altura: '))

    def area(largura, altura):
        return largura * altura

    def tinta(area):
        return area / 2

    area = area(largura, altura)
    tinta = tinta(area) 

    print(f'O valor da área dessa parede é {area}m²\nA quantidade de litros de tinta para pintar essa parede é {tinta}{"l" if tinta > 1 else "ml"}')

if __name__ == '__main__':
    main()