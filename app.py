'''ano = 0
mes = 0
dia = 0
user = int(input())
while user >= 365:
    user -= 365
    ano += 1
while user >= 30:
    user -=30
    mes += 1
dia = user

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
'''
'''numeroFuncionario = int(input())
horasTrabalhadas  = float(input())
valorPorHora = float(input())
salario = horasTrabalhadas * valorPorHora

print("NUMBER =", numeroFuncionario)
print(f"SALARY = U$ {salario:.2f}")'''
'''A, B, C = map(float, input().split())
area_triangulo = (A * C) / 2
area_circulo = 3.14159 * (C ** 2)
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")'''
'''a, b, c = map(int, input().split())
maior = (a+b+abs(a-b))/2
if c > maior:
    maior = c
print(f'{int(maior)} eh o maior')'''
'''from math import sqrt
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = sqrt(((x2 - x1)**2)+((y2 - y1)**2))
print(f'{distancia:.4f}')'''
'''distanciaTotal = int(input())
totalCombustivelG = float(input())
kmPh = distanciaTotal / totalCombustivelG
print(f'{kmPh:.3f} km/l')'''
'''nome = input()
salarioF = float(input())
vendas = float(input())
desconto = vendas * 0.15
total = salarioF + desconto
print(f'TOTAL = R$ {total:.2f}')'''
'''raio = float(input())
area = 3.14159*(raio**2)
print(f'A={area:.4f}')'''
'''A = int(input())
B = int(input())
soma = A + B
print(f'SOMA = {soma}')'''
'''x = int(input())
tempo = x * 2
print(f'{tempo} minutos')'''
'''n = 1000000
while n >= 1000000:
    n = float(input())
n = int(round(n * 100))
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
totCedulas, totMoedas, c = 0, 0, 1

print('NOTAS:')
for cedula in notas:
    while n >= notas[c-1]:
        n -= notas[c-1]
        totCedulas += 1
    print(f'{totCedulas} nota(s) de R$ {notas[c-1]/100:.2f}')
    if c < len(notas):
        c += 1
    totCedulas = 0
c = 1
print('MOEDAS:')
for moeda in moedas:
    while n >= moedas[c-1]:
        n -= moedas[c-1]
        totMoedas += 1
    print(f'{totMoedas} moeda(s) de R$ {moedas[c-1]/100:.2f}')
    if c < len(moedas):
        c += 1
    totMoedas = 0'''
'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
diferenca = a * b - c * d
print(f'DIFERENCA = {diferenca}')'''
'''lista = [1, 2, 3, 4]
lista = list(map(lambda x: x + 2, lista))
print(lista)'''
'''v1 = int(input())
v2 = int(input())
prod = v1 * v2
print(f'PROD = {prod}')'''
'''a, A = float(input()), 3.5
b, B = float(input()), 7.5
media = ((A * a) + (B * b)) / 11
print(f'MEDIA = {media:.5f}')'''
'''cp1, np1, vu1 = map(float, input().split())
cp2, np2, vu2 = map(float, input().split())
valor = (np1 * vu1) + (np2 * vu2)
print(f'VALOR A PAGAR: R$ {valor:.2f}')'''
'''a = float(input())
b = float(input())
c = float(input())
media = ((a * 2) + (b * 3) + (c * 5)) / 10
print(f'MEDIA = {media:.1f}')'''
'''raio = float(input())
volume = (4/3) * 3.14159 * (raio ** 3)
print(f'VOLUME = {volume:.3f}')'''
'''tempoViagem = int(input())
velocidadeMedia = int(input())
distancia = tempoViagem * velocidadeMedia
litrosNecessarios = distancia / 12
print(f'{litrosNecessarios:.3f}')'''
'''valor = 1000000"
while valor >= 1000000:
    valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(valor)
c = 0
for cedula in notas:
    while valor >= cedula:
        valor -= cedula
        c += 1
    print(f'{c} nota(s) de R$ {cedula:.0f},00')
    c = 0'''
'''n = int(input())
tempos = [3600, 60, 1]
lista = []
cont = 0
for tempo in tempos:
    while n >= tempo:
        n -= tempo
        cont += 1
    lista.append(cont)
    cont = 0
print(f'{lista[0]}:{lista[1]}:{lista[2]}')'''
'''n = int(input())
tempos = [3600, 60, 1]
resultado = []

for tempo in tempos:
    resultado.append(n // tempo)  # Calcula a quantidade de unidades
    n %= tempo  # Atualiza o restante dos segundos

print(f'{resultado[0]:02}:{resultado[1]:02}:{resultado[2]:02}')'''
'''a, b, c, d = map(int, input().split())
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')'''
'''from math import sqrt
a, b, c = map(float, input().split())
if a <= 0 or (b**2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else: 
    r1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    r2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')'''
'''user = float(input())

lista =  [[0,25], [25,50], [50,75], [75,100]]
if user > 100 or user < 0:
    print('Fora de intervalo')
else:
    for valor in lista:
        if user <= valor[1] and valor[1] == 25:
            print(f'Intervalo {valor[0]},{valor[1]}')
            break
        elif valor[0] >= 25:
            if user <= valor[1]:
                print(f'Intervalo ({valor[0]},{valor[1]}]')
                break'''
'''codigo, quantidade = map(int, input().split())
lanches = {1: 4, 2: 4.50, 3: 5, 4: 2, 5: 1.50}
escolha = lanches[codigo]
tot = escolha * quantidade
print(f'Total: R$ {tot:.2f}')'''
'''a, b, c, d = map(float, input().split())
pesos = [2, 3, 4, 1]
media = (2*a + 3*b + 4*c + d) / (sum(pesos))
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em exame.')
    notaExame = float(input())
    print(f'Nota do exame: {notaExame:.1f}')
    novaNota = (notaExame + media) / 2
    if novaNota >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {novaNota:.1f}')
    elif novaNota < 5:
        print('Aluno reprovado.')
        print(f'Media final: {novaNota:.1f}')'''
'''x, y = map(float, input().split())
if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')'''
'''a, b, c = map(int, input().split())
lista = [a, b, c]
listad = sorted(lista)
for elemento in listad:
    print(elemento)
print('')
for elemento in lista:
    print(elemento)'''
'''a, b, c = map(float, input().split())
lista = [a, b, c]
maiorNumero = max(lista)
lista.remove(maiorNumero)
if sum(lista) > maiorNumero or a == b == maiorNumero:
    perimetro = sum(lista) + maiorNumero
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a + b) * c / 2
    print(f'Area = {area:.1f}')'''
