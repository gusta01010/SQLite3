import sqlite3

class Database: #Classe de banco de dados
    #Funcionalidades:
    #Conecta ao banco de dados
    #Gerencia os dados
    #
    #Banco de dado: user.db
    #Tabela: Users
    #colunas: id (PK, AUTO INCREMENT), name (VARCHAR(30)), money (REAL)
    
    def __init__(self):
        self.sucessful = False
        self.isconnected = False
        self.__db = None
        
    #Verificador de usuário, se o usuário for válido e estiver no banco de dados
    def verificador(self, id):
        self.cursor.execute("SELECT * FROM Users WHERE id=%i"% (self.id)) #Pesquisa pelo valor do id
        if self.cursor.fetchone(): #Verifica se existeum dado encontrado ali, fetch.
            return True
        else:
            print("\033[31mErro:\033[0m ID não encontrado")
            #Antes de retornar falso a condição, ele exibe uma mensagem
            return False
            #Se fosse colocado depois o print, não seria executado a mensagem pois já terminaria a função com seu retorno em False
    
    #Conecta ao banco de dados
    def conectar(self):
        self.__db = sqlite3.connect("user.db")
        self.cursor = self.__db.cursor()
        self.isconnected = True
    
    #Insere dados na tabela Users
    def inserir_dado(self):
        self.nome = str(input("Digite o Nome: "))
        self.valor = float(input("Digite o Valor: "))
        self.cursor.execute("INSERT INTO Users(id, name, money) VALUES (null, ?, ?)", (self.nome, format(self.valor, '.2f'))) #null pois tem auto_increment no id
        self.cursor.execute("SELECT last_insert_rowid() from Users")
        print ("Valor de ID: " + str(list(self.cursor.fetchone())[0]))
        self.__db.commit()
        print("Dados salvos")
        
    def remover_dado(self):
        self.id = int(input("Digite o ID: "))
        if self.verificador(self.id):
            self.cursor.execute("DELETE FROM Users WHERE id=%i"% (self.id))
            self.__db.commit()
            print("Usuário apagado")
        
    def consultar_dado(self):
        self.id = int(input("Digite o ID: "))
        if self.verificador(self.id):
            self.cursor.execute("SELECT * FROM Users WHERE id=%i"% (self.id))
            self.result = self.cursor.fetchall()
            print("==============================================")
            for row in self.result:
                print("ID: " + str(list(row)[0]))
                print("Nome: " + str(list(row)[1]))
                print("Dinheiro: " + str(format((list(row)[2]), '.2f')))
            print("==============================================")
            
    def alterar_dado(self):
        self.id = int(input("Digite o ID: "))
        if self.verificador(self.id):
            print("Deseja editar o nome de usuário? (s/n)")
            self.option = input()
            if self.option == 's':
                self.config = input("Digite o novo nome de usuário: ")
                self.cursor.execute("UPDATE Users SET name = ? WHERE id = ?", (str(self.config), self.id))
                print ("Alteração realizada com sucesso!")
            print("Deseja editar o valor da grana? (s/n)")
            self.option = input()
            if self.option == 's':
                self.config = input("Digite o novo valor: ")
                self.cursor.execute("UPDATE Users SET money = ? WHERE id = ?", (format(self.valor, '.2f'), self.id))
                print ("Alteração realizada com sucesso!")
                self.__db.commit()
            else:
                self.__db.commit()

