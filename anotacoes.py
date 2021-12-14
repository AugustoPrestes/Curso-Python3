"""
Area Para anotacoes do Curso de Python da Geek University

Aula 1 - Recebendo dados do Usuario

# Para inprimir dados que estao em uma variavel e necessario utilizar %s, e apartir de duas variaveis e necessario inclui-las dentro de um parentese. (metodo antigo de printar informacoes)
Exemplo:
# Entrada de Dados do Sistema:
print("Favor Informar Seu Nome!")
nome = input()

print('Seja Bem-Vindo %s, informe sua idade' % nome)
idade = input()

# Saida dos Dados:
print('O %s Tem %s anos!' % (nome, idade))

---------------------------------------------------------------------------------------

# Para imprir dados que estao em uma variavel e necessario utulizar {numeroDaOrdem} no local aonde a variavel precisa aparecer, e .format(variavel) para informar qual variavel precisa ser formatada, a ordem corresponde a ordem que colocamos as variaveis dentro do print (metodo mais moderno)
Exemplo:
# Entrada de Dados do Sistema:
print("Favor Informar Seu Nome!")
nome = input()

print('Seja Bem-Vindo {0}, informe sua idade' .format(nome))
idade = input()

# Saida dos Dados:
print('O {0} Tem {1} anos!'.format(nome, idade))

---------------------------------------------------------------------------------------

# Para imprir dados que estao em uma variavel e necessario utulizar f'Texto {NomeDaVariavel}' no local aonde a variavel precisa aparecer(metodo mais moderno Ainda)
Exemplo:
# Entrada de Dados do Sistema:
print(f"Favor Informar Seu Nome!")
nome = input()

print(f'Seja Bem-Vindo {nome}, informe sua idade')
idade = input()

# Saida dos Dados:
print(f'O {nome} Tem {idade} anos!')

---------------------------------------------------------------------------------------

# Por padrao todo dado recebido por input sera reconhecido como String

Exemplos da Aula:

# Entrada de Dados do Sistema:
nome = input('Qual Seu nome: ')
idade = input('Informe sua idade: ')

# Saida dos Dados:
print(f'O {nome} Ribeiro Prestes da Silva Tem {idade} anos! E Nasceu no ano de {2021 - int(idade)}')


"""
#######################################################################################
""" 
Obs: O underline pode ser utilizado para separar as centenas
    Exemplo: 1_000_000_000

Obs: Pelo fato do Python ser uma linguagem de tipagem dinamica, nao precisamos colocar o tipo da variavel ao declara-la. O tipo e declarado ao atribuirmos o valor a variavel.

Aula 2 Variaveis e tipo de dados.
# Modulo tipo numerico
    soma : 1 + 1
    subtracao : 1 - 1
    multiplicacao : 1 * 1
    divisao : 1 /1
    divisao com resultadado de inteiro : 1 // 1 
    divisao para saber o resto da operacao : 1 % 1 
    potencia : 1 ** 1 

# Modulo tipo float. Float e um tipo dado para os numeros reais
    Exemplo:
        1.5
        2.3 

# Modulo tipo booleano. Boleano e um tipo de dado que consiste em duas constantes sendo elas verdadeiro ou falso, O valor sempre tem que ser descrito com a primeira letra maiuscula.
    Exemplo:
        True -> Verdadeiro
        False -> Falso

        # Operacoes basicas

            # NOT e uma operacao binaria, que inverte o resultado do valor recebido, se o valor for verdadeiro o resultado sera falso, e se o valor for falso o resultado sera verdadeiro
            ou seja sempre o valor sera ao contrario. 
            
            # Dentro do (not) e possivel negar a negacao dele com o (not) antes:
                Exemplo:
                    status = True

                    if status == True:
                        ativo = 'Ligado'
                    else: 
                        ativo = 'Desligado'

                    print(f'Agora o Computador esta {ativo}')

                    print(f'O Computador esta ligado na Fonte? {not not status}') #Aqui o NOT Nega a negacao no proximo NOT

            # OR e uma operacao binaria, que depende de dois valores, sendo que um deles precisa ser verdadeiro ou True.

            # AND e uma operacao binaria, que depende de dois valorees, ao contrario do OR o AND precisa que os dois valores sejam verdadeiros ou True

# Modulo tipo String. Em Python um dado e considerado String sempre que estiver entre aspas.
    Exemplo: 
        Aspas Simple -> ''
        Aspas Duplas -> ""
        Aspas Simples Triplas -> ''' '''
        Aspas duplas Triplas -> """ """

    # E utilizado na programacao o \n para pular a linha 
        Exemplo:
            print(f'meu nome e Augusto \n tenho 22 anos')
    
    # Para Acessar uma parte especifica da Sting e possivel utilizar o Colchetes [] e dentro dele infor a posicao que quer acessar ou o raio de acesso que quer acessar
        Exemplo:
            print(nome[0]) #Para acessar uma unica posicao dentro da String selecionada
            Slice de String -> print(nome[0:10]) # Para acessar um raio de possicoes dentro da String selecionada, nesse caso o ultimo numero selecionado sera um numero anterior ao informado na segunda posicao dentro do Colchetes
            Inverter a ordem da String -> print(nome[::-1]) # Para inverter a ordem das String e necessario utilizar esses sinais, que informam que vc quer que comece pelo ultimo va ate o primeiro mostrando de 1 
            Alterar String -> print(nome.replace('a', 'g')) # Para trocar as Strings informando a String antiga pela nova String. 
    
    # Funcoes para String:
        .split() -> Funcao utilizada para transformar trasnforma em uma lista de string com base no espaco que foi dado nas palavras ou letras ao introduzir no sistema 
            Tambem e posivel acessar a posicao de uma palavar Splitada pelo .split() utilizando o Colchetes [] e dentro o numero da posicao.

# Modulo de Escopo de variaveis.
    #Escopo de variaveis e a limitacao de uma variavel no caso, e aonde ela sera reconhecida dentro do programa:

    1 - Escopo das variaveis Globais:
        O escopo para essas variaveis se extende por todo o programa;

    2 - Escopo das Variaveis locais:
        O escopo para essas variaveis se extende apenas ao bloco aonde foram declaradas;

    # Para declarar uma variavel fazemos apenas:
        Exemplo:
            nome_da_variavel = valor_da_variavel 

"""
#######################################################################################
"""
Aula 3 - Estruturas logicas e condicionais:

    # Modulo - if, elif e else.

        Estruturas Condicionasis:
            If -> Corresponde ao Se.
                Exemplo: Se caso acontecer faca essa coisa.
            Elif -> Corresponde ao Senao Se, e uma juncao do if com o else tornando se mais uma opcao de entrada dentro da estrutura condicional, e sempre sera usado caso presice de uma nova condicao.
                Exemplo: Se nao entrar no if, faca essa coisa 
            ELse ->  Corresponde ao Senao.
                Exemplo: Se nao entrar no if ou no elif (que sempre vem antes do else na estrutura condicional), faca outra coisa.

    # Modulo - and, or, not e is.

        Estruturas Logicas:
            and -> Corresponde ao E. É uma operacao logica que depende de dois valores, sendo que os dois precisam ser verdadeiro ou no caso True.
            or-> Corresponde ao OU. É uma operacao logica que depende de dois valores, sendo que apenas um deles precisa ser verdadeiro ou no caso True
            not-> Corresponde ao NÃO (negacao). É uma operacao logica que nega o valor informado, de true para false e de false para true.
            is -> Corresponde ao É. É usado para checar se duas variaveis possuem o mesmo Objeto.
                Exemplo:
                    x = ["apple", "banana", "cherry"]
                    y = ["apple", "banana", "cherry"]
                    print(x is y)

"""