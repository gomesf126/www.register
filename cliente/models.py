from django.db import models

class ClienteBD(models.Model):
	nome = models.CharField(max_length=30)
	sobre_nome= models.CharField(max_length=30)
	idade = models.CharField(max_length=30)
	cpf = models.CharField(max_length=30)
	foto = models.ImageField(upload_to= 'fotos_clientes', null=True, blank=True)
	#criar um relacionamento de um para um 

	def __str__(self):
		return self.nome + ' ' + self.sobre_nome



