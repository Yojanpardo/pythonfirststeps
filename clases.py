# -*- coding: utf-8 -*-

class Comida(object):
	def __init__(self, principio,proteina):
		self.principio = principio
		self.proteina = proteina
	def almuerzo_principio(self):
		return 'El almuerzo tendrá %s' %self.principio
	def almuerzo_proteina(self):
		print 'e %s' %self.proteina

a=Comida("Lentejas","Hígado")
		
print a.almuerzo_principio()
a.almuerzo_proteina()