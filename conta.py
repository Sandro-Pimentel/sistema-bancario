from historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

        @classmethod
        def nova_conta(cls, cliente, numero):
            return cls(numero, cliente)

        @classmethod
        def saldo(self):
            return self._saldo
        
        @classmethod
        def numero(self):
            return self._numero
        
        @classmethod
        def agencia(self):
            return self._agencia
        
        @classmethod
        def cliente(self):
            return self._cliente
        
        @classmethod
        def historico(self):
            return self._historico
        
        def sacar(self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo

            if excedeu_saldo:
                print("\n--- Erro ao processar operação! Saldo insuficiente. ---")

            elif valor > 0:
                self._saldo -= valor
                print("\n--- Saque realizado com sucesso! ---")
                return True
            else: 
                print("\n --- Erro ao processar operação! Valor informado inválido. ---")

            return False
        
        def depositar(self, valor):
            if valor > 0:
               self._saldo += valor
               print("\n--- Depósito realizado com sucesso! ---")
            else:
                print("\n--- Erro ao processar operação! Valor informado inválido. ---")
                return False
            
            return True
