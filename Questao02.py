def sequencia_fibonacci(numero):
    num1, num2 = 0, 1

    if numero == num1 or numero == num2:
        return True
    
    prox_num = num1 + num2

    while prox_num <= numero:
        if prox_num == numero:
            return True
        num1, num2 = num2, prox_num
        prox_num = num1 + num2
    return False

numero_informado = int(input('Digite um número para verificar se pertece a sequencia Fibonacci: '))

if sequencia_fibonacci(numero_informado):
    print('O número {} pertence a sequencia Fibonacci'.format(numero_informado))
else:
    print('O número {} não pertence a sequencia de Fibonacci'.format(numero_informado))