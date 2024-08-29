# Generated by Django 5.1 on 2024-08-29 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "django_chunk_file_upload",
            "0003_rename_file_manager_checksum_idx_filemanager_checksum_idx",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="filemanager",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(class)s_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
