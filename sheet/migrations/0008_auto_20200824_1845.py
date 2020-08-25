# Generated by Django 3.1 on 2020-08-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0007_remove_ledger_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='borrower',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='lender',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
