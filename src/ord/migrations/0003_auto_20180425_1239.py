# Generated by Django 2.0.4 on 2018-04-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ord', '0002_auto_20180425_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orditem',
            name='ord_list',
            field=models.ManyToManyField(to='shop.Book'),
        ),
    ]
