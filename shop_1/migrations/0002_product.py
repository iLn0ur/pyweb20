# Generated by Django 3.0.3 on 2020-11-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=25)),
                ('discount', models.IntegerField()),
                ('price_dc', models.FloatField()),
                ('price_sale', models.FloatField()),
                ('type', models.CharField(choices=[('fruits', 'fruits'), ('vegetables', 'vegetables')], max_length=10)),
            ],
        ),
    ]
