import sqlite3
from contextlib import closing

nome = 'cruz'
telefone = '1478-1918'
with sqlite3.connect('teste.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("delete from contatos where nome = ?", (nome,))
        conexao.commit()
