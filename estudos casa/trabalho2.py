class Aluno:

    def __init__(self, av, presenca, sim1=0, sim2=0):
        self.Av = av
        self.presenca = presenca
        self.sim1 = sim1
        self.sim2 = sim2

    def get_nota_total(self):
        return self.Av + self.sim1 + self.sim2

    def Passou(self):
        nota_final = self.get_nota_total()
    
        return nota_final >= 6 and self.presenca <= 25

    def Avs(self, Nova_notaAvs):
        self.Av = Nova_notaAvs


class AlunoEspecial(Aluno):
    def Avs(self, Nova_notaAvs):
        self.Av = (self.Av + Nova_notaAvs) / 2





Ana = Aluno(2, 20)


Bia = Aluno(av=5, presenca=20, sim1=1, sim2=1)
Pedro = Aluno(av=5, presenca=50, sim1=1)


Bob = AlunoEspecial(2, 20)



print(f"Pedro.Passou() -> {Pedro.Passou()}")
print(f"Bia.Passou() -> {Bia.Passou()}")
print(f"Ana.Passou() -> {Ana.Passou()}")

Ana.Avs(7)
print("#Ana.Avs(7)")
print(f"Ana.Passou() -> {Ana.Passou()}")

print(f"Bob.Passou() -> {Bob.Passou()}")
Bob.Avs(7)
print("#Bob.Avs(7)")
print(f"Bob.Passou() -> {Bob.Passou()}")