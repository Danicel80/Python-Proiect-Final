# Generated by Django 5.0.2 on 2024-03-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_texts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.IntegerField()),
                ('client_pref', models.TextField()),
                ('client_bas', models.TextField()),
            ],
        ),
    ]
