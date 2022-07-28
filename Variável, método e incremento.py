class CanilCao:
	def __init__(self, nome, raca, idade, sexo):
		self.nome = nome
		self.raca = raca
		self.idade = idade
		self.sexo = sexo

	def ExibirInformacoesDesteCanilCao(self):
		print('Nome:', self.nome, ', Raça:', self.raca, ', Idade:',self.idade,'ano(s)', ', Sexo:', self.sexo)

canilcao1= CanilCao('Belinha', 'Poodle', '01', 'Fêmea')
canilcao1.ExibirInformacoesDesteCanilCao()
canilcao2= CanilCao('Costelinha', 'Shih Tzu', '02', 'Macho')
canilcao2.ExibirInformacoesDesteCanilCao()
canilcao3= CanilCao('Dora', 'Beagle', '03', 'Fêmea')
canilcao3.ExibirInformacoesDesteCanilCao()