import sqlite3

conexao = sqlite3.connect('baseDeDados.db') #vai criar o arquivo
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,peso REAL NOT NULL)') #execute vai executar comandos sql na database

cursor.execute('INSERT INTO clientes(nome,peso) VALUES("antony",11.5)') #pode ser usado em sql injection
cursor.execute('INSERT INTO clientes(nome,peso) VALUES(?,?)', ('maria',49.0)) #forma correta sem sql injection passando uma tupla de valores
cursor.execute('INSERT INTO clientes(nome,peso) VALUES(:nome,:peso)', {'nome':'joãozinho','peso':28.7}) #forma correta sem sql injection passando um dicionario de valores
cursor.execute('INSERT INTO clientes VALUES(:id,:nome,:peso)', {'id':None,'nome':'joãozinho','peso':28.7}) #forma correta sem sql injection passando um dicionario de valores porem sem a especificação da tabela e passando o id com none pois é auto incremente

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'id':11,'nome':'artorias'}) #forma correta sem sql injection passando um dicionario de valores porem sem a especificação da tabela e passando o id com none pois é auto incremente

cursor.execute('DELETE FROM clientes WHERE id=:id', {'id':6}) #forma correta sem sql injection passando um dicionario de valores porem sem a especificação da tabela e passando o id com none pois é auto incremente
conexao.commit()    #executando o comando descrito

cursor.execute("SELECT * FROM clientes")
#cursor.fetchall()   #executa o comando e busca os valores, tem que comentar senão não executa o for a seguir pois fecha as buscas

for linha in cursor.fetchall(): #criando um foreach
    print(linha)

for linha in cursor.fetchall(): #criando um foreach
    id, nome, peso = linha      #como os dados vem alinhados então é possivel fazer esse alinhamento de recebimento
    print(id, nome, peso)

cursor.execute("SELECT * FROM clientes WHERE id=11")
for linha in cursor.fetchall(): #criando um foreach
    id, nome, peso = linha      #como os dados vem alinhados então é possivel fazer esse alinhamento de recebimento
    print(id, nome, peso)

cursor.execute("SELECT * FROM clientes WHERE id=:id",{'id':27})
for linha in cursor.fetchall(): #criando um foreach
    id, nome, peso = linha      #como os dados vem alinhados então é possivel fazer esse alinhamento de recebimento
    print(id, nome, peso)

cursor.close
conexao.close