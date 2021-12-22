nome = 'Felipe'
idade = 35
altura = 1.73
peso = 71.0
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome}, {idade} anos, nascido em {ano_nascimento}, com {altura:.2f}m de altura e {peso:.1f}kg, apresenta IMC '
      f'total de {imc:.2f}')
