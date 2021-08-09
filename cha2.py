from datetime import date
import random

class Boleto:
    def __init__(self, banco='341-7', value=0, date=date.today().strftime('%d%m%Y')):
        self._banco = banco
        self._random = random.randint(1000,10000)
        self._date = date
        self._value = value

    def gen_boleto(self):
        return f'{self._banco} | {self._random}{self._date}{"0"*8}{self._value}'

if __name__ == '__main__':
    banco = input('Digite o número do banco: ')
    valor = int(input('Digite o valor da compra: '))
    boleto = Boleto(banco=banco, value=valor)

    print(boleto.gen_boleto())