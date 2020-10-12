# Generated by Django 3.0.4 on 2020-10-12 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_projectbug_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Transport', 'Transport'), ('Food', 'Food'), ('Entertainment', 'Entertainment'), ('Sports', 'Sports')], max_length=50, null=True)),
                ('amount', models.CharField(max_length=20, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectBug',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
