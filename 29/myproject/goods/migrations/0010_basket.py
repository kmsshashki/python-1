# Generated by Django 3.0.4 on 2020-04-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_delete_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
                ('total', models.FloatField(default=0)),
            ],
        ),
    ]