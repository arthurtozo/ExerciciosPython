larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {área}m².')
tinta = área / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')