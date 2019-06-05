class Remedio:
    def __init__(self,nome,preco,quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getPreco(self):
        return self._preco
    def setPreco(self,preco):
        self._preco = preco

    def getQTD(self):
        return self._quantidade
    def setQTD(self,quantidade):
        self._quantidade = quantidade

    def vende(self,qtd):
        self._quantidade -= qtd
