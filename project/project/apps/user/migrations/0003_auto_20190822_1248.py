# Generated by Django 2.2.2 on 2019-08-22 10:48

from django.db import migrations, models
import django.db.models.deletion
import project.apps.user.managers


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0002_actiontoken_temporarytoken'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects',
                 project.apps.user.managers.
                 UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True,
                                    verbose_name='email address'),
        ),
    ]
