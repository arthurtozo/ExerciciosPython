n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print(f"{n} x {1:2} = {n*1}\n"
      f"{n} x {2:2} = {n*2}\n"
      f"{n} x {3:2} = {n*3}\n"
      f"{n} x {4:2} = {n*4}\n"
      f'{n} x {5:2} = {n*5}\n'
      f"{n} x {6:2} = {n*6}\n"
      f'{n} x {7:2} = {n*7}\n'
      f'{n} x {8:2} = {n*8}\n'
      f'{n} x {9:2} = {n*9}\n'
      f'{n} x {10:2} = {n*10}')
print('-' * 12)

#Outro Exemplo
print('{} x {:2} = {}'.format(n, 1, n*1))