# !ANTES DE EXECUTAR! -> (CMD) pip install mysql-connector-python==8.0.13 
# LIGAR SERVIDOR MYSQL

from Livros import Livro
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Cadastro de Livros :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblcodigo = Label(self.container2,
        text="Código:", font=self.fonte, width=10)
        self.lblcodigo.pack(side=LEFT)

        self.txtcodigo = Entry(self.container2)
        self.txtcodigo["width"] = 10
        self.txtcodigo["font"] = self.fonte
        self.txtcodigo.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarLivro
        self.btnBuscar.pack(side=RIGHT)

        self.lbltituloLv = Label(self.container3, text="Titulo:",
        font=self.fonte, width=10)
        self.lbltituloLv.pack(side=LEFT)

        self.txttituloLv = Entry(self.container3)
        self.txttituloLv["width"] = 25
        self.txttituloLv["font"] = self.fonte
        self.txttituloLv.pack(side=LEFT)

        self.lblautor = Label(self.container4, text="Autor:",
        font=self.fonte, width=10)
        self.lblautor.pack(side=LEFT)

        self.txtautor = Entry(self.container4)
        self.txtautor["width"] = 25
        self.txtautor["font"] = self.fonte
        self.txtautor.pack(side=LEFT)

        self.lbleditoria= Label(self.container5, text="Editoria:",
        font=self.fonte, width=10)
        self.lbleditoria.pack(side=LEFT)

        self.txteditoria = Entry(self.container5)
        self.txteditoria["width"] = 25
        self.txteditoria["font"] = self.fonte
        self.txteditoria.pack(side=LEFT)

        self.lblano= Label(self.container6, text="Ano:",
        font=self.fonte, width=10)
        self.lblano.pack(side=LEFT)

        self.txtano = Entry(self.container6)
        self.txtano["width"] = 10
        self.txtano["font"] = self.fonte
        self.txtano.pack(side=LEFT)


        self.btnSalvar = Button(self.container8, text="Salvar",
        font=self.fonte, width=12)
        self.btnSalvar["command"] = self.salvaLivro
        self.btnSalvar.pack (side=LEFT)


        self.btnLimpar = Button(self.container8, text="limpar",
        font=self.fonte, width=12)
        self.btnLimpar["command"] = self.limpaCampos
        self.btnLimpar.pack(side=LEFT)


        self.btnExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluiLivro
        self.btnExcluir.pack(side=LEFT)

        self.btnAtualizar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.btnAtualizar["command"] = self.atualizaLivro
        self.btnAtualizar.pack(side=RIGHT)




        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()



    def salvaLivro(self):

        #Valida dados
        codigo = self.txtcodigo.get().strip()
        titulo = self.txttituloLv.get().strip()
        autor = self.txtautor.get().strip()
        editoria = self.txteditoria.get().strip()
        ano = self.txtano.get().strip()

        if(codigo == "" or titulo == "" or autor == "" or editoria == "" or ano == ""):
            self.lblmsg["text"] = "Todos os campos são obrigatórios!"
            return
        else:
            try:
                ano = int(ano)
                if ano <= 0:
                    self.lblmsg["text"] = "Ano inválido!"
                    return 
                else:
                    ano = str(ano) #a class espera receber uma string no parametro
            except:
                self.lblmsg["text"] = "Informe um ano válido!"
                return 

        #define parametros
        livro.codigo = codigo
        livro.titulo = titulo
        livro.autor = autor
        livro.editoria = editoria
        livro.ano = ano

        #chama metodo e atribui retorno
        self.lblmsg["text"] = livro.insertLivro()

        #limpa campos
        self.txtcodigo.delete(0, END)
        self.txttituloLv.delete(0, END)
        self.txtautor.delete(0, END)
        self.txteditoria.delete(0, END)
        self.txtano.delete(0, END)



    def buscarLivro(self):
       
        codigolv = self.txtcodigo.get()
        self.lblmsg["text"] = livro.buscaLivro(codigolv)

        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, livro.codigo)

        self.txttituloLv.delete(0, END)
        self.txttituloLv.insert(INSERT, livro.titulo)

        self.txtautor.delete(0, END)
        self.txtautor.insert(INSERT, livro.autor)

        self.txteditoria.delete(0, END)
        self.txteditoria.insert(INSERT, livro.editoria)

        self.txtano.delete(0, END)
        self.txtano.insert(INSERT, livro.ano)
    



    def excluiLivro(self):
       
        codigolv = self.txtcodigo.get()

        self.lblmsg["text"] = livro.deleteLivro(codigolv)

        self.txtcodigo.delete(0, END)
        self.txttituloLv.delete(0, END)
        self.txtautor.delete(0, END)
        self.txteditoria.delete(0, END)
        self.txtano.delete(0, END)



    def atualizaLivro(self):

        #Valida dados
        codigo = self.txtcodigo.get().strip()
        titulo = self.txttituloLv.get().strip()
        autor = self.txtautor.get().strip()
        editoria = self.txteditoria.get().strip()
        ano = self.txtano.get().strip()

        if(codigo == "" or titulo == "" or autor == "" or editoria == "" or ano == ""):
            self.lblmsg["text"] = "Todos os campos são obrigatórios!"
            return
        else:
            try:
                ano = int(ano)
                if ano <= 0:
                    self.lblmsg["text"] = "Ano inválido!"
                    return 
                else:
                    ano = str(ano) #a class espera receber uma string no parametro
            except:
                self.lblmsg["text"] = "Informe um ano válido!"
                return 

        #define parametros
        livro.codigo = codigo
        livro.titulo = titulo
        livro.autor = autor
        livro.editoria = editoria
        livro.ano = ano

        self.lblmsg["text"] = livro.updateLivro()

        self.txtcodigo.delete(0, END)
        self.txttituloLv.delete(0, END)
        self.txtautor.delete(0, END)
        self.txteditoria.delete(0, END)
        self.txtano.delete(0, END)



    def limpaCampos(self):  

        self.txtcodigo.delete(0, END)
        self.txttituloLv.delete(0, END)
        self.txtautor.delete(0, END)
        self.txteditoria.delete(0, END)
        self.txtano.delete(0, END)

#Instância
root = Tk()
livro = Livro()

root.title("POO COM PYTHON :)")
Application(root)
root.mainloop()



