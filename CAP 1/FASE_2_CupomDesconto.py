#solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o cupom de desconto: ")
#realizando o teste lógico com o cupom em maiúsculas caso usuario digite em minusculo
#if cupom == "NIVER10" or cupum == 'niver10: OUTRA OPÇÃO

if cupom.upper() == "NIVER10":
    #cálculo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
#exibindo o valor final da compra
print("O valor final da compra é {}".format(valor_final))