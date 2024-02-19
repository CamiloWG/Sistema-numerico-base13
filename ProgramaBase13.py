def sumar_en_base13(num1, num2, simbolos, base):

    len_max = max(len(num1), len(num2))
    num1 = num1.zfill(len_max)
    num2 = num2.zfill(len_max)
    acarreo = 0
    resultado = ''

    for i in range(len_max - 1, -1, -1):
        suma_temporal = simbolos.index(num1[i]) + simbolos.index(num2[i]) + acarreo
        resultado = simbolos[suma_temporal % base] + resultado
        acarreo = suma_temporal // base

    if acarreo:
        resultado = simbolos[acarreo] + resultado

    return resultado if resultado else '0'


def resta_en_base13(num1, num2, simbolos, base):

    len_max = max(len(num1), len(num2))
    num1 = num1.zfill(len_max)
    num2 = num2.zfill(len_max)
    acarreo = 0
    resultado = ''

    for d1, d2 in zip(num1[::-1], num2[::-1]):
        diff = (simbolos.index(d1) - simbolos.index(d2) - acarreo) % base
        resultado = simbolos[diff] + resultado
        acarreo = 1 if diff < 0 else 0

    return resultado if resultado else '0'


def multiplicar_en_base13(num1, num2, simbolos, base):

    def multiplicar_digito_en_base13(num, digito, posicion):
        resultado_parcial = ''
        acarreo = 0

        for i in range(len(num) - 1, -1, -1):
            producto = simbolos.index(num[i]) * simbolos.index(digito) + acarreo
            resultado_parcial = simbolos[producto % base] + resultado_parcial
            acarreo = producto // base

        if acarreo:
            resultado_parcial = simbolos[acarreo] + resultado_parcial

        return resultado_parcial + '0' * posicion

    resultado = '0'

    len_max = max(len(num1), len(num2))
    num1 = num1.zfill(len_max)
    num2 = num2.zfill(len_max)

    for i in range(len_max - 1, -1, -1):
        multiplicador = simbolos.index(num2[i])
        if multiplicador != 0:
            producto_parcial = multiplicar_digito_en_base13(num1, num2[i], len_max - 1 - i)
            resultado = sumar_en_base13(resultado, producto_parcial)

    return resultado

def divide_in_base_13(dividend, divisor, simbolos, base, precision=5):
    
    if divisor == '0':
        return '-1'
           
    resultado = ''
    acarreo = 0

    for digit in dividend:
        acarreo = acarreo * base + simbolos.index(digit)
        quotient_digit = 0

        while acarreo >= simbolos.index(divisor):
            acarreo -= simbolos.index(divisor)
            quotient_digit += 1

        resultado += simbolos[quotient_digit]

    if acarreo > 0:
        resultado += '.'
        for _ in range(precision):
            acarreo *= base
            quotient_digit = 0

            while acarreo >= simbolos.index(divisor):
                acarreo -= simbolos.index(divisor)
                quotient_digit += 1

            resultado += simbolos[quotient_digit]

    resultado = resultado.lstrip('0') or '0'

    return resultado


# Definición de variables
simbolos = '0123456789ABC'
base = 13

# Mostrar menú de operaciones
print("\nOperaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar al usuario la operación deseada
opcion = input('Selecciona el número de la operación deseada (1-4): ')

# Solicitar al usuario los números en base 13
num1_base13 = input('Ingresa el primer número en base 13: ')
num2_base13 = input('Ingresa el segundo número en base 13: ')

# Realizar la operación seleccionada y mostrar el resultado
try:
    if opcion == '1':
        resultado = sumar_en_base13(num1_base13, num2_base13, simbolos, base)
        print(f'Suma en base 13: {num1_base13} + {num2_base13} = {resultado}')
    elif opcion == '2':
        resultado = resta_en_base13(num1_base13, num2_base13, simbolos, base)
        print(f'Resta en base 13: {num1_base13} - {num2_base13} = {resultado}')
    elif opcion == '3':
        resultado = multiplicar_en_base13(num1_base13, num2_base13, simbolos, base)
        print(f'Multiplicación en base 13: {num1_base13} * {num2_base13} = {resultado}')
    elif opcion == '4':
        resultado = divide_in_base_13(num1_base13, num2_base13, simbolos, base)
        if resultado[0] == '.':
            resultado = '0' + resultado
        print(f'División en base 13: {num1_base13} / {num2_base13} = {resultado}') if resultado != '-1' else print('No se puede dividir entre 0!')
    else:
        print('Opción no válida')
except:
        print('Ingrese números en base 13 válidos!')
        