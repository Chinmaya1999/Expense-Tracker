# Generated by Django 3.0.4 on 2020-03-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
