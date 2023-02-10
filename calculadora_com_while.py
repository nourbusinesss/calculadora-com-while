""" Calculadora com while """
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    
    try:
        nume_1_float = float(numero_1)
        nume_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None    

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos')    
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
