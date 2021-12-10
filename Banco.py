import mysql.connector
from mysql.connector import errorcode

########## EXECUTAR ANTES DE TESTAR ##########
# CREATE DATABASE IF NOT EXISTS bd_livro;
# USE bd_livro;
# CREATE TABLE IF NOT EXISTS livros(
#     idLivro int primary key unique not null,
#     titulo text,
#     autor text,
#     editoria text,
#     ano int
# );

class Banco():
    
    def __init__(self):
        self.conexao = mysql.connector.connect(host='HOST_AQUI', user='USER_AQUI', password='PASSWORD_AQUI', database='bd_livro')
            


