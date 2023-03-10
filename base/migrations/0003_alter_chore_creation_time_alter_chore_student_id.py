# Generated by Django 4.1.4 on 2023-01-25 16:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_alter_chore_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 16, 14, 44, 373710, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='chore',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
