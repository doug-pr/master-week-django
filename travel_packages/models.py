from django.db import models
import os

# Create your models here.
class TravelPackage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Original")
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço com Desconto")
    image = models.ImageField(upload_to='travel_packages/', verbose_name="Imagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")
    
    # Sobrescrever o Método  save no Modelo
    def save(self, *args, **kwargs):
        # Verificar se o objeto já existe no banco
        if self.pk:
            # Buscar o objeto atual no banco
            old_image = TravelPackage.objects.get(pk=self.pk).image
            # Comparar se a imagem foi alerada
            if old_image and old_image != self.image:
                # Remover a imagem antiga do sistema de arquivos
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        # Salvar o novo registro
        super().save(*args, **kwargs)

        # Sobrescrever o Método delete para remover a imagem quando excluir o pacote
        def delete(self, *args, **kwargs):
            # Remover a imagem associada ao pacote
            if self.image and os.path.isfile(self.image.path):
                os.remove(self.image.path)
            #Excluir o registro
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "travel_packages"
        verbose_name = 'pacote de viagem'
        verbose_name_plural = 'pacotes de viagens'
