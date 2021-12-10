from Banco import Banco

class Livro(object):

    def __init__(self, codigo = "", titulo = "", autor = "", editoria = "", ano = ""):
        #self.livros = [] 
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.editoria = editoria
        self.ano = ano


    def insertLivro(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into livros (idLivro,titulo,autor,editoria,ano) values (" + self.codigo + ", '" + self.titulo + "', '" + self.autor + "', '" + self.editoria + "', '" + self.ano + "' )")

            banco.conexao.commit()
            c.close()

            return "Livro salvo com sucesso!";    
        except:
            return "Ocorreu um erro no cadastro do livro!" 

    def updateLivro(self):
    
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("update livros set titulo = '" + self.titulo + "', autor = '" + self.autor + "', editoria = '" + self.editoria + "', ano = " + self.ano + " where idLivro = " + self.codigo + " ")

            banco.conexao.commit()
            c.close()

            return "Livro atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do livro!"

    def deleteLivro(self, codigoLv):
    
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("delete from livros where idLivro = " + codigoLv + " ")

            banco.conexao.commit()
            c.close()

            return "Livro excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do livro!"
        
    
    def buscaLivro(self, codigoLv):
    
        banco = Banco()

        try:

            c = banco.conexao.cursor()
            c.execute("select * from livros where idLivro = " + codigoLv + "  ")
            
            row = c.fetchall()
            #VERIFICA SE TEM RETORNO
            if len(row) == 0 :
                self.codigo = ""
                self.titulo = ""
                self.autor = ""
                self.editoria = ""
                self.ano = ""
                return "Código não encontrado!"
            else:
                for linha in row:
                    self.codigo = linha[0]
                    self.titulo = linha[1]
                    self.autor = linha[2]
                    self.editoria = linha[3]
                    self.ano = linha[4]
                    c.close()
                return ""
        except:
            self.codigo = ""
            self.titulo = ""
            self.autor = ""
            self.editoria = ""
            self.ano = ""
            return "Código não encontrado"






        
