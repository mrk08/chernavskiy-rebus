# Generated by Django 3.0.3 on 2020-02-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rebus',
            name='text',
            field=models.TextField(),
        ),
    ]
