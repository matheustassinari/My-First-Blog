
def comp(b,a):
    if b > a:
        print("b é maior que a")
    #posso adicionar quantos elif´s desejar, que o python ira executar todos em ordem
    elif b == a:
        print('b é igual a')
    else:
        print('b não é maior que a')

valores_a = [1, 53, 86, 600, 75, 83, 56, 22, 51, 515, 7684, 8521, 157, 0]
for valor_a in valores_a:
    comp(70, valor_a)
    print('Próxima')