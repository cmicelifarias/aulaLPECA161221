from Banco import Banco

class Usuario:

    def __init__(self, idusuario=0, nome="",telefone="",email="", usuario="",senha=""):
        self.info = {}
        self.idusuario=idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
    
    def insertUser(self):

        banco = Banco()

        c = banco.conexao.cursor()
        comando = "insert into usuarios(nome, telefone,email,usuario, senha) values('"+ self.nome +"', '"+ self.telefone + "','"+ self.email +"','"+ self.usuario +"','"+ self.senha +"')"
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def deleteUser(self):
        pass

    def selectUser(self):
        pass

    def updateUser(self):
        pass

