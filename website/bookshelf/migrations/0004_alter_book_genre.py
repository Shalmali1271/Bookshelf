# Generated by Django 3.2.5 on 2021-07-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_auto_20210709_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('101', 'Narrative'), ('102', 'Fiction'), ('103', 'Non-Fiction'), ('104', 'Mystery'), ('105', 'Science-Fiction'), ('106', 'Historical-Fiction'), ('107', 'Fantasy'), ('108', 'Romance'), ('109', 'Horror'), ('110', 'Thriller')], max_length=100),
        ),
    ]
