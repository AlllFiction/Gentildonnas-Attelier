import pickle

def recupera_produtos():
    try:
        produtos = {}
        arq_produtos = open("produtos.dat", "rb")
        produtos = pickle.load(arq_produtos)
        arq_produtos.close()
    except:
        produtos = {
            "1" : ["fedora", 54, "chapeu", 67, True],
            "2" : ["chapeu maluco", 670, "chapeu", 5, True],
            "3" : ["bone de aba reta", 45, "bone", 60, True],
            "4" : ["bone de aba curvada", 50, "bone", 80, True],
            "5" : ["chapeu festivo",  600, "chapeu", 10, False]
        }
        arq_produtos = open("produtos.dat", "wb")
        pickle.dump(produtos, arq_produtos)
        arq_produtos.close()
    return produtos

def grava_produtos(produtos):
    arq_produtos = open("produtos.dat", "wb")
    pickle.dump(produtos, arq_produtos)
    arq_produtos.close()