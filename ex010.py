real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.92
print('Com R${:.2F} você pode comprar US${:.2F}'.format(real, dolar))
