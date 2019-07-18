from django.db import models

# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=70)
    statename = models.ForeignKey('States', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class Pincode(models.Model):
    officename = models.CharField(max_length=70)
    pincode = models.IntegerField()
    divisionname = models.CharField(max_length=70)
    regionname = models.CharField(max_length=70)
    circlename = models.CharField(max_length=70)
    taluk = models.CharField(max_length=70)
    resuboffc = models.CharField(max_length=70)
    reheadoffc = models.CharField(max_length=70)
    district = models.ForeignKey(District, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pincode'


class States(models.Model):
    state = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'states'