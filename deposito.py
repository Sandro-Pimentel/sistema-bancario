import transacao as t

class Deposito(t.Transacao):
    def __init__(self, valor):
        self.valor = valor