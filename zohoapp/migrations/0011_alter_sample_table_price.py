# Generated by Django 4.1.7 on 2023-05-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_alter_sample_table_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_table',
            name='price',
            field=models.IntegerField(),
        ),
    ]
