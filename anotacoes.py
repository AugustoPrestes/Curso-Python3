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
import sys

""" 
Obs: O underline pode ser utilizado para separar as centenas
    Exemplo: 1_000_000_000

Obs: Caso uma variavel global tenha o mesmo nome de uma local, a variavel local tera preferencia dentro do bloco aonde ela foi criada. Porem podemos utilizar a variavel global, informando dentro do bloco (global nome_da_variavel_global), nao sera criado uma nova variavel.
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

from collections import Counter
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
            and -> Corresponde ao E. ?? uma operacao logica que depende de dois valores, sendo que os dois precisam ser verdadeiro ou no caso True.
            or-> Corresponde ao OU. ?? uma operacao logica que depende de dois valores, sendo que apenas um deles precisa ser verdadeiro ou no caso True
            not-> Corresponde ao N??O (negacao). ?? uma operacao logica que nega o valor informado, de true para false e de false para true.
            is -> Corresponde ao ??. ?? usado para checar se duas variaveis possuem o mesmo Objeto.
                Exemplo:
                    x = ["apple", "banana", "cherry"]
                    y = ["apple", "banana", "cherry"]
                    print(x is y)

"""
#######################################################################################
"""
OBs: Utilizamos loops para iterar sobre sequencias ou valores iteraveis.
    Exemplo:
    - String -> nome = 'Augusto'
    - Lista -> cont = [1, 2, 3, 4]
    - range -> numeros = range(1, 100)
    
    # Nesse exemplo utilizamos o "Letra para separar o interavel", Podemos tamber utilizar o underline, quando nao queremos utilizar um "valor" como o indice nesse exemplo: 
        for indice, letra in enumerate(nome):
            print(letra)
        for _, letra in enumerate(nome):
            print(letra)

Obs: E necessario colocar um breack poin dentro do while para que nao gere um loop infinito


Aula 4 - Estrutura de repeticao
    # Modulo - Loop for.
        Exemplos de for:
            # Exemplo com String
            for letra in nome:
                print(f'letra do nome: {letra}')

            # Exemplo com Range()
            for numero in numeros:
                if numero == 50:
                    print(numero, ':Metade da conta')
                else:
                    print(numero)
                
            # Exemplo Com Lista 
            for numero in lista:
                if numero == 50:
                    print(numero, ':Metade da conta')
                else:
                    print(numero)   

        Loop e uma estrutura de repeticao.
            for - > Corresponde ao para, no sentido de iteravel

    # Modulo  - Range(). O range e uma funcao que auxilia a contrucao das estruturas de repeticao, com o range podes informar quantas vezes queremos que o codigo rode. 
        Exemplo: 
            range(valor_de_inicio, valor_de_parada, contador)

    # Modulo - Loop While.
        while -> O While corresponde a, enquanto e serve para que possamos iterar sobre sequencias, de forma booleana, considerando que enquanto a condicao for verdadeira o codigo continuara sendo executado.

    # Modulo - Saindo de loops com break. 
        break -> E utilizado para sair de um loop de maneira projetada

"""
#######################################################################################
"""
Obs: As Lista em python funcionam com array ou vetores. Com a diferenca de serem dinamicos e possamos incluir qualquer tipo de dados em um so array
Obs: Tambem e possivel juntar a listas, utilizando o sinal de mais criando uma nova lista, ou adicionando uma lista a outra com o extend()
Obs: A representacao inicial de uma tupla precisa ser feita com mais de um numero, para que o Python reconheca que, o mesmo e uma tupla, e nao e necessario representar de inicio os valores dentro de um parenteses, o Python fara isso automaticamente 
Obs: Todas as funcoes de manipulacao de lista nao funcionam em tuplas, devido sua caracteristica de ser imutavel.
Obs: E possivel concatenar Tuplas.
Obs: os Dicionarios nao sao indexados, o acesso e feito pelo valor da chave, ou o valor do conteudo
Obs: E interresante utilizar tuplas, como chaves de um dict, e as chaves NAO podem ser repetidas
Obs: O COunter te a ordenacao do counter e baseada na quantidade do iterado, de forma decrescente.

Aula 5 - Colecoes em Python.
    # Modulo - Listas - list.
        Lista -> E considerado dinamico por nao possuir limite de tamanho, o limite e a penas a memoria do computador. nao exites destincao dos dados ao inserilos na lista
            Exemplos de Listas:
                lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 31, 43, 65, 12]
                lista_str = ['Augusto', ' ', 'Ribeiro']
                lista_vaz = []
                lista_range = list(range(11))
                lista_str2 = list('Augusto Ribeiro')

        Funcoes para manipular as listas:
            sort() -> Funcao utilizada para ordenar a lista, normalmente urilizada para tratar numeros. Porem tbm e possivel utiliza-las com Strings.
                lista_num.sort()
            cont() -> Conta quantas vezes um determinado valor se repete dentro da lista.
                print(lista_num.count(valor_a_ser_contado))   
            append() -> Adiciona novo elemento a lista, Porem so e possivel adicionar um elemento por vez. Novo valor sempre sera mandado para o final da fila
                lista_num.append(1)
            extend() -> Adiciona novos elementos a lista, Porem nao possui limite de valores como o append e so aceita a insersao de mais de um valor por vez. Novo valor sempre sera mandado para o final da fila
                lista_num.extend([1, 2, 4, 5, 6, 00, 1, 3, 6])  
            insert() -> Adiciona um novo elemento a lista, Porem e possivel escolher o indice desse novo valor. E nao sera removido o valor anterior na possicao desejada
                lista_num.insert(index_da_lista, valor_a_ser_inserido)
            reverse() -> Invert a ordem da lista 
                lista_num.reverse()
            copy() -> Como o nome diz ele copia o valor da lista para outro lugar ou outra lista 
                lista_num = lista_test.copy()
            len() -> Len de length comprimento, para que possamos ver qual o tamanho total da lista, baseado na quantidade de elementos dentro da mesma.
                print(len(lista_num))
            pop() -> Deleta o ultimo valor inserido na lista, por padrao, porem e possivel escolher qual valor sera deletado informando o seu indice como paramentro.
                lista_num.pop()
            clear() -> Limpa todos os dados da lista de uma so vez. 
                lista_num.clear()
            split() -> Transforma String em uma lista, e por padrao separa os elementos considerando o espaco entre eles. Porem e possivel informal qual sera o parametro para a separacao dos elementos.
                nome = 'Augusto Ribiro Prestes da Silva'
                nome = nome.split()
            join() -> Transforma Uma lista em String. Informando se algo ficara entre cada elemento, para separar os elementos da lista dentro da string.
                nome = ['Augusto', 'Ribiro', 'Prestes', 'da', 'Silva']
                nome_string = ' '.join(nome)
            index() -> Informa o indice do valor que foi passado no parametro da funcao. Caso possua mais de um elemento com o mesmo valor, o index retorna o primeiro valor encontrado. E tambem e possivel buscar os indices em um
                print(lista_num.indes(valor_a_ser_procurado))
                print(lista_num.indes(valor_a_ser_procurado, indice_de_inicio, indice_de_parada)) # Busca em um range

        Operadores para manipular dados em listas. Para utilizar esses operadores, e necessario que a lista tenha apeas um tipo de dado, sendo eles, float ou int:
            sum -> Soma dos valores dentro da lista.
            max -> Valor maximo que a lista possui.
            min -> Valor minimo que a lista possui.
            len -> Quantidade de elementos que a lista possui.

        Desempacotamento de listas. E possivel fazer com quem os valores da lista sejam passados para variaveis externas, porem so e passado um valor para cada variavel, sendo assim, precisa ter a mesma quantidade de variaveis para a quantidade de elementos na lista
            lista = [1, 2, 3]
            num1, num2, num3 = lista1
        
        Tipos de copia de Lista
            Shallow Copy -> E quando uma lista recebe o valor copiado de outra lista, porem elas criam uma coneccao e sempre teram o mesmo valor.
                lista = [1, 2, 3]
                nova = lista
                nova.append(34) # A partir desse momento ambas as listas teram o mesmo valor.
            Deep Copy -> E quando uma lista recebe o valor copiado de outra lista, porem ambas permanecem independentes uma da outra.
                lista = [1, 2, 3]
                nova = lista.copy()

    # Modulo - Tuplas - tuple
        Tuple -> As Tuplas sao parecisas com as listas, e sua definicao e baseada na virgula e nao no parentese, as tuplas aceitam tipos diferentes de dados assim como as listas, Devemos utilizar as tuplas para colecoes que nao precisarame ter seus dados alterados suas diferencas sao:
            Exemplos:
                tupla1 = (1, 2, 3)
                tupla2 = 1, 2, 3
                tupla3 = 1,

            Primeira -> A representacao, pois em tuplas utilizamos parenteses;
            Segunda -> As tuplas sao imutaveis, isso quer dizer que ao criar uma tuplas seu valor nao ira sofrer alteracao, e qualquer tentativa de alteracao, ira criar uma nova tupla.

    # Modulo - Dicionarios - dict
        Dicionario -> Os dicionarios sao colecoes do tipo chave e valor, porem as chaves ficam explicitas no codigo e na hora de representalas separando a chave do valor utilizando dois pontos, ambas podem ser de qualquer tipo de dados e sao representados por chaves {} 
            Exemplos:
                paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
                paises = dict(br='Brasil', eua='Estados Unidos')
            
            Funcoes exclusivas em dict:
                values() -> Imprime apenas os valores do dict;
                clear() -> Limpar dados dentro do dict;
                copy() -> Copia os valores do dict, para outro local;   
                fromkeys() -> Cria um novo dict, passando como primeiro parametro umm iteravel a chave e como segundo parametro o valor para cada chave informada;
                keys() -> Imprime apenas as chaves de cada valor do dict;
                get() -> Seleciona e determinado valor da lista, pela chave que e passada no paramentro da funcao, e possivel passar um valor default, caso o valor informado nao seja encontrado;
                update() -> inseri um novo valor ao dict de uma variavel externa, que tenha valores compativeis com os parametros de 'key' = 'valor';             

            Para acessar os dados dentro de um dicionario, existem duas maneiras:
                Utilizando a chave do valor -> print(paises['br'])
                Utilizando a funcao get() -> print(paises.get('br'))  # A funcao get(), pode ser utilizada tbm para confirmar a existencia de um dado dentro do dict, pois caso o valor nao seja encontrado pela chave passada, sera retornado o valor none, e nao ocorrera um erro caso utilizemos a forma de busca a cima.

            Formas de inserir dados ou atualizalos em um dict:
                Exemplos:
                    Primeira forma-> Utilizando o proprio parametro de key do dict, informando o nome da nova key e o valor que ela vai receber;
                        receita['abr'] = 300.
                    Segunda forma -> Criando uma variavel que recebe um ou mais valores de um dict, e inserindo esses valores da variavel utilizando a funcao update(), OU apenas inserir os dados diretamente pelo update();
                        novo_dado = {'mai': 500}
                        receita.update(novo_dado)  #Com isso o dict de receita recebera o novo valor.
                        receita.update({'mai': 500})  #Outra forma de inserir dados com o update().

    # Modulo - Conjuntos - sets:
        sets -> Os conjuntos em Pytho estao fazendo referencia aos conjuntos da matematica.
            -> Nao podem ser duplicados;
            -> Nao podem ser ordenados;
            -> Nao podem ser acessados via indice;

        Diferenca entre Dicionarios e Conjuntos:
            -> Dicionario possui chave/valor;
            -> COnjunto possui apenas valor;

    # Modulo - Collections - Counter
        counter -> E necessario importa o counter de collection, ?? uma funcao utilizada para contar quantas vezes um valor se repete dentro de uma lista, pois recebe um interavel como parametro e cria um objeto contando quantas vezes cada valor dentro do interavel se repete.
            Exemplo:
                lista = [1, 1, 3, 5, 6, 7, 2, 2, 3, 4, 5, 6, 7, 8, 9, 12, 31, 43, 65, 12]
                res = Conter(lista)  # O retorno sera um objeto contendo a quantidade de vezes que cada elemento dentro da lista se repete.

            Funcoes utilizadas em Counter:
                 most_common() -> seloeciona os elementos em maior quantidade, e dentro do parametro informamos, quantos elementos deveram aparecer
                    Exemplo: 
                        from collections import Counter
                        texto = "Augusto Prestes"
                        palavras = list(texto)
                        res = Counter(palavras)
                        print(res)
                        print(res.most_common(10))
        
    # Modulo - Collections - Default Dict
        defaultdict -> Ao criar um dicionario utilizando a funcao defaultdict sempre que inserirmos uma nova chave sem valor, ou buscar-mos um valor e passar-mos uma chave que nao existe no dicionario, a funcao ira inclui-lo no automaticamente com o valor default informado.
            Exemplo:
                from collections import defaultdict
                dicionario = defeultdict(lambda: 0)
                dicionario['nome'] = 'Augusto'  # Incluindo um elemento de uma forma ja vista antes
                print(dicionario['outro'])  # Dessa forma pelo fato de que nao possui nenhuma chave que corresponde com 'outro', automaticamento o defeultdict ira inseri-lo a lista
                
    # Modulo - Collection - Ordered Dict
        ordereddict -> E uma ferramenta para ordenar um dicionario existente, porem aparentemente a funcao nao ordena de acordo com as chaves atuais, ou pelos valores ja inseridos, olhando rapidamente a documentacao e utilizado o OrderedDict, para criar uma propria maneira de ordenar a insersao de dados no dicionario
            exeplo do curso, porem nao funcionou como esperado:
                from collections import OrderedDict
                dicionario = OrderedDict({'a': 2, 'c': 1, 'b': 1, 'x': 0})
                for chave, valor in dicionario.items():
                    print(f'Chave {chave} e Valor {valor}')
                print(dicionario)
    
    # Modulo - Collection - Named Tuple
        NamedTuple -> As tuplas nomeadas atribuem significado a cada posi????o em uma tupla e permitem um c??digo mais leg??vel e autodocumentado. Eles podem ser usados ??????sempre que tuplas regulares s??o usadas e adicionam a capacidade de acessar campos por nome em vez de ??ndice de posi????o.
            Exemplo:
                from collections import namedtuple
                produto = namedtuple('Produto', ['nome', 'valor', 'tipo'])
                carrinho = produto(nome='playstation', valor=10000, tipo='eletronico')  # Assim Criamos o nosso tipo de dado chamado produto,
    # Modulo - Collection - Deque
        Deque -> E uma lista de alta performance, tem a mesma funcao do namedtuple na criacao da lista.
            Deque possui uma funcao chamada appendleft(), inseri o novo dado no inicio da lista/deque;
            Deque possui uma funcao chamada popleft(), remove o primeiro elemento da lista/deque;

"""
#######################################################################################
"""
Obs: Sempre crie funcoes de forma mais simples possiveis, facilitando a manutencao do codigo e a melhorando o desempenho do mesmo;
Obs: Toda funcao que ja e vem da linguagem e chama de built-in;
Obs: Parametros sao variaveis declaradas na definicao da funcao, ja argumentos sao dados passados durante a execucao da funcao;
Obs: Caso a funcao que utiliza o *Args receba uma lista tuplua ou dict, e possivel desempacotar os valores contidos nelas utilizando o *no no inicio da variavel detro do parametro da funcao  
Obs: Caso uma funcao necessite o uso de todos os tipos de parametro, devera seguir um padra: Parametros obrigatorio, *Args, Parametros default(nao obrigatorios) e **Kwargs.
Obs: O duplo * e utilizado para desempacotar uma variavel dentro dos parametros da funcao. Porem os nomes das chaves tem que ser o mesmo que consta na funcao

Aula 6 - Funcoes em Python:

    # Modulo - Definindo funoes:
        Definicao de funcoes -> Funcoes sao pequenos trechos de codigos que realizam tarefas especificas. Pode ou nao receber ou retornar dados. Sao uteis para executar procedimentos que se repetem ao longo do codigo.
        Exemplo: -> na definicao de funcao por padrao devemos utilizar o methodo Snake case, e a funcao deve ser com letras minusculas. Parametros de entrada sao opcionais, e sempre separar por virgula caso contenha mais de um.
            def nome_da_funcao(parametros_de_entrada):
                    bloco_da_funcao

    # Moduolo - Funcoes com Retorno:
        Retorno de funcao ->
            return -> A palavra reservada return que garante um retorno de dados para a noca funcao. E ela tambem sai da funcao.

    # Modulo - Funcoes com Parametros:
        Parametros de funcao -> Sao funcoes que recebem dados para ser processados dentro da propria funcao, 
        
    # Modulo - Funcoes com parametro padrao:
        Parametro padrao -> Sao funcoes que informar o parametro e opcional. Caso a funcao tenha a penas um valor default, ele deve estar ao final da declaracao!
            Exemplo:
            def func_raiz(numero, raiz=2):
                return numero ** raiz
    # Modulo - Docstrings 
        Docstrings -> Sao Strings de Documentacao, modulo para reforcar a importancia de documentar partes importantes do codigo Utilizado Para Documentar funcoes.
            Ela e executada com a funcao help, mostrando o que foi documentado dentro da funcao, para que possamos entender como a funcao criada funciona, formas de chamar a DocString:
                Exemplo:
                    help(funcao_criada());
                    print(funcao_criada.__doc__)
    # Modulo - *Args
        *Args -> E um parametro de entrada de uma funcao, isso significa que podemos nomealo de qualquer coisa, porem e necessario que comece com *. O parametro *args coloca os valores extras em uma tupla. Pode ser usado para que nao precise-mos informar uma quantidade limitada de parametros para nossa funcao.

    # Modulo - Entendendo **Kwargs
        E mais um parametro, porem ele exige que utilizemos parametros nomeados, e transforma os parametros extra em um dicioario. No caso Kwargs Sao argumentos que possuem chave de identificacao. 
     
    
"""
#######################################################################################
"""
Aula 7 - Comprehensions em Python - Parte 1:
    # Modulo - List Comprehensions (Uma das features mais poderosas da linguagem Python):
        List Comprehensions ->  Com essa feature e possivel gerar novas listas com dados processados a partir de outro iteravel.
            # Sintax: 
                [ calculo for dado in iteravel ] 
            Exemplos: 
                numeros = [1, 2, 3, 4, 5, 6]
                res = [numero * 10 for numero in numeros] # Dentro dessa Comprehensions e possivel realizar qualquer tipo de calculo, ou ate mesmo utilizar uma funcao dentro dessa lista
                print(res)
                
                # Resultado no console
                [10, 20, 30, 40, 50, 60]
    # modulo - List Aninhadas
        Em algumas linguagens de programacao possuem uma estrutura de dados chamada de arrays, porem em Python sao chamadas de listas:
            - Unidimensionais (Array/ Vetores);
            - Multidimensionais (Matrizes);
        Exemplos de Listas aninhadas:
            lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print(lista[0][0])  # Printando o elemento dentro da lista aninhada (valor a ser exibido sera o 1)
            print(lista[2][1])  # Printando o elemento dentro da lista aninhada (valor a ser exibido sera o 8)
            
        Exemplo de Iterando com loops em uma lista aninhada:
            for lista in listas:  # Iterando as listas dentro da lista;
                for num in lista:  # Iterando os numeros dentro das listas que estao dentro da lista;
                    print(num)
        Exemplo de Iterando com poops em lista aninhada utilizando list comprehension (O resultado sera o mesmo do exemplo acima):
            [[print(valor) for valor in lista] for lista in listas]
        
        Exemplo para gerar uma lista aninhada com range():
            tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
            print(tabuleiro)
            
    # modulo - Dictionary Compreension:
        Dicinary Comprehensions ->  Com essa feature e possivel gerar novas dicts com dados processados a partir de outro iteravel.
        
        Exemplo:
            numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
            quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
            print(quadrado)
            
        Exemplo para trasnformar qualquer tipo de conjuto de dados em dict utilizando o Compreesion (nesse exemplo utilizei uma lista:) 
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            quadrado = {valor: valor ** 2 for valor in numeros} 
            print(quadrado)
            
        Exemplo para misturar qualquer tipo de conjuto de dados em dict utilizando o Compreesion (nesse caso utilizei uma tupla e uma lista):
            chaves = 'abcdefghi'
            valores = [1, 2, 4, 5, 6, 7, 8, 9, 10]
            mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
            print(mistura)
            
        Exemplo utilizando logica condicional:
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
            print(res)
            
            numeros = {x: x ** 2 for x in range(10)}
            print(numeros)  
"""
#######################################################################################
"""
Obs: Para Remover o espa??amento antes e depois da string Caso seja inserido um espa??o indevido, e necess??rio utilizar a fun????o strip().
Obs: Assim como a funcao map a funcao filter recebe dois parametros
Obs: Os dados gerados na funcao map, filter, reduce, any, all e generator, so podem ser utilizados uma vez.
Obs: A Funcao sorted() possui parametros para reverter a ordem padrao (ascendente) e um parametro key, para personalizar
a ordem de classificacao

Aula 8 - Express??es Lambdas e Fun????es integradas:

    # Modulo - Utilizando Lambda:
        Lambdas sao funcoes que nao possuem nome, ou funcoes anonimas.
        
        Exemplo de uma Funcao em Lambda:
        func_lambda = lambda x: 3 * x + 1
        print(func_lambda(5))    
        
        Exemplo de funcao lambda com multiplas entradas:
        
        Exemplo de LAmbda em uma funcao sort():
        autores = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Franl Herbert", "Orson Scott Card",
           "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
        autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
        print(autores)

        Exemplo de lambda em uma funcao quadradita
        # f(x) = a * x ** 2 + b * x + c
        # Definindo a funcao Quadratica
        def quadratica(a, b, c):
            Retorna a funcao f(x) = a * x ** 2 + b * x + c
            return lambda x: a * x ** 2 + b * x + c
        teste = quadratica(3, 6, 9)  # A variavel teste esta recebendo o retorno da funcao lambda, por isso e necessario informar o valor de x dentro do teste
        print(teste(2))
        
    # Modulo - MAP:
        Com Map podemos mapear valores para func????o. MAP ?? uma funcao que recebe dois parametros (o primeiro valor e a funcao e o segundo o iteravel)
        A Funcao Map retorna valores se baseando na funcao criada que retorna valores (menos os valores booleanos)
        Exemplo:
            
            import math
            def area(r):
                return math.pi * (r ** 2)         
            raios = [2, 5, 0.3, 7.1, 10]
            areas = map(area, raios)
            print(list(areas))
            
    # Modulo - Filter:
        Utilizado para filtrar dados de uma determinada cole????o. sao utilizado dois parametros sendo uma funcao e um iteravel;
        A funcao filter retorna valores se baseando em resultados booleanos (True ou False)
        Utilizando Lambda no filter:
            import statistics as statis
            dados = [2.3, 5.6, 0.3, 7.1, 5.10, 9.0, -0.12]
            media = statis.mean(dados)
            res = filter(lambda x: x > media, dados )
            print(list(res))
            
        Utilizando o map() e o filter() juntos (foi utilizado o for apenas para o print sair mais bonito):
            nomes = ['Augusto', 'Maria', 'Ana', 'Vanessa', 'Beca']
            lista = list(map(lambda nome: f'O nome da pessoa e {nome}', filter(lambda nome: len(nome) >= 5, nomes)))
            for nome in lista:
                print(f'{nome}, o seu amigo')
                
    # Modulo - Reduce (funcao substituida pelo for, que e uma maneira mais clean)
        Funcao so pode ser utilizada a partir do modulo functools (import functools), para utilizar o reduce e necessario
        uma funcao que utiliza 2 parametros uma funcao e um iteravel:
        Exemplo:
            from functools import reduce
            dados = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            multi = lambda x, y: x * y
            res = reduce(multi, dados)
            print(res)
    # Modulo - Any e All:
        A funcao all() retorna True se todos os elementos do iteravel s??o verdadeiros ou ainda se o iteravel estiver vazio.
        Exemplo Utilizando list Compreesion:
            print(all([num for num in [2, 4, 6, 8, 10] if num % 2 == 0])) #resultado sera True devido aos resultados serem Par
            print(all([num for num in [2, 4, 6, 8, 10] if num % 2 == 1])) #resultado sera True devido aos resultados serem Impar e gerar uma lista vazia
            
        A funcao any() retorna True se qualquer elemento do iteravel for True, caso o iteravel estiver vazio retorna False
        Exemplo Utilizando list Compreesion:
            print(any([num for num in [2, 4, 6, 8, 10] if num % 2 == 0])) #resultado sera True devido que pelo menos 1 dos valores sera True
            print(any([num for num in [2, 4, 6, 8, 10] if num % 2 == 1])) #resultado sera False devido que o iteravel retornara vazio
            
    # modulo - Generator Expression:
        Os Generators sao parecidos com comprehensions porem utilizam os conchetes (), e o generator ao ser executado 
        ocupa menos recurso da memoria do computador, por armazenor um objeto e nao uma lista completa como o list comprehension
        Exemplo de iteravel em Generetor Expression:
        gen = (x * 10 for x in range(1000))
        print(gen)
        
        Utilizando a funcao getsizeof(), da biblioteca sys -> a funcao informao a quantidade de memoria que esta sendo
        utilizada pelo PC:
            # Gerando uma lista de numeros com list Comprehension:
            list_comp = sys.getsizeof([x * 10 for x in range(1000)]) # Utilizados 8856 bytes
            # Gerando uma lista de numeros com set Comprehension:
            set_comp = sys.getsizeof({x * 10 for x in range(1000)}) # Utilizados 32984 bytes
            # Gerando uma lista de numeros com Dictionary Comprehension:
            dic_comp = sys.getsizeof({x: x * 10 for x in range(1000)}) # Utilizados 36960 bytes
            # Gerando uma lista de numeros com Generator Expression :
            gen = sys.getsizeof(x * 10 for x in range(1000)) # Utilizados 104 bytes
            # Prints de demonstracao de ocupacao de memorias
            print("PAra fazermos a mesma tarefa gastamos:")
            print(f"list Comprehension: {list_comp} bytes")
            print(f"set Comprehension: {set_comp} bytes")
            print(f"Dictionary Comprehension: {dic_comp} bytes")
            print(f"Generator Expression: {gen} bytes")
    
    # modulo - Sorted:
        A funcao sorted() pode ser utilizada para ordenar qualquer tipo de iteravel, transformando em uma 
        lista ja ordenado (utilizando em um dictionary sera ordenado pela chave do dicionario).
        A diferenca da funcao sorted() para a sort() e que a funcao sort() altera a ordem daquela lista, e a sorted()
        gera uma lista nova
        Exemplo: 
            numeros_list = [1, 2, 5, 1, 3, 9, 10, 6, 8]
            numeros_tuple = (1, 2, 5, 1, 3, 9, 10, 6, 8)
            numeros_set = {1, 2, 5, 1, 3, 9, 10, 6, 8}
            numeros_dict = {"1": 1, "2": 2, "3": 5, "4": 1, "5": 3, "6": 9, "7": 10, "8": 6, "9": 8}
            
            print(f" lista crua: {numeros_list}")
            print(f" lista apos o sorted(){sorted(numeros_list)}\n")
            
            print(f" tupla crua: {numeros_tuple}")
            print(f" tupla apos o sorted: {sorted(numeros_tuple)}\n")
            
            print(f" set crua: {numeros_set}")
            print(f" set apos o sorted: {sorted(numeros_set)}\n")
            
            print(f" dict crua: {numeros_dict}")
            print(f" dict apos o sorted: {sorted(numeros_dict)}\n")
   
    # modulo - min e max:
        Como visto anteriormente sao funcoes que mostram o maior e o menor valor, porem se executados para strings,
        iram se basear na ordem alfabetica das letras.so e possivel verificar o tamanho da string se baseando em quantidade,
        caso seja alterado o parametro key= dentro das funcoes max e min.
        Exemplo:
            musicas =[
                {"titulo": "Thunderstruck", "tocou": 3},
                {"titulo": "senta no bugalu", "tocou": 100},
                {"titulo": "Pike", "tocou": 2200},
                {"titulo": "Foto do Corte", "tocou": 10000},
            ]
            
            print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
            print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

    # modulo - Reversed:
        A funcao reversed() pode ser utilizada para alterar todos os iteraveis, ao contrario da funcao reverse() que 
        altera apenas a lista. E retorna um iteravel chamado (List reverse Iterator)
        Podemos utilizalo para imprimir um loop for reverso
        Exemplo:
            for n in reversed(range(1, 10)):
                print(n)
                
    # modulo - len, abs, sum e round:
        A funcao len retorna o tamanho de um iteravel.
        A funcao abs retorna valor absoluto do numero real ou inteiro.
        A funcao sum retorna a soma de um iteravel ou de apenas mais de um numero.
        A funcao round retorna um numero aredondado para o numero inteiro mais proximo da entrada.
        
    # modulo - Zip:
        Cria um iteravel chamado zip object, ele agrega elemento de cada um dos iteraveis passados como entrada em pares
        Melhor maneira de juntar dus listas e organizalas como chave e valor, considerando a ordem de cada uma delas.
        Porem so funciona com dicionary, quando o zip possui apenas 2 iteraveis
        Exemplo (O resultado sera um dicionario, como chave os itens da lista1 e valor os itens da lista2):
            lista1 = [1, 2, 4]
            lista2 = [5, 6, 7]
            zip1 = zip(lista1, lista2)
            print(dict(zip1))            
"""
#######################################################################################
"""
Obs: Sempre procure tratar um erro de forma espec??fica.

Aula 9 - Debugando e Tratando erros:

    # Modulo - Erros mais comuns em Python:
        SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja, voce escreveu algo que o Python nao 
        reconhece como parte da linguagem;
        
        NameError -> Ocorre quando uma variavel ou funcao utilizada nao foi definida, ou estiver com o nome errado;
        
        TypeError -> Ocorre quando uma funcao, operacao ou acao e aplicada a um tipo errado de dados;
        
        IndexError -> Ocorre quando tentamos acessar um elemento em um tipo de dado indexado utilizando um index invalido;
        
        ValueError -> Ocorre quando uma funcao ou funcao integrada recebe um argumento com tipo correto, mas com o valor inapropriado;
        
        KeyError -> Ocorre quando queremos acessar um dicionario com uma chave q nao existe;
        
        AtributeError -> Ocorre quando uma variavel nao te um atributo ou funcao;
        
        IdentantionError -> Ocorre quando nao respeitamos a indentacao do Python de 4 espacos;
        
    # Modulo -  Levantando os proprio erros com raise:
        Raise lanca excecoes em uma funcao criada em nosso codigo. O raise funciona como o return, pois nada apos dele
        e executado.
        Exemplo de utilizacao do raise;
            raise TipoDoErro('Mensagem do erro')
        
        Exemplo Real:
        def colore(texto, cor):
            if type(texto) is not str:
                raise TypeError('Texto precisa ser uma string')
            if type(cor) is not str:
                raise TypeError('Cor precisa ser uma string')
            print(f"O texto '{texto}', sera impresso na cor {cor}")
        
        colore("AUgusto", "Azul")
        
    # Modulo - O bloco Try/Except:
        o bloco Try/Except utilizamos para tratar erros que podem ocorrer no nosso codigo. Previnindo que o programa pare de funcionar
        Devemo sempre tratar o erro de forma especifica, informando o tipo do erro junto do except. E possivel inserir
        diversos except no bloco para tratar mais de um tipo de erro.
        Exemplo mais simples:
            try:
                execucao problematica
            except:
                O que deve ser feito para corrigir o problema
        
        Exemplo 1 - tratando um erro generico
        try:
            geek()
        except:
            print('Ocorreu um erro aqui') 
             
        Exemplo 2 - tratando um erro especifica
        try:
            len(2)
        except TypeError as err: # Dando um apelido para o tipo do erro para que ele seja informado no log sem gerar erro no programa
            print(f'Ocorreu um erro aqui{err}')    
    
    # Modulo - Try / Except / Else / Finally:
        Devemos tratar os erros em todas as entradas de dados.
        Else -> E executado somente se nao ocorrer o erro
            Exemplo:
                try:
                    num = int(input("Informe um numero: "))
                except ValueError:
                    print('valor incorreto')
                else:
                    print(f"Seu numero foi {num}")
        
        Finally -> E sempre executado independente se o erro e gerado ou nao. Geralmente e utilizado para fechar ou 
        desalocar recursos:
            Exemplo:
                try:
                    num = int(input("Informe um numero: "))
                except ValueError:
                    print('valor incorreto')
                else:
                    print(f"Seu numero foi {num}")
                finally:
                    print("Finally passou por aqui")
        
        Exemplo Mais completo:
        def dividri(a, b):
            return a / b
        
        try:
            num1 = int(input("Informe um numero: "))
            num2 = int(input("Informe outro numero: "))
        
        except ValueError:
            print("O valor informado precisa ser um numero")
        
        else:
            print(dividri(num1, num2))
            
    # Modulo - Debugando codigo com PDB (Python Debug):
        Para Utilizar o PDB e necessario importar a biblioteca
        

"""

from pdb import set_trace



def dividri(a, b):
    return a / b

try:
    num1 = int(input("Informe um numero: "))
    num2 = int(input("Informe outro numero: "))

except ValueError:
    print("O valor informado precisa ser um numero")

else:
    print(dividri(65, 3))
