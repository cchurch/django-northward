# Django
from django.db import models

if 0:
    class MigrationHistory(models.Model):

        class Meta:
            db_table = 'south_migrationhistory'
            managed = False

        app_name = models.CharField(max_length=255)
        migration = models.CharField(max_length=255)
        applied = models.DateTimeField(blank=True)
