#publico
#_protegido
#__private



class ContaBancaria:
    def __init__(self, titular,saldo):
        self.titular = titular #publico
        self._saldo = saldo  #protegido so pessoas especificas tem acesso
        self.__senha="1234"  #privado quase ninguem terá essa informaçao



    #metodo publico acessivel em qualquer lugar
    def depositar(self,valor):
        if valor>0:
            self._saldo+=valor
            print(f"Deposito de {valor} Realizado com sucesso")
        else:
            print("Valor Invalido Para Deposito")



    #metodo protegido: recomendado que usavel apenas por sub classes ou internamente
    def _verificar_saldo(self):
        print(f"saldo Atual: R${self._saldo}")




    #metodo privado: acessivel apenas dentro da classe
    def __verificar_senha(self,senha):
        return senha==self.__senha




    #metodo publico para acessar metodo privado

    def autenticar(self,senha):
        if self.__verificar_senha(senha):
            print("Autenticado com sucesso")
        else:
            print("Senha incorreta")



conta=ContaBancaria("Joao",1000)



print(conta.titular)
conta.depositar(200)


#Atributos e métodos protegidos (pode acessar , mas nao é recomendado)
print(conta._saldo)  #1200 (nao protegido de fato,apenas uma convençao)
conta._verificar_saldo()





#acessando o privado indiretamente
conta.autenticar("1234") #autenticaçao bem sucedida
conta.autenticar("0000") #Senha incorreta