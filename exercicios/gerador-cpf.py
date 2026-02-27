import random
import sys
#Primeiro Digito

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

cont_regressivo_1 = 10
resultado_digito_1 = 0

# Percorre os dígitos calculando a soma ponderada
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1

# Cálculo do primeiro dígito verificador
digito_1 = (resultado_digito_1 * 10) % 11

# Aplica a regra: se o resto for > 9, vira 0
if digito_1 <= 9:
    digito_1 = digito_1
else:
    digito_1 = 0

print(f'Primeiro digito é {digito_1}')
print('-'*20)


#Segundo Digito

dez_digitos = nove_digitos + str(digito_1)
cont_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * cont_regressivo_2
    cont_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11

if digito_2 >= 9:
    digito_2 = 0
else:
    digito_2 = digito_2

print(f'Segundo digito é {digito_2}')

cpf_gerado_calculo = f"{nove_digitos}{digito_1}{digito_2}"

print('-'*20)
print(cpf_gerado_calculo)
print('-'*20)