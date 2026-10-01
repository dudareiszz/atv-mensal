from produto import Produto
from venda import Venda

camiseta = Produto("Camiseta", 50.0, 10)
bone = Produto("Boné", 30.0, 5)

venda = Venda()

print(venda.adicionar_item(camiseta, 2))  
print(venda.adicionar_item(bone, 1))      
print(venda.adicionar_item(bone, 10))   

print("Total:", venda.valor_total)       
print("Estoque camiseta:", camiseta.estoque)  
print("Estoque boné:", bone.estoque)         

venda.remover_item(camiseta)
print("Total depois de remover:", venda.valor_total)  
print("Estoque camiseta:", camiseta.estoque)          
