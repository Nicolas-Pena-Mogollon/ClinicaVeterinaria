from django.db import models


# Create your models here.
class Especializacion(models.Model):
    cod_esp = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    est_especializacion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especializacion'


class Rol(models.Model):
    cod_rol = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True, null=True)
    est_rol = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    clave = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    num_identificacion = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    cod_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='cod_rol')
    direccion = models.CharField(max_length=100, blank=True, null=True)
    tel_fijo = models.CharField(max_length=7, blank=True, null=True)
    tel_celular = models.CharField(max_length=10, blank=True, null=True)
    est_usuario = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarioespec(models.Model):
    cod_user = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='cod_user', primary_key=True)
    cod_esp = models.ForeignKey(Especializacion, models.DO_NOTHING, db_column='cod_esp')

    class Meta:
        managed = False
        db_table = 'usuarioespec'
        unique_together = (('cod_user', 'cod_esp'),)
