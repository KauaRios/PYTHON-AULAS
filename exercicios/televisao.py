class Televisão:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv1 = Televisão(9 , 2,  10 )
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)

tv2 = Televisão(3 , 2,  10 )
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)