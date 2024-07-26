from database import Database

BD = Database()
Options = [0,1,2,3]

while True:
    if not BD.isconnected:
        print("Status da conexão: \033[31mDESCONECTADO\033[0m")
        print("0 - Conectar ao banco de dados\n1 - Inserir dados\n2 - Remover dado\n3 - Mostrar Dados\n4 - Alterar Dados")
        
    else:
        print("Status da conexão: \033[32mCONECTADO\033[0m")
        print("0 - Desconectar\n1 - Inserir dados\n2 - Remover dado\n3 - Mostrar Dados\n4 - Alterar Dados")
    
    option = int(input("Option: "))
    
    if option == 0 and not BD.isconnected:
        BD.conectar()
    
    elif option == 0 and BD.isconnected:
        BD.__db = None
        BD.isconnected = False
        
    elif option == 1 and BD.isconnected:
        BD.inserir_dado()
        
    elif option == 2 and BD.isconnected:
        BD.remover_dado()
        
    elif option == 3 and BD.isconnected:
        BD.consultar_dado()
        
    elif option == 4 and BD.isconnected:
        BD.alterar_dado()
    else:
        print("\033[31mErro\033[0m: Conectado à nenhum banco de dados!\n")
            
        


#db = sqlite3.connect("user.db")
# db.commit() Salva os dados na tabela de forma permanente
#cursor.execute("Select * From Users")
#resultado = cursor.fetchall() #Trás uma lista do resultado, semelhante a list(cursor)
#print(list(resultado[1])[2])