arq_res = 'testes/n-digitos1.res'
arq_out = 'testes/n-digitos1.out'


res = []
out = []
diferenca = []
with open(arq_res) as arquivo:
    for linha in arquivo:
        res.append(linha)
with open(arq_out) as arquivo:
    for linha in arquivo:
        out.append(linha)        

for item in res:
    if item not in out:
        diferenca.append('res:')
        diferenca.append(item)
for item in out:
    if item not in res:
        diferenca.append('out:')
        diferenca.append(item)    
print(diferenca)            


