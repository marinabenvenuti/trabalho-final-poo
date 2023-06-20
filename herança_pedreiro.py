from funcionarios import funcionario
class Pedreiro(Funcionario):
    def __init__(self, nome, cpf, fone, salario, qtdObras):
        super().__init__(nome, cpf, fone, salario)
        self.qtdObras = qtdObras
        
    def getQtdObras(self):
        return self.qtdObras
    
    def setQtdObras(self, qtdObras):
        self.qtdObras = qtdObras
