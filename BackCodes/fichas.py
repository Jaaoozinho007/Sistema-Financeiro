

def criar_ficha(usuario):

    ficha = {
        "nome": usuario.nome,
        "saldo_inicial": 1000.00,
        "inventario": [],
        "historico": []
    }

    return ficha