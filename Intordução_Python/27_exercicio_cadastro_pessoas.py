#faça um programa que o usuario possa cadastrar n pessoas 
#armazenando seu nome, idade e altura.

pessoas = []

while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
    if decisao == 2:
        break

    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    altura = input('Digite a altura: ')

    pessoa = {'nome': nome, 'idade': idade, 'altura': altura}

    pessoas.append(pessoa)

    print(pessoas)