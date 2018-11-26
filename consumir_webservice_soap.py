import zeep
client = zeep.Client(wsdl='colocar aqui seu endpoint, lembrar do "?wsdl" no fim ')
#F E I T O !  Conexao realizada!



# caso necessite de user e senha, e o request pede 2 campos:
# Ex (1) :::::   
print(client.service.nome_da_operacao_login('Primeiro atributo, seu user por exemplo', 'Segundo atributo que o request pede, sua senha por exemplo'))  



# Ex (2) :::::
# Multiple choice:
#
# Request pede:
# 
# <nome_da_tag>
#    <nome_da_tag_dois>descricao</nome_da_tag_dois>
#    <nome_da_tag_dois>sumario</nome_da_tag_dois>
# </nome_da_tag>
#
print( client.service.nome_da_operacao('Primeiro atributo', 'Segundo atributo', nome_da_tag="descricao"))