from django.db import models

class Log(models.Model):

    ORIGIN_CHOICES = [
        ('Produção', 'Produção'),
        ('Homologação', 'Homologação'),
        ('Dev', 'Dev')
    ]

    LEVEL_CHOICES = [
        ('Debug', 'Debug'),
        ('Error', 'Error'),
        ('Warning', 'Warning'),
    ]

    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    origin = models.CharField(max_length=11, choices=ORIGIN_CHOICES, default='Produção')
    level = models.CharField(max_length=7, choices=LEVEL_CHOICES, default='Error')
    
