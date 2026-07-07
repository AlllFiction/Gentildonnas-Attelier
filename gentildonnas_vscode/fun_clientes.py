import pickle
import os

def recupera_clientes():
    try:
        clientes = {}
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
        arq_clientes.close()
    except:
        clientes = {
            '02317472000106' : ["Pristine Mirror", "84977158718", "Caicó", "RN", True],
            '94170126000158' : ["Sailor Mars", "21969926402", "Rio de Janeiro", "RJ", True],
            '71521817000153' : ["The Almighty", "84928412260", "Pau dos Ferros", "RN", True],
            '23910070000175' : ["Michelle my Baby", "51910578289", "Gramados", "RS", False],
            '31921467000137' : ["White Lightining", "11936454950", "São Paulo", "SP", False]
        }
        arq_clientes = open("clientes.dat", "wb")
        pickle.dump(clientes, arq_clientes)
        arq_clientes.close()
    return clientes

def grava_clientes(clientes):
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()


def confirma_cnpj(cnpj):
    cnpj = cnpj.replace('/', '').replace('-', '').replace('.', '').replace(' ', '')

    if len(cnpj) != 14:
        return False
    
    for i in range (14):
        if (cnpj[i] < '0' or cnpj[i] > '9'):
            return False

    if cnpj == cnpj[0] * 14:
        return False
    
    return True

def confirma_tel(telefone):
    telefone = telefone.replace('/', '').replace('-', '').replace('.', '').replace(' ', '')
    if len(telefone) != 11:
        return False
    
    return True


def confirma_local(local):
    local.lower()
    if not local.isalpha():
        return False
    
    return True
    
def confirma_uf(uf):
    uf.upper()
    if not uf.isalpha():
        return False
    
    if len(uf) != '2':
        return False
    
    return True


