class Pessoa:
    def __init__(self, nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf

      
    def Logar(self):
        print("voce logou")

ListaUsuario = []
ListaAdmin = []

class Usuario:
    #Construtor
    def __init__(self,nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf
    def logar(self):
        print("Logou")

    def deslogar(self):
        print("sair da conta")

#Classe Pai
class Usuario:
    #Construtor
    def __init__(self,nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf

    def Saudacoes(self):
          print("oi eu sou " + int(self.nome))
          print("e eu tenho " + str(self.numero))
          print("o meu e-mail e " + int(self.email))
          print("do sexo: " + int(self.sexo))
          print("do cpf: " + int(self.cpf))

class Admin(Pessoa):
    def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                nome = (input("Digite o nome do Usuario"))
                email = (input("Digite o E-mail do Usuario"))
                sexo = (input("Digite o sexo do Usuario"))
                numero = str(input("Digite a idade do usuario"))
                cpf = (input("Digite o CPF do Usuario"))

                p = Pessoa(nome, email, sexo, numero, cpf)
                ListaUsuario.append(p)
                
            else:
                x = False
                Admin.menuUI()

    def listar():
            print(ListaUsuario)

    def menuUI():
        print("Escolha uma Opcao")
        print("1 - Adicionar")
        print("2 - listar")
        print("3 - parar")

        escolha = int(input("Digite um numero, para Escolher"))

        if escolha == 1:
            Admin.adicionar()
        elif escolha == 2:
            Admin.listar()
        if escolha == 3:
           print("encerrando...")
           exit()
        else:
            print("opcao invalida!")

Admin.menuUI()