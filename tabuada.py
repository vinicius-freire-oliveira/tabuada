n = int(input('Digite um número: '))

# Loop que itera de 1 a 10 para calcular e imprimir a tabuada do número fornecido
for c in range(1, 11):
    # Calcula o resultado da multiplicação e imprime no formato "número x multiplicador = resultado"
    print('{} x {} = {}'.format(n, c, n * c))
