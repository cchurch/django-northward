# Python
import sys

# Django
import django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):

    help = ''

    requires_model_validation = False

    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', '1'))
        assert django.VERSION < (1, 7)
        from south import migration
        from south.models import MigrationHistory

        try:
            MigrationHistory.objects.count()
        except OperationalError:
            return

        apps  = list(migration.all_migrations())
        applied_migrations = MigrationHistory.objects.filter(app_name__in=[app.app_label() for app in apps])
        applied_migrations = ['%s.%s' % (mi.app_name, mi.migration) for mi in applied_migrations]

        for app in apps:
            for app_migration in app:
                migration_name = '%s.%s' % (app_migration.app_label(), app_migration.name())
                
                print migration_name, bool(migration_name in applied_migrations)
                if migration_name not in applied_migrations:
                    result = migration.migrate_app(
                        app,
                        app_migration.name(),
                        verbosity = verbosity,
                        db_dry_run = True,
                    )
                    if result is False:
                        sys.exit('Migration %s failed.' % migration_name)
