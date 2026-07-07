import pickle

def recupera_pedidos():
    try:
        pedidos = {}
        arq_pedidos = open("pedidos.dat", "rb")
        pedidos = pickle.load(arq_pedidos)
        arq_pedidos.close()
    except: 
        pedidos = {
            '1' : ["12317472000106", "1", 45, "12/12/26", True],
            '2' : ["94170126000158", "3", 34, "31/1/26", True],
            '3' : ["71521817000153", "4", 23, "11/11/26", False],
            '4' : ["23910070000175", "1", 44, "12/2/26", True],
            '5' : ["31921467000137", "2", 21, "30/3/26", False]
        }
        arq_pedidos = open("pedidos.dat", "wb")
        pickle.dump(pedidos, arq_pedidos)
        arq_pedidos.close()
    return pedidos

def grava_pedidos(pedidos):
    arq_pedidos = open("pedidos.dat", "wb")
    pickle.dump(pedidos, arq_pedidos)
    arq_pedidos.close()