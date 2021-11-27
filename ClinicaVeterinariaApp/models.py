from django.db import models


# Create your models here.
class Rol(models.Model):
    cod_rol = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True, null=True)
    est_rol = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Especializacion(models.Model):
    cod_esp = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    est_especializacion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especializacion'


class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    clave = models.CharField(max_length=256, blank=True, null=True)
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


class Especie(models.Model):
    cod_especie = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True, null=True)
    est_especie = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especie'


class Raza(models.Model):
    cod_raza = models.AutoField(primary_key=True)
    cod_especie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='cod_especie')
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    est_raza = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raza'


class Color(models.Model):
    cod_color = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True, null=True)
    est_color = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class Mascota(models.Model):
    cod_mascota = models.AutoField(primary_key=True)
    cod_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='cod_usuario')
    nombre = models.CharField(max_length=30, blank=True, null=True)
    cod_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='cod_raza')
    edad = models.SmallIntegerField(blank=True, null=True)
    peso = models.SmallIntegerField(blank=True, null=True)
    fec_nacimiento = models.DateField(blank=True, null=True)
    cod_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='cod_color')
    est_mascota = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota'


class Mediopago(models.Model):
    cod_medpago = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    est_mediopago = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mediopago'


class Factura(models.Model):
    cod_factura = models.AutoField(primary_key=True)
    cod_mascota = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='cod_mascota')
    cod_medpago = models.ForeignKey('Mediopago', models.DO_NOTHING, db_column='cod_medpago')
    fecha = models.DateField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    est_factura = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    est_categoria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Producto(models.Model):
    cod_producto = models.AutoField(primary_key=True)
    cod_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='cod_categoria')
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    desc_producto = models.FloatField(blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    precio_total = models.FloatField(blank=True, null=True)
    est_producto = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Venta(models.Model):
    cod_venta = models.AutoField(primary_key=True)
    cod_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='cod_factura')
    cod_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='cod_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    desc_venta = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    precio_total = models.IntegerField(blank=True, null=True)
    est_venta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
        unique_together = (('cod_factura', 'cod_producto'),)
