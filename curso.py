faturamento = 1000
custos = 710
novas_vendas  = 300
faturamento = faturamento + novas_vendas
taxa_imposto = 0.1 #representar fração
imposto = taxa_imposto * faturamento
mensagem = 'o faturamento foi de: '

print('faturamento', faturamento)
print ('custos', custos)
print('lucro', faturamento  - custos - imposto)
print(mensagem, faturamento)

#aqui é basicamente manipulação de var