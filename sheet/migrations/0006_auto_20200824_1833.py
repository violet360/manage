# Generated by Django 3.1 on 2020-08-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0005_auto_20200824_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='group',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
