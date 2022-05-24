import sqlite3
from contextlib import closing

nome_arquivo = 'Base_date_agenda.db'

try:
    # Verificar se o arquivo existe
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        pass
except:
    # Caso o arquivo não exista, então criar
    with sqlite3.connect('Base_date_agenda.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(""" create table contatos(
            id integer primary key autoincrement,
            nome text,
            telefone text)
            """)


def pede_nome():
    return input('Nome: ')


def pede_telefone():
    return input('Telefone: ')


def mostra_dados(nome, telefone):
    print(f'Nome: {nome} -> Telefone: {telefone}')


def pesquisa(nome):
    mnome = nome
    with sqlite3.connect('Base_date_agenda.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('select * from contatos where nome = ?', (mnome,))
            agenda = cursor.fetchone()
            if agenda:
                return agenda
            else:
                return None


def altera():
    contato = pesquisa(pede_nome())
    if contato is not None:
        nome = contato[1]
        telefone = contato[2]
        print('Encontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        with sqlite3.connect('Base_date_agenda.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute("update contatos set nome = ?, telefone = ? where nome = ? and telefone = ?", (nome, telefone, contato[1], contato[2]))
                conexao.commit()
    else:
        print('Nome não encontrado.')


def novo():
    nome = pede_nome()
    telefone = pede_telefone()
    grava(nome, telefone)


def apaga():
    nome = pede_nome()
    contato = pesquisa(nome)
    if contato is not None:
        with sqlite3.connect('Base_date_agenda.db') as conexao:
            with closing(conexao.cursor()) as cursor:
                cursor.execute("""delete from contatos
                where nome = ? and telefone = ?""", (contato[1],contato[2]))
    else:
        print('Nome não encontrado.')


def lista():
    print('\nAgenda\nn------------------------------')
    with sqlite3.connect('Base_date_agenda.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('select * from contatos')
            contatos = cursor.fetchall()
            for contato in contatos:
                print(f'Nome: {contato[1]} -> Telefone: {contato[2]}')


def grava(nome, telefone):
    with sqlite3.connect('Base_date_agenda.db') as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute('insert into contatos(nome, telefone) values(?, ?)', (nome, telefone))
            conexao.commit()


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor and valor <= fim:
                return valor
            else:
                print(f'Valor inválido, favor digitar entre {inicio} e {fim}')
        except:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')


def menu():
    print('''
    1 - Novo
    2 - Alterar
    3 - Apagar
    4 - Listar


    0 - Sair
    ''')
    return valida_faixa_inteiro('Escolha uma opcao: ', 0, 4)


while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()