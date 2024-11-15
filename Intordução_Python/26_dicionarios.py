
pessoa = { 'nome': 'Diego Carvalho', 'idade': 37, 'cep': '1235456567' }
    
pessoa['nome'] = 'Marcos'

print(pessoa)

#########################################################################

x = { 'nomes': [], 'idade': [] }

x ['nomes'].append('Diego Carvalho')

x ['idade'].append(37)

print(x['nomes'][0])

print(x['idade'][0])

##########################################################################

pessoas = [
    
           {'nome': 'Diego', 'idade': 21, 'altura': 180},
           {'nome': 'Michele', 'idade': 21, 'altura': 180},
           {'nome': 'Derick', 'idade': 21, 'altura': 180},

                                                        ]

for i in pessoas:
    print(i['nome'])