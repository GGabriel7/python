from funcionalidadesTV import *

tv = Televisor('SONY', 'SONY-123')

controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.listaCanais)
print(tv.canalAtual)