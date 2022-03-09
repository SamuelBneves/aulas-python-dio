a = int(input('Entre com um valor: '))
for num in range(a+1):

    div = 0
    for x in range(1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)





# a = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo' .format(a))
# else:
#     print('Número {} não é primo' .format(a))