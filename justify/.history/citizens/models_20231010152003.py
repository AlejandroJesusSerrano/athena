from django.db import models

class Province(models.Model):
  province = models.CharField(max_length=50, verbose_name='Provincia')

  def __str__(self):
  return self.province

  class Meta:
    verbose_name = 'Provincia'
    verbose_name_plural = 'Provicias'
    db_table = 'provincia'
    ordering = ['id']

class Citizen(models.Model):
  names = models.CharField(max_length=75, verbose_name='Nombres')
  last_names = models.CharField(max_length=75, verbose_name='Apellidos')
  email = models.EmailField(max_length=80, blank=False, unique=True, verbose_name='Email')
  dni = models.CharField(max_length=8, verbose_name='DNI')
  cuil = models.CharField(max_length=11, unique=True, verbose_name='CUIL')
  province = models.ForeignKey(Province, verbose_name='Provincia', on_delete=models.CASCADE)
  location = models.CharField(max_length=50, verbose_name='Localidad')
  address = models.CharField(max_length=300, verbose_name='Domicilio')
  created_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Registro')

def __str__(self):
  return self.names

class Meta:
  verbose_name = 'Ciudadano'
  verbose_name_plural = 'Ciudadanos'
  db_table = 'ciudadano'
  ordering = ['id']