#Marina Benvenuti Cardeal 23103131
#Iago Rodrigues Munoz 23104313
funcionarios= []
pedreiros = []
gestores = []

class Funcionario:
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario):
        self.nome = Fun_Nome
        self.cpf = Fun_CPF
        self.fone = Fun_Fone
        self.cadastro = Fun_Cadastro
        self.salario = Fun_Salario
        
    def setNome(self, nome):
        self.nome = nome
    
    def setCPF(self, cpf):
        self.cpf = cpf
        
    def setFone(self, fone):
        self.fone = fone
        
    def setCadastro(self, cadastro):
        self.cadastro = cadastro
        
    def calculaSalario(self, salario):
        print(f'O salário básico é R${salario}')
        
    def setSalario(self, salarioTot):
        self.salario = salarioTot
                
class Gestor(Funcionario):    
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario, anoContrat):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)
        self.anoContrat = anoContrat
        gestores.append(self)
        funcionarios.append(self)
        
    def setContra(self, contratacao):
        self.anoContrat = contratacao
        
    def calculaSalario(self, salario, anoContrat):
        salarioTot = salario+(500*(2023-self.anoContrat))
        return salarioTot
    
    def setSalario(self, salarioTot):
        self.salario = salarioTot
        
class Pedreiro(Funcionario):
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario, numObras):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)        
        self.numObras= numObras
        funcionarios.append(self)
        pedreiros.append(self)
        
    def calculaSalario(self):
        self.salario = 1500+(350*(self.numObras))
        
    def setNumObras(self):
        self.numObras += 1
        
    def setNumObrasBosta(self):
        self.numObras -= 1      
