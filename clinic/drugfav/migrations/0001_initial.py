# Generated by Django 3.2.10 on 2022-03-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavDrugs',
            fields=[
                ('drugid', models.AutoField(primary_key=True, serialize=False)),
                ('favname', models.CharField(max_length=100)),
                ('favdose', models.CharField(max_length=100)),
            ],
        ),
    ]
