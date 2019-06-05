class Vendedor:
    def __init__(self,cpf,total):
        self._cpf = cpf
        self._total = total

    def getCPF(self):
        return self._cpf
    def setCPF(self,cpf):
        self._cpf = cpf

    def getTotal(self):
        return self._total
    def setTotal(self,total):
        self._total = total

    def vende(self,venda):
        self._total += venda
