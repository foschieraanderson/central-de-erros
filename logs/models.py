from django.db import models

class Log(models.Model):

    LEVEL_CHOICES = [
        ('Debug', 'Debug'),
        ('Error', 'Error'),
        ('Warning', 'Warning'),
    ]

    title       = models.CharField('Título', max_length=50, blank=False, null=False)
    description = models.TextField('Descrição')
    origin      = models.GenericIPAddressField(protocol='IPv4')
    level       = models.CharField('Nível', max_length=7, choices=LEVEL_CHOICES, default='Error')
    events      = models.IntegerField('Eventos')
    archived    = models.BooleanField('Arquivado', default=False)
    created_at  = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

